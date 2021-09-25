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


def ComputingFrequencies(Text, k):
    FreqArray = [0] * (4 ** k)
    for i in range(len(Text) - k + 1):
        Pattern = Text[i:i + k]
        inx = PatternToNumber(Pattern)
        FreqArray[inx] += 1
    return FreqArray


Text = input().strip()
k = int(input())
print(*ComputingFrequencies(Text, k))
