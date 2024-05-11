def solution(s):
    res = []
    for indx,value in enumerate(s):
        if value.isupper():
            res.append(' ')
        res.append(value)
    return ''.join(res)

print(solution("helloWorld"), "hello World",sep='\n')
print()
print(solution("camelCase"), "camel Case",sep='\n')
print()
print(solution("breakCamelCase"), "break Camel Case",sep='\n')