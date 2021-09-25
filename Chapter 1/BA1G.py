def HammingDistance(s1, s2):
    return (sum(a != b for a, b in zip(s1, s2)))

s1=input().strip()
s2=input().strip()
print(HammingDistance(s1,s2))