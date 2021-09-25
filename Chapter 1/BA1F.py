def Skew(Genome):
    skew = [0]
    for i in range(len(Genome)):
        if Genome[i] == 'C':
            skew.append(skew[-1] - 1)
        elif Genome[i] == 'G':
            skew.append(skew[-1] + 1)
        else:
            skew.append(skew[-1])
    return skew


def MinSkew(Genome):
    minSkew = []
    skew = Skew(Genome)
    mini = min(skew)
    for i in range(len(skew)):
        if skew[i] == mini:
            minSkew.append(i)
    return minSkew


Genome = input().strip()
print(*MinSkew(Genome))
