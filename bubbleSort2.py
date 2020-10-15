# bubble sort 2

l = []
for j in range(len(l)):
    for i in j + 1:
        if l[i] < l[i-1]:
            aux = l[i]
            l[i] = l[i-1]
            l[i-1] = aux