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


Pattern = input().strip()
d = int(input())
print(*Neighbors(Pattern, d), sep='\n')
