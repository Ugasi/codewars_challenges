import collections
def is_hollow(x):
    first_zero = None
    last_zero = None
    counts = collections.Counter(x)
    if counts.get(0) < 3:
        return False
    else:
        for i, v in enumerate(x):
            if v == 0:
                if first_zero is None:
                    first_zero = i
                if last_zero is None or last_zero < i:
                    last_zero = i
        for i in range(first_zero, last_zero):
            if x[i] != 0:
                return False
        return (first_zero == len(x)-last_zero-1 and first_zero != 0 and last_zero != len(x)) or counts.get(0) == len(x)

is_hollow([-1, 0, 100, 0, 0, 0, -7, 0, -99])
