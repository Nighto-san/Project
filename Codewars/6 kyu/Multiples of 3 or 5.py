def solution(number):
    if number < 0: return 0
    res = 0
    for i in range(1, number):
        if i % 3 == 0 or i % 5 == 0:
            res += i
    return res




print(solution(10))
