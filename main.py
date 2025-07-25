from stats import count_words
from stats import get_lowered_char_freq
def get_book_text(filepath):
    with open(filepath) as f:
        book = f.read()
        return book

def main():
    book = get_book_text("books/frankenstein.txt")
    print(str(count_words(book)) + " words found in the document")
    lowered = get_lowered_char_freq(book)
    print(lowered)
if __name__ == "__main__":
    main()