def PatternCount(Text, Pattern):
    cnt = 0
    for i in range(len(Text) - len(Pattern) + 1):
        if Text[i:i + len(Pattern)] == Pattern:
            cnt += 1
    return cnt


Text = input().strip()
Pattern = input().strip()
print(PatternCount(Text, Pattern))
