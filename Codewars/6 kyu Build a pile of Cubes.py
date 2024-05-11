def find_nb(m):
    res = 0
    c = 0
    while res < m:
        c +=1
        res += c**3

    if res == m:  return c
    else:   return -1



print(find_nb(16), -1)
print(find_nb(4183059834009), 2022)
print(find_nb(24723578342962), -1)
print(find_nb(135440716410000), 4824)
print(find_nb(26825883955641), 3218)