def camel_case(s):
    return ''.join(i.capitalize() for i in s.split())





print(camel_case('camel case word'))



# "hello case" --> "HelloCase"
# "camel case word" --> "CamelCaseWord"