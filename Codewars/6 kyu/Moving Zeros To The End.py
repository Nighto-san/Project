def move_zeros(lst):
    a = lst.count(0)
    return [i for i in lst if i != 0] + [0]*a

print(move_zeros([9, 0, 0, 9, 1, 2, 0, 1, 0, 1, 0, 3, 0, 1, 9, 0, 0, 0, 0, 9]))