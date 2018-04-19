def in_array(array1, array2):
    return sorted(list(set(s for s in array1 for s2 in array2 if s in s2)))

a1 = ["live", "arp", "strong"] 
a2 = ["lively", "alive", "harp", "sharp", "armstrong"]
in_array(a1, a2)