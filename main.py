from stats import count_words
from stats import get_lowered_char_freq
from stats import sort_dict_by_value
def get_book_text(filepath):
    with open(filepath) as f:
        book = f.read()
        return book

def main():
    book = get_book_text("books/frankenstein.txt")
    print(str(count_words(book)) + " words found in the document")
    lowered = get_lowered_char_freq(book)
    print(lowered)
    sorted = sort_dict_by_value(lowered)
    for item in sorted:
        if item["char"].isalpha():
           print(item["char"], item["num"])
if __name__ == "__main__":
    main()