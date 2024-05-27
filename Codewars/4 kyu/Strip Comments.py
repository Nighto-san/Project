
def strip_comments(string, markers):
    lines = string.split('\n')
    res = []
    for line in lines:
        for mark in markers:
            if mark in line:
               line = line.split(mark)[0].rstrip()
        res.append(line)
    return '\n'.join(res)


print(strip_comments('apples, pears # and bananas\ngrapes\nbananas !apples', ['#', '!']))