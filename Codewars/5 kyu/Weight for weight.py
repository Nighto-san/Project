def order_weight(strng):
    return ' '.join(sorted([i for i in strng.split()], key=lambda x: (sum(int(digit) for digit in x), x)))

print(order_weight("103 123 4444 99 2000"))