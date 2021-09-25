def PatternToNumber(Pattern):
    temp = 1
    num = {'A': 0, 'C': 1, 'G': 2, 'T': 3}
    i = len(Pattern) - 1
    inx = 0
    while i != -1:
        inx += (temp * num[Pattern[i]])
        temp *= 4
        i -= 1
    return inx


Pattern = input().strip()
print(PatternToNumber(Pattern))
