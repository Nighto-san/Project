def wave(people):
    res =[]
    for i in range(len(people)):
        if people[i].isalpha():
            res.append(   people[:i] + people[i:i+1].upper() + people[i+1:]     )
    return res

print(wave("two words"))




