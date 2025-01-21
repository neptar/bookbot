def main():
    print("--- Begin report of books/frankenstein.txt ---")
    book_path = "books/frankenstein.txt"
    text = get_book_text(book_path)
    num_words = get_num_words(text)
    print(f"{num_words} words found in the document")
    print()
    char_dict = get_char_counts(text)
    char_list = sorted(char_dict, key=char_dict.get, reverse=True)
    for cd in char_list:
        print(f"The '{cd}' character was found {char_dict[cd]} times")
    print("--- End report ---")

def get_char_counts(text):
    lower_text = text.lower()
    char_dict = {}
    for c in lower_text:
        if not c.isalpha():
            next       
        elif c in char_dict:
            char_dict[c] += 1
        else:
            char_dict[c] = 1
    return char_dict

def get_num_words(text):
    words = text.split()
    return len(words)


def get_book_text(path):
    with open(path) as f:
        return f.read()


main()