def parse(data):
    c = 0
    res = []
    for i in data:
        if i == 'o':
            res.append(c)
        elif i == 'i': c += 1
        elif i == 'd': c -= 1
        elif i == 's': c = c**2
    return res



print(parse("isoisoiso"), [1,4,25])