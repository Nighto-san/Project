import re

    pattern = r"^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)[A-Za-z\d]{6,}$"

password = "123abcABC"
match = re.match(pattern, password)

print(match)


