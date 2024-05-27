d = {'a':'1','e':'2','i':'3','o':'4','u':'5'}


def encode(st):
    res = ''
    for i in st:
        if i in d:res += d[i]
        else:res += i
    return res

def decode(st):
    res = ''
    new_d = dict(zip(d.values(),d.keys()))
    for i in st:
        if i in new_d:res += new_d[i]
        else:res += i
    return res


