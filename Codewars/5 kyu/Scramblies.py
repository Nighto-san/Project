def scramble(s1, s2):
    letters = {}
    for char in s1:
        letters[char] = letters.get(char, 0) + 1
    for char in s2:
        if letters.get(char, 0) > 0:
            letters[char] -= 1
        else:
            return False
    return True




print(scramble('rkqodlw', 'world'))