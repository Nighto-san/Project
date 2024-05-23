def make_readable(seconds):
    h = seconds//3600
    m = (seconds % 3600) // 60
    s = (seconds % 3600) % 60

    return f"{str(h).zfill(2)}:{str(m).zfill(2)}:{str(s).zfill(2)}"


print(make_readable(3600),"       " ,"01:00:00")
print(make_readable(86399), "       " , "23:59:59")