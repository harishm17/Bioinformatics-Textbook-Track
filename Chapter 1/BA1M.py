def NumberToPattern(index, k):
    char = ['A', 'C', 'G', 'T']
    Pattern = ''
    while index != 0:
        Pattern = char[index % 4] + Pattern
        index = index // 4
    while len(Pattern) < k:
        Pattern = 'A' + Pattern
    return Pattern

index=int(input())
k=int(input())
print(NumberToPattern(index, k))