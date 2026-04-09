#!/usr/bin/env python3
"""
PDF Extractor - Extract text from PDF to plain text file

Usage:
    python3 pdf_extractor.py <pdf_file> [output_txt_path]

Args:
    pdf_file: Path to the PDF file to extract
    output_txt_path: (Optional) Path to write txt file.
                    If not provided, writes to same directory as pdf
                    with .txt extension

Output:
    Plain text file with extracted content
"""

import sys
import os
import json
import pdfplumber
import fitz  # PyMuPDF — for image extraction


def cluster_drawings_to_figures(drawings, page_width, page_height, min_figure_size=0.02):
    """
    Cluster drawing paths into distinct figure regions.

    Merges overlapping/nearby drawing bboxes and filters out small decorative
    elements (arrows, borders) to identify coherent figures.

    Args:
        drawings: List of drawing dicts from fitz_page.get_drawings()
        page_width: Page width for relative size calculations
        page_height: Page height for relative size calculations
        min_figure_size: Min figure size as fraction of page dimension (default 2%)

    Returns:
        List of (bbox, element_count) tuples for identified figures
    """
    if not drawings:
        return []

    # Collect all drawing bboxes
    bboxes = []
    for d in drawings:
        if d.get("rect"):
            bbox = d["rect"]
            bboxes.append({
                "x0": bbox.x0,
                "y0": bbox.y0,
                "x1": bbox.x1,
                "y1": bbox.y1,
            })

    if not bboxes:
        return []

    # Merge overlapping or nearby bboxes (within 5% of page size threshold)
    merge_threshold = min(page_width, page_height) * 0.05

    def should_merge(b1, b2):
        # Check if bboxes are close enough to merge
        horizontal_gap = max(0, max(b1["x0"], b2["x0"]) - min(b1["x1"], b2["x1"]))
        vertical_gap = max(0, max(b1["y0"], b2["y0"]) - min(b1["y1"], b2["y1"]))
        return horizontal_gap < merge_threshold and vertical_gap < merge_threshold

    def merge_bbox(b1, b2):
        return {
            "x0": min(b1["x0"], b2["x0"]),
            "y0": min(b1["y0"], b2["y0"]),
            "x1": max(b1["x1"], b2["x1"]),
            "y1": max(b1["y1"], b2["y1"]),
        }

    merged = []
    for bbox in bboxes:
        matched = False
        for i, existing in enumerate(merged):
            if should_merge(existing, bbox):
                merged[i] = merge_bbox(existing, bbox)
                matched = True
                break
        if not matched:
            merged.append(bbox)

    # Filter by size (filter out small arrows, decorative elements)
    min_width = page_width * min_figure_size
    min_height = page_height * min_figure_size
    figures = []
    for bbox in merged:
        width = bbox["x1"] - bbox["x0"]
        height = bbox["y1"] - bbox["y0"]
        # Also filter out anything that's very thin (likely arrows/borders)
        aspect_ratio = width / height if height > 0 else 0
        if width >= min_width and height >= min_height and 0.05 < aspect_ratio < 20:
            # Count how many original drawings fall into this figure
            elem_count = sum(1 for d in drawings if d.get("rect") and
                           bbox["x0"] <= d["rect"].x0 and bbox["y0"] <= d["rect"].y0 and
                           bbox["x1"] >= d["rect"].x1 and bbox["y1"] >= d["rect"].y1)
            figures.append((bbox, elem_count))

    # Sort by position (top-to-bottom, left-to-right)
    figures.sort(key=lambda x: (x[0]["y0"], x[0]["x0"]))

    # Filter out regions fully contained within other regions
    # (keep larger regions, discard nested sub-regions)
    filtered = []
    for bbox, elem_count in figures:
        is_contained = False
        for larger_bbox, _ in filtered:
            # Check if this bbox is fully inside the larger one
            if (larger_bbox["x0"] <= bbox["x0"] and larger_bbox["y0"] <= bbox["y0"] and
                larger_bbox["x1"] >= bbox["x1"] and larger_bbox["y1"] >= bbox["y1"]):
                is_contained = True
                break
        if not is_contained:
            filtered.append((bbox, elem_count))

    return filtered


def extract_figures_from_page(fitz_page, page_num, img_dir, dpi=150):
    """
    Extract vector figures from a PDF page by analyzing drawing regions.

    Clusters drawing paths into distinct figures, filters small decorative
    elements, and saves each figure as a cropped PNG.

    Args:
        fitz_page: PyMuPDF page object
        page_num: 1-indexed page number
        img_dir: Directory to save images
        dpi: Resolution for rendering (default 150)

    Returns:
        List of dicts with 'filename' for each extracted figure
    """
    image_info = []
    drawings = fitz_page.get_drawings()

    if not drawings:
        return image_info

    page_rect = fitz_page.rect
    page_width = page_rect.width
    page_height = page_rect.height

    # Cluster drawings into figures
    figures = cluster_drawings_to_figures(drawings, page_width, page_height)

    for fig_idx, (bbox, elem_count) in enumerate(figures, 1):
        # Add padding around the figure (5% of figure size)
        pad_x = (bbox["x1"] - bbox["x0"]) * 0.05
        pad_y = (bbox["y1"] - bbox["y0"]) * 0.05

        clip_rect = fitz.Rect(
            max(0, bbox["x0"] - pad_x),
            max(0, bbox["y0"] - pad_y),
            min(page_width, bbox["x1"] + pad_x),
            min(page_height, bbox["y1"] + pad_y),
        )

        # Render just the figure region
        pix = fitz_page.get_pixmap(dpi=dpi, clip=clip_rect)
        filename = f"page-{page_num:03d}-fig-{fig_idx:02d}.png"
        filepath = os.path.join(img_dir, filename)
        pix.save(filepath)

        image_info.append({
            "filename": filename,
            "img_idx": fig_idx,
        })

    return image_info


def extract_images_from_page(fitz_page, page_num, img_dir):
    """
    Extract images from a single PDF page using PyMuPDF.
    Handles embedded raster images and vector graphics as per-figure crops.

    Args:
        fitz_page: PyMuPDF page object
        page_num: 1-indexed page number
        img_dir: Directory to save images

    Returns:
        List of dicts with 'filename' for each extracted image
    """
    image_info = []
    img_list = fitz_page.get_images(full=True)

    # Pass 1: Extract embedded raster images
    for img_idx, img_ref in enumerate(img_list, 1):
        xref = img_ref[0]
        try:
            base_image = fitz_page.parent.extract_image(xref)
            if base_image and base_image.get("image"):
                ext = base_image["ext"]
                img_bytes = base_image["image"]
                filename = f"page-{page_num:03d}-img-{img_idx:02d}.{ext}"
                filepath = os.path.join(img_dir, filename)
                with open(filepath, "wb") as f:
                    f.write(img_bytes)
                image_info.append({
                    "filename": filename,
                    "img_idx": img_idx,
                })
        except Exception as e:
            print(f"Warning: Failed to extract image {img_idx} from page {page_num}: {e}", file=sys.stderr)
            continue

    # Pass 2: Extract vector figures as per-figure crops
    # (replaces the old "whole page as one PNG" fallback)
    figures = extract_figures_from_page(fitz_page, page_num, img_dir)
    image_info.extend(figures)

    return image_info


def insert_image_placeholders(page_text, images_on_page, plumber_page):
    """
    Insert [Image: ...] placeholders into extracted text at approximate positions.

    Matches images to pdfplumber bounding boxes by index (both list images in
    the same order for typical PDFs). For vector-only pages, inserts at end.

    Args:
        page_text: Extracted text from pdfplumber
        images_on_page: List of image info dicts from extract_images_from_page
        plumber_page: pdfplumber page object for coordinate access

    Returns:
        Modified text with image placeholders inserted
    """
    if not images_on_page or not page_text:
        return page_text

    plumber_images = plumber_page.images
    text_lines = plumber_page.extract_text_lines()

    if not text_lines:
        for img in images_on_page:
            page_text += f"\n\n[Image: {img['filename']}]\n"
        return page_text

    # Build insertion points: (line_index_to_insert_after, placeholder_text)
    # Process in reverse order so insertions don't shift earlier indices
    insertions = []

    for i, img in enumerate(images_on_page):
        # Match image to pdfplumber bbox by index
        if i < len(plumber_images):
            img_top = plumber_images[i]["top"]
        else:
            # More images than pdfplumber found — append at end
            insertions.append((len(text_lines) - 1, f"\n[Image: {img['filename']}]\n"))
            continue

        # Find the last text line above the image's top coordinate
        best_line_idx = -1
        for idx, line in enumerate(text_lines):
            if line["top"] < img_top:
                best_line_idx = idx

        placeholder = f"\n[Image: {img['filename']}]\n"

        if best_line_idx >= 0:
            insertions.append((best_line_idx, placeholder))
        else:
            # Image is above all text — insert at start
            insertions.append((-1, placeholder))

    # Sort by line index descending so we insert from bottom up
    insertions.sort(key=lambda x: x[0], reverse=True)

    # Split text into segments after each text_line's text
    segments = []
    remaining = page_text
    for tl in text_lines:
        tl_text = tl["text"]
        idx = remaining.find(tl_text)
        if idx >= 0:
            segments.append(remaining[:idx + len(tl_text)])
            remaining = remaining[idx + len(tl_text):]
        else:
            print(f"Warning: Could not locate text line in page text, skipping segment", file=sys.stderr)
            segments.append("")
    if remaining:
        segments.append(remaining)

    # Apply insertions in reverse order (high index first)
    for line_idx, placeholder in insertions:
        if line_idx == -1:
            segments.insert(0, placeholder)
        elif line_idx < len(segments):
            segments[line_idx] += placeholder
        else:
            segments[-1] += placeholder

    return "".join(segments)


def extract_pdf_to_txt(pdf_path, output_path=None):
    """
    Extract text from PDF and write to txt file.

    Args:
        pdf_path: Path to input PDF
        output_path: Path to output txt file (optional)
    """
    if output_path is None:
        # Default: same name as PDF but .txt
        output_path = os.path.splitext(pdf_path)[0] + '.txt'

    result = {
        'title': '',
        'pages': []
    }

    try:
        with pdfplumber.open(pdf_path) as pdf:
            # Try to extract title from first page
            if len(pdf.pages) > 0:
                first_page = pdf.pages[0]
                for char in first_page.chars:
                    if char.get('size', 0) > 16:
                        result['title'] += char.get('text', '')
                result['title'] = result['title'].strip()

            with fitz.open(pdf_path) as fitz_doc:

                # Create image output directory once
                img_dir = os.path.join(os.path.dirname(output_path), "images")
                os.makedirs(img_dir, exist_ok=True)

                # Extract each page
                for i, page in enumerate(pdf.pages, 1):
                    text = page.extract_text()

                    # Extract images using PyMuPDF
                    fitz_page = fitz_doc[i - 1]
                    images = extract_images_from_page(fitz_page, i, img_dir)

                    # Insert image placeholders into text
                    if images and text:
                        text = insert_image_placeholders(text, images, page)

                    if text:
                        result['pages'].append({
                            'page_number': i,
                            'content': text
                        })

        # Write to txt file (not JSON)
        if os.path.exists(output_path):
            print(f"Warning: Overwriting existing {output_path}")
        with open(output_path, 'w', encoding='utf-8') as f:
            # Write title if found
            if result['title']:
                f.write(result['title'] + '\n\n')

            # Write page content
            for page_data in result['pages']:
                f.write(f"---\n")
                f.write(f"Page {page_data['page_number']}\n")
                f.write(f"---\n\n")
                f.write(page_data['content'])
                f.write('\n\n')

        print(f"Extracted: {output_path}")
        return 0

    except Exception as e:
        print(f"Error: {e}", file=sys.stderr)
        return 1


def main():
    if len(sys.argv) < 2:
        print('Usage: python pdf_extractor.py <pdf_file> [output_txt_path]', file=sys.stderr)
        sys.exit(1)

    pdf_path = sys.argv[1]
    output_path = sys.argv[2] if len(sys.argv) > 2 else None

    if not os.path.exists(pdf_path):
        print(f"Error: PDF file not found: {pdf_path}", file=sys.stderr)
        sys.exit(1)

    sys.exit(extract_pdf_to_txt(pdf_path, output_path))


if __name__ == '__main__':
    main()
