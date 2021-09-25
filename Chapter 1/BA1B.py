def FrequencyTable(Text, k):
    freqMap = {}
    n = len(Text)
    for i in range(n - k + 1):
        kmer = Text[i:i + k]
        if kmer in freqMap:
            freqMap[kmer] += 1
        else:
            freqMap[kmer] = 1
    return freqMap


def FrequentWords(Text, k):
    freqMap = FrequencyTable(Text, k)
    maxi = max(freqMap.values())
    freqPatterns = []
    for key in freqMap:
        if freqMap[key] == maxi:
            freqPatterns.append(key)
    return freqPatterns


Text = input().strip()
k = int(input().strip())
print(*FrequentWords(Text, k))
