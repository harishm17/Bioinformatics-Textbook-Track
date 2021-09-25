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

def FindClumps(Text, k, L, t):
    Patterns = []
    for i in range(len(Text) - L + 1):
        Window = Text[i:i + L]
        freqMap = FrequencyTable(Window, k)
        for key in freqMap:
            if freqMap[key] == t:
                Patterns.append(key)
    return list(set(Patterns))

Text=input().strip()
k,L,t=map(int,input().split())
print(*FindClumps(Text, k, L, t))