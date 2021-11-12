def DeBruijn2(kmers):
    over = {}
    for i in kmers:
        if i[:-1] not in over:
            over[i[:-1]] = [i[1:]]
        else:
            over[i[:-1]].append(i[1:])
    return over

k = input()
kmers = []
while (k):
    kmers.append(k)
    k = input()
over = DeBruijn2(kmers)
for i in over:
    s = ''
    for j in over[i]:
        if len(s) == 0:
            s = j
        else:
            s = s + ',' + j
    print(i, '->', s)
