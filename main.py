def main():
    book_path = "books/frankenstein.txt"
    text = get_book_text(book_path)
    print_report(text)

def get_book_text(path):
    with open(path) as f:
        return f.read()

def count_words(text):
    words = text.split()
    return len(words)

def get_letters(text):
    chars = {}
    for c in text:
        lowered = c.lower()
        if lowered in chars:
            chars[lowered] += 1
        else:
            chars[lowered] = 1
    return chars

def sort_on(dict):
    return dict["num"]

def get_dict_list(dict):
    dict_list = []
    for letter in dict:
        letter_number = dict[letter]
        new_dict = {}
        new_dict["letter"] = letter
        new_dict["num"] = letter_number
        dict_list.append(new_dict)
    dict_list.sort(reverse=True, key=sort_on)
    return dict_list

def print_report(text):
    print("--- Begin report of books/frankenstein.txt ----")
    print(f"{count_words(text)} words found in the document\n")
    letter_dict = get_letters(text)
    dict_list = get_dict_list(letter_dict)
    for dict in dict_list:
        letter = dict["letter"]
        number = dict["num"]
        if letter.isalpha():
            print(f"The {letter} character was found {number} times")
    print("--- End report ---")
main()
