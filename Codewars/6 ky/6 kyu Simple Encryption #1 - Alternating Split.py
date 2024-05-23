def decrypt(e_text, n):
    if not e_text: return e_text
    for _ in range(n):
        res = [None] * len(e_text)
        res[::2] = e_text[len(e_text) // 2:]
        res[1::2] = e_text[:len(e_text) // 2]
        e_text = ''.join(res)

    return e_text


def encrypt(text, n):
    if not text: return text
    for _ in range(n):
        text = text[1::2] + text[::2]

    return text



print(encrypt("This is a test!", 0), "This is a test!",sep='\n')
print()
print(encrypt("This is a test!", 1), "hsi  etTi sats!",sep='\n')
print()
print(encrypt("This is a test!", 2), "s eT ashi tist!",sep='\n')

print(decrypt("This is a test!", 0), "This is a test!",sep='\n')
print()
print(decrypt("hsi  etTi sats!", 1), "This is a test!",sep='\n')
print()
print(decrypt("s eT ashi tist!", 2), "This is a test!",sep='\n')