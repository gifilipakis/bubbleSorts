# bubble sort 2
import re

with open('bubbleSort2.csv', encoding="utf8") as myfile:
    l = myfile.read()
    l = re.split('\n|,',l)
print(l)

for j in range(len(l)):
    for i in j + 1:
        if l[i] < l[i-1]:
            aux = l[i]
            l[i] = l[i-1]
            l[i-1] = aux