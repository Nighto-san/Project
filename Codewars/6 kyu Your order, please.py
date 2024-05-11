def order(sentence):
    res = dict()
    for word in sentence.split():
        for symbol in word:
            if symbol.isdigit():
                res[word] = symbol
    return ' '.join(sorted(res, key=lambda x: res[x] ))

print(order("is2 Thi1s T4est 3a"), "Thi1s is2 3a T4est", sep='\n')
print(order("4of Fo1r pe6ople g3ood th5e the2"), "Fo1r the2 g3ood 4of th5e pe6ople", sep='\n')
print(order(""), "")