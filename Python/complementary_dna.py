def DNA_strand(dna):
    dna_set = {"A":"T","C":"G","G":"C","T":"A"}
    strand = ""
    for value in dna:
        strand += dna_set[value]
    return strand

DNA_strand("ATTGC")
