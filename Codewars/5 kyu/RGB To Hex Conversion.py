def rgb(r, g, b):
    def tohex(x):
        if x<0: return "00"
        elif x> 255: return "FF"
        return hex(x)[2:].zfill(2)
    return f"{tohex(r)+tohex(g)+tohex(b)}".upper()


print(rgb(254, 253, 252))