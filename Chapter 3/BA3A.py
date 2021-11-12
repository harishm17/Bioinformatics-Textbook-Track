def Composition(k, Text):
    comp = []
    for i in range(len(Text) - k + 1):
        comp.append(Text[i:i + k])
    return comp

k=int(input())
Text=input()
comp=Composition(k, Text)
for i in comp:
    print(i)
