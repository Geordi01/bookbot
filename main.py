import sys
from stats import count_words, count_char, sort_char, get_book_text

def main():
    print(sys.argv)
    book_path = sys.argv[1]
    text = get_book_text(book_path)
    num_words = count_words(text)
    char_dict = count_char(text)
    char_sort = sort_char(char_dict)
    
    print(f"--- Begin report of {book_path} ---")
    print(f"{num_words} words found in the document")
    print("")
    for char in char_sort:
        print(f"{char["char"]}: {char["count"]}")
    print("--- End report ---")

main()