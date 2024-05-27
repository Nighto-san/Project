def to_weird_case(words):
    res =[]
    for word in words.split():
        w = ""
        for i in range(len(word)):
            if i%2 == 0:
                w+=word[i].upper()
            else:
                w+=word[i].lower()
        res.append(w)
    return " ".join(res)


print(to_weird_case('THIs iS a TEST'), 'ThIs Is A TeSt')