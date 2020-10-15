# bubble sort 1

l = []
for j in range(len(l)):
    for i in range(len(l)-1):
        if l[i] > l[i+1]:
            aux = l[i]
            l[i] = l[i+1]
            l[i+1] = aux