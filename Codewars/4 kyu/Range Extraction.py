def solution(a):
    if len(a)==0: return ""
    res = []
    start = a[0]
    end = a[0]
    for i in range(1,len(a)):
        if a[i] == end + 1:
            end = a[i]
        else:
            if end - start >= 2:
                res.append(f"{start}-{end}")
            else:
                res.extend(str(j) for j in range(start, end + 1))
            start = a[i]
            end = a[i]
    if end - start >= 2:
        res.append(f"{start}-{end}")
    else:
        res.extend(str(j) for j in range(start, end + 1))

    return ",".join(res)

print(solution([3,4,5,7,8,9,10,11,14,15,17,18,19,20]))
#3-5,7-11,14,15,17-20')


