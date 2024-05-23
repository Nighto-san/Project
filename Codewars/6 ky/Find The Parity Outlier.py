def find_outlier(integers):
    a = sum(1 if i % 2 == 0 else -1 for i in integers[:3])
    if a > 0:
        for i in integers:
            if i % 2 != 0:
                return i
    else:
        for i in integers:
            if i % 2 == 0:
                return i


print(find_outlier([160, 3, 1719, 19, 11, 13, -21]), 160)