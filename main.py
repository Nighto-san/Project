def series_sum(n):
    res = 0
    for i in range(n):
        res += 1 / (1+i*3)
    return '{:.2f}'.format(res)


print(series_sum(1), "1.00")
print(series_sum(2), "1.25")
print(series_sum(3), "1.39")