def in_array(a1, a2):
    res =[]
    for i in set(a1):
        if i in " ".join(set(a2)):
            res.append(i)
    return sorted(res)