def ReverseComplement(Pattern):
    comp = {'T': 'A', 'A': 'T', 'G': 'C', 'C': 'G'}
    Pattern_rc = ''
    for x in Pattern:
        Pattern_rc = comp[x] + Pattern_rc
    return Pattern_rc


Pattern = input().strip()
print(ReverseComplement(Pattern))
