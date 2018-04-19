def validBraces(string):
    while "()" in string or "[]" in string or "{}" in string:
        string = string.replace("()", "").replace("[]", "").replace("{}", "")
    return True if len(string) == 0 else False
validBraces( "[(])" )