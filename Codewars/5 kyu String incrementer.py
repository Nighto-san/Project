def increment_string(strng):
    if strng and strng[-1].isdigit():
        number = ''
        for i in strng[::-1]:
            if i.isdigit():
                number += i
            else:
                break
        number = number[::-1]
        strng = strng[:len(strng)-len(number)]
        number = str(int(number) + 1).zfill(len(number))
        return strng + number
    else:
        return strng + '1'



print(increment_string("foo")," >>> ", "foo1")
print(increment_string("foobar001")," >>> ", "foobar002")
print(increment_string("foobar1"), " >>> ","foobar2")
print(increment_string("foobar00")," >>> ", "foobar01")
print(increment_string("foobar99"), " >>> ","foobar100")
print(increment_string("foobar099"), " >>> ","foobar100")
print(increment_string("fo99obar99"), " >>>> ","fo99obar100")
print(increment_string("")," >>>> ", "1")