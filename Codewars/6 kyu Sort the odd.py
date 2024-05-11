def sort_array(source_array):
    sort_a = sorted([i for i in source_array if i % 2 != 0])
    c = 0
    res = []
    for i in source_array:
        if i % 2 != 0:
            res.append(sort_a[c])
            c += 1
        else:
            res.append(i)



    return res




print(sort_array([5, 3, 2, 8, 1, 4]), [1, 3, 2, 8, 5, 4],sep='\n')
print()
print(sort_array([5, 3, 1, 8, 0]), [1, 3, 5, 8, 0],sep='\n')
print()
print(sort_array([]), [],sep='\n')