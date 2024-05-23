def sum_dig_pow(a, b):
    results = []
    for number in range(a, b + 1):
        str_number = str(number)
        summ = 0
        for i in range(len(str_number)):
            summ += int(str_number[i]) ** (i + 1)
        if summ == number:
            results.append(number)

    return results


#print(sum_dig_pow(1, 10), [1, 2, 3, 4, 5, 6, 7, 8, 9], sep='\n')
print(sum_dig_pow(1, 100), [1, 2, 3, 4, 5, 6, 7, 8, 9, 89], sep='\n')
print(sum_dig_pow(10, 89), [89], sep='\n')
print(sum_dig_pow(10, 100), [89], sep='\n')
print(sum_dig_pow(90, 100), [], sep='\n')
print(sum_dig_pow(89, 135), [89, 135], sep='\n')