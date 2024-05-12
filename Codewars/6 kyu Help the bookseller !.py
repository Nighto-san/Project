def stock_list(catalog, strs):
    if len(strs) == 0 or len(catalog) == 0: return
    res = {}
    re = ''
    for s in strs:
        res.setdefault(s, 0)
        for v in catalog:
            if s == v[0]:
                res[s] += int(v.split()[1])
    for k,v in res.items():
        re +=f'({k} : {v}) - '

    return re.strip(' -')



b = ["BBAR 150", "CDXE 515", "BKWR 250", "BTSQ 890", "DRTY 600"]
c = ["A", "B", "C", "D"]



print(stock_list(b, c),'\n', "(A : 0) - (B : 1290) - (C : 515) - (D : 600)")
