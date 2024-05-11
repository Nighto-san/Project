def reverse_seq(n):
    return [i for i in range(1,n+1)][::-1]

def is_uppercase(inp : str):
    return True if all(i.isupper() for i in inp if i.isalpha()) else False



print(reverse_seq(5))
