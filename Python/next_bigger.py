def next_bigger(n):
    na = list(str(n))
    for i in range(len(str(n))-1, -1, -1):
        na[i], na[i-1] = na[i-1], na[i]
        if int("".join(na)) > n:
            print(int("".join(na)))
            return int("".join(na))
    return -1

next_bigger(1234567890)