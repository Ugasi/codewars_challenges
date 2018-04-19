def namelist(names):
    if len(names) == 0:
        return ""
    elif len(names) == 1:
        return names[0]["name"]
    elif len(names) == 2:
        return " & ".join(str(v["name"]) for v in names)
    else:
        return " & ".join([", ".join(str(v["name"]) for v in names[:-1]), names[-1]["name"]])

namelist([ {'name': 'Bart'}, {'name': 'Lisa'}, {'name': 'Maggie'} ])
namelist([ {'name': 'Bart'} ])