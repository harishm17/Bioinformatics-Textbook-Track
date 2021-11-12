def EulerianCycle(adjlist):
    stack = []
    cycle = []
    stack.append(next(iter(adjlist)))
    while len(stack) != 0:
        u = stack[-1]
        if u not in adjlist or len(adjlist[u]) == 0:
            cycle.append(stack.pop())
        else:
            stack.append(adjlist[u].pop(0))
    cycle.reverse()
    return cycle
  
def DeBruijn2(kmers):
    over = {}
    for i in kmers:
        if i[:-1] not in over:
            over[i[:-1]] = [i[1:]]
        else:
            over[i[:-1]].append(i[1:])
    return over

def k_universal(k):
    init=[]
    for i in range(2**k):
        binary=bin(i)[2:]
        init.append('0'*(k-len(binary))+binary)
    cycle = EulerianCycle(DeBruijn2(init))
    cycle = cycle[:-(k - 1)]
    genome = cycle[0][:-1]
    for i in cycle:
        genome += i[-1]
    return genome
