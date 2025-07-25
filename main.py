from stats import count_words
from stats import get_lowered_char_freq
from stats import sort_dict_by_value
def get_book_text(filepath):
    with open(filepath) as f:
        book = f.read()
        return book

def main():
    book = get_book_text("books/frankenstein.txt")
    lowered = get_lowered_char_freq(book)
    sorted_chars = sort_dict_by_value(lowered)
    print("============ BOOKBOT ============")
    print("Analyzing book found at books/frankenstein.txt...")
    print("----------- Word Count ----------")
    print(f"Found {count_words(book)} total words")
    print("--------- Character Count -------")

    for item in sorted_chars:
        if item["char"].isalpha():
           print(f"{item['char']}: {item['num']}")
    print("============= END ===============")
if __name__ == "__main__":
    main()