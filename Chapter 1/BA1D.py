def PatternMatching(Pattern, Genome):
    pos = []
    for i in range(len(Genome) - len(Pattern) + 1):
        if Genome[i:i + len(Pattern)] == Pattern:
            pos.append(i)
    return pos


Pattern = input().strip()
Genome = input().strip()
print(*PatternMatching(Pattern, Genome))
