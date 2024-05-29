def rev_rot(strng, sz):
    if sz <= 0 or strng == '' or sz > len(strng):
        return ''
    ss = [int(i) for i in strng]
    res = []
    for i in range(0, len(strng) - len(strng) % sz, sz):
        sr = ss[i:i + sz]
        if sum(sr) % 2 == 0:
            res.append(''.join(str(x) for x in sr[::-1]))
        else:
            res.append(''.join(str(x) for x in sr[1:]) + str(sr[0]))
    return ''.join(res)








print(rev_rot("733049910872815764",5))