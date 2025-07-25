def get_book_text(book):
    book = f.read()

def main(get_book_text):
    book = get_book_text("frankenstein.txt")
    print(book)
main(get_book_text)