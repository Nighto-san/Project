def expanded_form(num):
    s_num = str(num)
    box = []
    for indx,ciphra in enumerate(s_num):
        if ciphra != '0':
            box.append(ciphra + '0'* len(s_num[indx+1:]))
    return ' + '.join(box)



print(expanded_form(12), '10 + 2', sep='\n')
print(expanded_form(42), '40 + 2', sep='\n')
print(expanded_form(70304), '70000 + 300 + 4', sep='\n')