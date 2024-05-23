def solution(s):
    res = []
    for indx, value in enumerate(s):
        print("Индекс:", indx)
        print("Значение:", value)
        if value.isupper():
            print("Значение является заглавной буквой")
            res.append(' ')
        res.append(value)
        print("Текущий результат:", res)
        print("---")
    return ''.join(res)

print(solution("helloWorld"), "hello World", sep='n')
print()
print(solution("camelCase"), "camel Case", sep='n')
print()
print(solution("breakCamelCase"), "break Camel Case", sep='n')