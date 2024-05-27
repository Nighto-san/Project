def next_bigger(n):
    s = list(str(n))
    for i in range(len(s) - 2, -1, -1):
        if s[i] < s[i + 1]:
            break
    else:
        return -1

    for j in range(len(s) - 1, i, -1):
        if s[j] > s[i]:
            break
    s[i], s[j] = s[j], s[i]
    s[i + 1:] = reversed(s[i + 1:])
    return int("".join(s))


