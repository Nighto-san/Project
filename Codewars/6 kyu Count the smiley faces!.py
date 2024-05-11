def count_smileys(arr):
    s = 0
    for smile in arr:
        if smile[0] in ':;' and smile[-1] in ')D':
            if len(smile) == 3:
                if smile[1] in '-~':
                    s +=1
            else: s +=1
    return s




print(count_smileys([]), 0)
print(count_smileys([':D' ,':~)' ,';~D' ,':)']), 4)
print(count_smileys([':)' ,':(' ,':D' ,':O' ,':;']), 2)
print(count_smileys([';]', ':[', ';*', ':$', ';-D']), 1)