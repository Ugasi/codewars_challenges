def is_merge(s, part1, part2):
    print(s, part1, part2)
    s = list(s)
    part1 = list(part1)
    part2 = list(part2)
    for i in range(len(s)):
        
        print(s, part1, part2)
        if len(part1) != 0:
            if s[0] == part1[0]:
                part1.pop(0)
                s.pop(0)
                continue
        if len(part2) != 0:
            if s[0] == part2[0]:
                part2.pop(0)
                s.pop(0)
                continue
    print(True if len(s) == 0 and len(part1) == 0 and len(part2) == 0 else False)
    return True if len(s) == 0 and len(part1) == 0 and len(part2) == 0 else False

is_merge('Bananas from Bahamas', 'Bahas', 'Bananas from am')