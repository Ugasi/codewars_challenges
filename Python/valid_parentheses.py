import re
def valid_parentheses(string):
    string = re.sub("[^()]", "", string)
    while "()" in string:
        string = string.replace("()", "")
    return True if len(string) == 0 else False
valid_parentheses("(((()))))")