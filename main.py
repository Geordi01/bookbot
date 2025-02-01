def main():
    book_path = "books/frankenstein.txt"
    text = get_book_text(book_path)
    num_words = count_words(text)
    char_dict = count_char(text)
    char_sort = sort_char(char_dict)
    
    print(f"--- Begin report of {book_path} ---")
    print(f"{num_words} words found in the document")
    print("")
    for char in char_sort:
        print(f"The '{char["char"]}' character was found {char["count"]} times")
    print("--- End report ---")

def count_words(text):
    words = text.split()
    return len(words)

def count_char(text):
    char_dict = {}
    lowered_letters = text.lower()
    for char in lowered_letters:
        if char not in char_dict:
            char_dict[char] = 1
        else:
            char_dict[char] += 1
    return char_dict

def sort_char(char_count):
    char_list = []
    for char in char_count:
        if char.isalpha():
            char_list.append({"char": char, "count": char_count[char]})
    char_list.sort(reverse=True, key=sort_on)
    return char_list

def sort_on(dict):
    return dict["count"]

def get_book_text(path):
    with open(path) as f:
        return f.read()

main()