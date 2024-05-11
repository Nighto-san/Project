
def expression_matter(a, b, c):
    return max(a*(a+b), a*b*c, a+b*b, (a+b)*c )


print(expression_matter(2, 1, 1), 4)


