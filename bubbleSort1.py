# bubble sort 1
import re

with open('bubbleSort1.csv', encoding="utf8") as myfile:
    l = myfile.read()
    l = re.split('\n|,',l)
print(l)

for j in range(len(l)):
    for i in range(len(l)-1):
        if l[i] > l[i+1]:
            aux = l[i]
            l[i] = l[i+1]
            l[i+1] = aux
print(l)