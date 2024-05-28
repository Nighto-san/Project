from test import test

def sq_in_rect(lng, wdth):
    if lng == wdth:
        return None
    squares = []
    while lng != wdth:
        if lng > wdth:
            squares.append(wdth)
            lng -= wdth
        else:
            squares.append(lng)
            wdth -= lng
    squares.append(lng)
    return squares


