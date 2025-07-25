def count_words(text):
    words = text.split()
    return len(words)
def get_book_text(filepath):
    with open(filepath) as f:
        book = f.read()
        return book
chars = get_book_text("books/frankenstein.txt")
lowered = chars.lower()
freq = {}

for c in lowered:
    if c in freq:
        freq[c] += 1
    else:
        freq[c] = 1

print(freq)