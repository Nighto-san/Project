
def get_middle(s):
    return s[len(s)//2 -1] + s[len(s)//2] if len(s) % 2 == 0 else s[len(s)//2]


print(get_middle("test"), "es")
print(get_middle("testing"), "t")
print(get_middle("middle"), "dd")
print(get_middle("A"), "A")
print(get_middle("of"), "of")








