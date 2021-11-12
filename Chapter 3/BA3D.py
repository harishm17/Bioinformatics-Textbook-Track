def Composition(k, Text):
    comp = []
    for i in range(len(Text) - k + 1):
        comp.append(Text[i:i + k])
    return comp

def DeBruijn(k, Text):
    over = {}
    kmers = Composition(k, Text)
    for i in kmers:
        if i[:-1] not in over:
            over[i[:-1]] = [i[1:]]
        else:
            over[i[:-1]].append(i[1:])
    return over

k = int(input())
Text = input()
over = DeBruijn(k, Text)
for i in over:
    s = ''
    for j in over[i]:
        if len(s) == 0:
            s = j
        else:
            s = s + ',' + j
    print(i, '->', s)
