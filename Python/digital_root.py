def digital_root(n):
    value = sum(int(val) for val in str(n))
    while value > 9:
        value = sum(int(val) for val in str(value))
    return value

digital_root(24569)