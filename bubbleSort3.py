# bubble sort 3
import os
import datetime
import re
import psutil

start_time = datetime.datetime.now()

pid = os.getpid()
py = psutil.Process(pid)

with open('bubbleSort3.csv', encoding="utf8") as myfile:
    l = myfile.read()
    l = re.split('\n|,',l)
print(l)

qtrocas = 0
qcomparacoes = 0

j = 1
troca = True
while j <= len(l) and troca:
    troca = False
    for i in len(l) - 1:
        qcomparacoes += 1
        if l[i] < l[i+1]:
            qtrocas += 1
            troca = True
            aux = l[i]
            l[i] = l[i+1]
            l[i+1] = aux
    j += 1


end_time = datetime.datetime.now()
time_diff = (end_time - start_time)
execution_time = time_diff.total_seconds() * 1000

print('Quantidade de comparações'+': '+str(qcomparacoes))
print('Quantidade de trocas'+': '+str(qtrocas))
print('Tempo de execução'+': '+str(execution_time))
print('Consumo de CPU'+': '+str(py.cpu_times()[0]))
print('Consumo de memória'+': '+str(py.memory_info()[0]))