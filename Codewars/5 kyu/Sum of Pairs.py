

def sum_pairs(ints, s):
    res = {}
    for digit in ints:
        if digit in res:
            return [res[digit], digit]
        res[s-digit] = digit

    return None









print(sum_pairs([1, 4, 8, 7, 3, 15], 8), [1, 7],)
print(sum_pairs([1, -2, 3, 0, -6, 1], -6), [0, -6],)
print(sum_pairs([20, -13, 40], -7), None)
print(sum_pairs([1, 2, 3, 4, 1, 0], 2), [1, 1],)
print(sum_pairs([10, 5, 2, 3, 7, 5], 10), [3, 7])