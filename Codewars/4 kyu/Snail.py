
def snail(arr):
    n = len(arr)
    mas = [[None] * n for i in range(n)]
    r = []
    i = 1
    x = 0
    y = -1
    drow = 0  # -1 0 1
    dcol = 1  # -1 0 1
    while i <= n**2:
        if 0 <= x + drow < n and 0 <= y + dcol < n and mas[x + drow][y + dcol] is None:
            x += drow
            y += dcol
            r.append(arr[x][y])
            mas[x][y] = arr[x][y]
            i += 1
        else:
            if dcol == 1:
                dcol = 0
                drow = 1
            elif drow == 1:
                drow = 0
                dcol = -1
            elif dcol == -1:
                dcol = 0
                drow = -1
            elif drow == -1:
                drow = 0
                dcol = 1

    return r

result = snail([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
expected_result = [1, 2, 3, 6, 9, 8, 7, 4, 5]
print(result, "            ", expected_result)


