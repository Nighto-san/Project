def perimeter(n):
    if n == 1: return 1
    if n == 2: return 2
    res = [1,1]
    for i in range(2,n+1):
        res.append(res[i-1] + res[i-2])
    return sum(res)*4


print(perimeter(20))    