import random

with open('arquivo100.csv', "a") as myfile:
    for i in range(99):
            myfile.write(str(random.randint(1, 100)) + "\n")
    myfile.write(str(random.randint(1, 100)))
myfile.close() 