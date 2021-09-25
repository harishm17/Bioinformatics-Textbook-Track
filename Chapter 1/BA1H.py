def HammingDistance(s1, s2):
    return (sum(a != b for a, b in zip(s1, s2)))


def ApproximatePatternMatching(Pattern, Text, d):
    pos = []
    for i in range(len(Text) - len(Pattern) + 1):
        if HammingDistance(Text[i:i + len(Pattern)], Pattern) <= d:
            pos.append(i)
    return pos

Pattern=input().strip()
Text=input().strip()
d=int(input())
print(*ApproximatePatternMatching(Pattern, Text, d))