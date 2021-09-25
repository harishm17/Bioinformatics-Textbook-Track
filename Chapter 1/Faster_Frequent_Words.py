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


def NumberToPattern(index, k):
    char = ['A', 'C', 'G', 'T']
    Pattern = ''
    while index != 0:
        Pattern = char[index % 4] + Pattern
        index = index // 4
    while len(Pattern) < k:
        Pattern = 'A' + Pattern
    return Pattern


def ComputingFrequencies(Text, k):
    FreqArray = [0] * (4 ** k)
    for i in range(len(Text) - k + 1):
        Pattern = Text[i:i + k]
        inx = PatternToNumber(Pattern)
        FreqArray[inx] += 1
    return FreqArray


def FasterFrequentWords(Text, k):
    FrequentPatterns = []
    FreqArray = ComputingFrequencies(Text, k)
    maxi = max(FreqArray)
    for i in range(4 ** k):
        if FreqArray[i] == maxi:
            Pattern = NumberToPattern(i, k)
            FrequentPatterns.append(Pattern)
    return FrequentPatterns

Text=input().strip()
k=int(input())