def genome_path(kmers):
    genome = kmers[0][0:len(kmers[0]) - 1]
    for i in kmers:
        genome += i[len(i) - 1]
    return genome
  
k=input()
kmers=[]
while(k):
    kmers.append(k)
    k=input()
print(genome_path(kmers))
