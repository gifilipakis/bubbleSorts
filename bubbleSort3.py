# bubble sort 3
import re

with open('bubbleSort3.csv', encoding="utf8") as myfile:
    l = myfile.read()
    l = re.split('\n|,',l)
print(l)

troca = True
while j <= len(l) and troca:
    troca = False
    for i in len(l) - 1:
        if l[i] < l[i+1]:
            troca = True
            aux = l[i]
            l[i] = l[i+1]
            l[i+1] = aux
    j += 1