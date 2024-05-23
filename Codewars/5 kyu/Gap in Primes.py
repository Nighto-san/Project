
def gap(g, m, n):
    def is_prime(number):
        if number < 2:
            return False
        for i in range(2, int(number**0.5) + 1):
            if number % i == 0:
                return False
        return True

    previous_prime = None
    for number in range(m, n + 1):
        if is_prime(number):
            if previous_prime is not None and number - previous_prime == g:
                return [previous_prime, number]
            previous_prime = number

    return None









print(gap(2, 100, 110), [101, 103])
print(gap(4, 100, 110), [103, 107])
print(gap(6, 100, 110), None)