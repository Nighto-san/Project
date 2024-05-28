def parts_sums(ls):
    res =[]
    s = sum(ls)
    res.append(s)
    for i in range(len(ls)):
        res.append(s-ls[i])
        s = s-ls[i]
    return res



print(parts_sums([0, 1, 3, 6, 10]))