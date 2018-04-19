def create_phone_number(n):
    return "({}) {}-{}".format("".join(str(v) for v in n[:3]), "".join(str(v) for v in n[3:6]), "".join(str(v) for v in n[6:]))