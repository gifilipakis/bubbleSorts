import random

for i in range(99999):
    with open('bubbleSort3.csv', "a") as myfile:
        myfile.write(str(random.randint(1, 100000)) + "\n")
myfile.write(str(random.randint(1, 100000)))
myfile.close() 