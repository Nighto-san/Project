def encrypt_this(text):
    res = []
    for word in text.split():
        if len(word) == 1:
            res.append(str(ord(word[0])))
        elif len(word) == 2:
            res.append(str(ord(word[0])) + word[-1] )
        else:
            res.append(str(ord(word[0])) + word[-1] + word[2:-1]+ word[1])
    return ' '.join(res)

print(encrypt_this("The less he spoke the more he heard"))
print('84eh 108sse 104e 115eokp 116eh 109ero 104e 104dare')