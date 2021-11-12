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
  
adjlist = {}
k = input()
while (k):
    adjlist[int(k.strip().split(' -> ')[0])] = list(map(int, k.strip().split(' -> ')[1].split(',')))
    k = input()
path = (EulerianCycle(adjlist))
print(*path, sep='->')
