def get_book_text(filepath):
    with open(filepath) as f:
        book = f.read()
        return book

def main():
    book = get_book_text("books/frankenstein.txt")
    print(book)

if __name__ == "__main__":
    main()

from stats import count_words

print(str(count_words(get_book_text("books/frankenstein.txt"))) + " words found in the document")
