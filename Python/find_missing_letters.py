def find_missing_letter(chars):
    return chr(sum(i for i in range(ord(chars[0]), ord(chars[-1])+1))-sum(ord(x) for x in chars))

find_missing_letter(['a','b','c','d','f'])