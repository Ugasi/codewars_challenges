def likes(names):
    if len(names) > 3:
        return "{} and {} others like this".format(", ".join(n for n in names[:2]), len(names)-2)
    elif len(names) > 1:
        return "{} and {} like this".format(", ".join(n for n in names[:-1]), names[-1])
    elif len(names) == 1:
        return "{} likes this".format(names[0])
    else:
        return "no one likes this"
likes(['Alex'])
