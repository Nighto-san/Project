def to_camel_case(text):
    r = ""
    flag = False
    for letter in text:
        if letter in "_-":
            flag = True
            continue
        elif flag:
            r += letter.upper()
            flag = False
            continue
        r += letter
    return r



print(to_camel_case("A-B-C"))