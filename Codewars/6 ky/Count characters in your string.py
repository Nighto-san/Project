def count(s):
    return {i: s.count(i) for i in s}

print(count('aba'), {'a': 2, 'b': 1})
print(count(''), {})
print(count('aa'), {'a' : 2})
print(count('aabb'), {'b' : 2, 'a' : 2})