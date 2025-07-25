def count_words(text):
    words = text.split()
    return len(words)
    
def get_lowered_char_freq(book):
        lowered = book.lower()
        freq = {}
        for c in lowered:
            if c in freq:
                freq[c] += 1
            else:
                freq[c] = 1
        return freq
def sort_dict_by_value(d):
    return[{"char": c, "num": n} for c, n in sorted(d.items(), key=lambda item: item[1], reverse=True)]