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