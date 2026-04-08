#!/usr/bin/env python3
"""
Semantic Chunker - Sliding window text chunking for LLM Wiki

Splits extracted text into overlapping chunks for chapter detection.

Usage:
    python3 chunker.py <input.txt> <output_dir> [--window 5000] [--overlap 500]

Args:
    input.txt: Path to the extracted text file
    output_dir: Directory to write chunk files (e.g. raw/<book>/chunks)
    --window: Window size in words (default: 5000)
    --overlap: Overlap between windows in words (default: 500)

Output:
    chunk-001.md, chunk-002.md, etc. in the output directory
"""

import sys
import os
import argparse

CHUNK_PREFIX = "chunk"


def get_word_windows(text, window_size, step_size):
    """Generate sliding window chunks from text."""
    words = text.split()
    total_words = len(words)

    if total_words <= window_size:
        yield text
        return

    start = 0
    while start < total_words:
        end = min(start + window_size, total_words)
        chunk_words = words[start:end]
        yield ' '.join(chunk_words)
        start += step_size


def chunk_file(input_path, output_dir, window_size, overlap):
    """Chunk a text file into overlapping pieces."""
    with open(input_path, 'r', encoding='utf-8') as f:
        text = f.read()

    if not text.strip():
        print("Error: Input file is empty", file=sys.stderr)
        return 1

    os.makedirs(output_dir, exist_ok=True)

    step_size = window_size - overlap
    book_name = os.path.splitext(os.path.basename(input_path))[0]

    total_chunks = 0
    for content in get_word_windows(text, window_size, step_size):
        total_chunks += 1
        chunk_filename = f"{CHUNK_PREFIX}-{total_chunks:03d}.md"
        chunk_path = os.path.join(output_dir, chunk_filename)

        with open(chunk_path, 'w', encoding='utf-8') as f:
            f.write(f"# {book_name} - Chunk {total_chunks}\n\n")
            f.write(content)

        print(f"Created: {chunk_filename} ({len(content.split())} words)")

    print(f"\nTotal chunks: {total_chunks}")
    return 0


def main():
    parser = argparse.ArgumentParser(description='Chunk text file into overlapping pieces')
    parser.add_argument('input', help='Input text file path')
    parser.add_argument('output_dir', help='Output directory for chunks')
    parser.add_argument('--window', type=int, default=5000, help='Window size in words (default: 5000)')
    parser.add_argument('--overlap', type=int, default=500, help='Overlap in words (default: 500)')
    args = parser.parse_args()

    if not os.path.exists(args.input):
        print(f"Error: Input file not found: {args.input}", file=sys.stderr)
        sys.exit(1)

    if args.window <= 0:
        print("Error: Window size must be positive", file=sys.stderr)
        sys.exit(1)
    if args.overlap < 0:
        print("Error: Overlap must be non-negative", file=sys.stderr)
        sys.exit(1)
    if args.overlap >= args.window:
        print("Error: Overlap must be less than window size", file=sys.stderr)
        sys.exit(1)

    print(f"Chunking: {args.input}")
    print(f"Output: {args.output_dir}")
    print(f"Window: {args.window} words, Overlap: {args.overlap} words")
    print("-" * 50)

    sys.exit(chunk_file(args.input, args.output_dir, args.window, args.overlap))


if __name__ == '__main__':
    main()
