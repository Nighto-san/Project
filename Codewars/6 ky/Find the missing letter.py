def find_missing_letter(chars):
    c = ord(chars[0])
    for i in chars:
        if ord(i) != c:
            return chr(ord(i)-1)
        c = ord(i)+1

    return



print(find_missing_letter(['a','b','c','d','f']), 'e')