def is_pangram(st):
    return len(set(i.lower() for i in st if i.isalpha())) == 26



print(is_pangram("The quick brown fox jumps over the lazy dog."))



