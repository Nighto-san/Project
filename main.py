
def is_integer(string):
    if string[0] in '-0123456789':
        for i in range(1,len(string) +1):
            if string[i] not in '0123456789':
                return False
            else: return True


