def digital_root(n):
    while len(str(n)) != 1: n = sum(int(i) for i in str(n))
    return n


print(digital_root(493193)) # -> 2