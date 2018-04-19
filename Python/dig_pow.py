def dig_pow(n, p):
    total = 0
    for i, v in enumerate(str(n)):
        total += int(v)**(p+i)
    return total / n if total % n == 0 else -1
dig_pow(46288, 3)