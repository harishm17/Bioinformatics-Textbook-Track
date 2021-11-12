def Overlap(kmers):
    over = {}
    for i in kmers:
        suff = i[1:]
        for j in kmers:
            if suff == j[:-1]:
                if i in over:
                    over[i].append(j)
                else:
                    over[i] = [j]
    return over

k=input()
kmers=[]
while(k):
    kmers.append(k)
    k=input()
over=Overlap(kmers)
for i in over:
    s=''
    for j in over[i]:
        if len(s)==0:
            s=j
        else:
            s=s+','+j
    print(i,'->',s)
