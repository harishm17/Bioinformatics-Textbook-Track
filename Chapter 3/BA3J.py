def EulerianPath(adjlist):
    degree = {}
    for i in adjlist:
        if i not in degree:
            degree[i] = 0
        degree[i] -= len(adjlist[i])
        for j in adjlist[i]:
            if j not in degree:
                degree[j] = 0
            degree[j] += 1
    for i in degree:
        if degree[i] == -1:
            start = i
        elif degree[i] == 1:
            end = i
    adjlist[start].append(end)
    stack = []
    cycle = []
    stack.append(start)
    while len(stack) != 0:
        u = stack[-1]
        if u not in adjlist or len(adjlist[u]) == 0:
            cycle.append(stack.pop())
        else:
            stack.append(adjlist[u].pop(0))
    cycle.reverse()
    # print(cycle)
    for i in range(len(cycle)):
        if cycle[i] == start and cycle[(i + 1) % len(cycle)] == end:
            cycle.pop((i + 1) % len(cycle))
            break
    return cycle

def DeBruijn3(read_pairs):
    over = {}
    for pair in read_pairs:
        pair = pair.split('|')
        pref = (pair[0][:-1], pair[1][:-1])
        suff = (pair[0][1:], pair[1][1:])
        if pref in over:
            over[pref].append(suff)
        else:
            over[pref] = [suff]
    return over

def StringReconstructionFromReadPairs(d, read_pairs):
    db = DeBruijn3(read_pairs)
    path = EulerianPath(db)
    text = path[0][0]
    for pair in path[1: d + 2]:
        text += pair[0][-1]

    text += path[0][1]
    for pair in path[1:]:
        text += pair[1][-1]
    return text

k,d=map(int,input().split())
kmer=input()
kmers=[]
while(kmer):
    kmers.append(kmer)
    kmer=input()
over=DeBruijn3(kmers)
# print(over)
path=EulerianPath(over)
# print(path)
print(StringReconstructionFromReadPairs(d,kmers))
