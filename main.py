from stats import *
import sys

def get_book_text(path):
    with open(path, 'r', encoding='utf-8') as file:
        return file.read()

def main():
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    book_path = sys.argv[1]
    book_text = get_book_text(book_path)
    print(f'Found {word_count(book_text)} total words')
    sorted_counts = sorted_char_count(book_text)
    for entry in sorted_counts:
        print(f"{entry['char']}: {entry['num']}")
main()