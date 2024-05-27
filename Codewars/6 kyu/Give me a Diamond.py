def diamond(n):
    if n < 1 or not n & 1:
        return None
    expected = '*' * n + '\n'

    for i in range(n - 2, 0, -2):
        line = ' ' * ((n - i) // 2) + '*' * i + '\n'
        expected = line + expected + line
    return expected


