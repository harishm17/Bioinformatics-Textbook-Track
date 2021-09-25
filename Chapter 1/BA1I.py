def HammingDistance(s1, s2):
    return (sum(a != b for a, b in zip(s1, s2)))


def Neighbors(Pattern, d):
    Neighborhood = []
    if d == 0:
        Neighborhood.append(Pattern)
    else:
        if len(Pattern) == 1:
            Neighborhood.extend(['A', 'T', 'G', 'C'])
        else:
            Suffix = Pattern[1:]
            SuffixNeighbors = Neighbors(Suffix, d)
            for x in SuffixNeighbors:
                if HammingDistance(x, Suffix) < d:
                    Neighborhood.extend(['A' + x, 'T' + x, 'G' + x, 'C' + x])
                else:
                    Neighborhood.append(Pattern[0] + x)
    return list(set(Neighborhood))


def FrequentWordsWithMismatches(Text, k, d):
    Patterns = []
    freqMap = {}
    n = len(Text)
    for i in range(n - k + 1):
        Pattern = Text[i:i + k]
        Neighborhood = Neighbors(Pattern, d)
        for x in Neighborhood:
            if x in freqMap:
                freqMap[x] += 1
            else:
                freqMap[x] = 1
    maxi = max(freqMap.values())
    for x in freqMap:
        if freqMap[x] == maxi:
            Patterns.append(x)
    return Patterns

Text=input().strip()
k,d = map(int,input().split())
print(*FrequentWordsWithMismatches(Text, k, d))