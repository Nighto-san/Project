def dig_pow(n, p):
    str_n = str(n)
    total = 0
    for i in range(len(str_n)):  # проходим по каждому индексу в строковом представлении числа
        digit = int(str_n[i])  # извлекаем цифру по текущему индексу и преобразуем ее в число
        total += digit ** (p + i)  # возводим цифру в степень (p + i) и добавляем результат в total
    if total % n == 0:
        return total // n
    else:
        return -1
    return

def dig_pow(n, p):
  summ = 0
  for indx,ciphra in enumerate(str(n)):
     summ += pow(int(ciphra),p+indx)
  return summ/n if summ%n==0 else -1


print(dig_pow(89, 1), 1)
print(dig_pow(92, 1), -1)
print(dig_pow(46288, 3), 51)
print(dig_pow(41, 5), 25)
print(dig_pow(114, 3), 9)
print(dig_pow(8, 3), 64)