import re
def search(regex, password):
    return False if re.match(regex, password) == None else True
regex = r"^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)[a-zA-Z\d]{6,}$"
search(regex, 'fjdId5dsaR')