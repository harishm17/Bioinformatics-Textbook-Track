def EulerianPath(adjlist):
    degree = {}
    for i in adjlist:
        if i not in degree:
            degree[i]=0
        degree[i] -= len(adjlist[i])
        for j in adjlist[i]:
            if j not in degree:
                degree[j]=0
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
  
adjlist = {}
k = input()
while (k):
    adjlist[int(k.strip().split(' -> ')[0])] = list(map(int, k.strip().split(' -> ')[1].split(',')))
    k = input()
path = (EulerianPath(adjlist))
print(*path, sep='->')
