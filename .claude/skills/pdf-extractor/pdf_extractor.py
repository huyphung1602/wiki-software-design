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


def extract_images_from_page(fitz_page, page_num, img_dir):
    """
    Extract images from a single PDF page using PyMuPDF.
    Handles both embedded raster images and vector graphics.

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

    # Pass 2: Extract vector graphics as rendered PNGs
    # Vector drawings are common in technical diagrams and won't appear in get_images()
    drawings = fitz_page.get_drawings()
    if drawings and not img_list:
        # Page has vector drawings but no raster images — render the full page as PNG
        filename = f"page-{page_num:03d}-img-vector.png"
        filepath = os.path.join(img_dir, filename)
        pix = fitz_page.get_pixmap(dpi=150)
        pix.save(filepath)
        image_info.append({
            "filename": filename,
            "img_idx": 1,
        })

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
