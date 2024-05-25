
def valid_braces(string):
    res = []
    d = {')': '(', '}': '{', ']': '['}
    for char in string:
        if char in d.values(): res.append(char)
        elif char in d.keys():
            if res == [] or d[char] != res.pop(): return False
        else: continue
    return res==[]










