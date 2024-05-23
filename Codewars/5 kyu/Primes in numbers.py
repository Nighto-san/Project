
def prime_factors(n):
    facts = []
    for i in range(2, int(n**0.5) + 1):
        while n % i == 0:
            facts.append(i)
            n = n//i
    if n > 1:
        facts.append(n)
    res = {}
    for i in facts:
        res.setdefault(i,0)
        res[i] += 1
    final = ''
    for k,v in res.items():
        if v < 2:
            final +=f'({k})'
        else:
            final +=f'({k}**{v})'

    return final





print(prime_factors(7775460), "(2**2)(3**3)(5)(7)(11**2)(17)")
