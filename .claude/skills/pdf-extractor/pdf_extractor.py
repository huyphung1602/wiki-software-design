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

            # Extract each page
            for i, page in enumerate(pdf.pages, 1):
                text = page.extract_text()
                if text:
                    result['pages'].append({
                        'page_number': i,
                        'content': text
                    })

        # Write to txt file (not JSON)
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
