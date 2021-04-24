import numpy as np
import math as ma

def probCal(a):
    return a / dLen

#your dataSet 
#let (+) = 1, (-) = 0 at last attrubutes (two class only and attributes 1 or 0 only)
dataSet = np.array([[0,0,0,1],[1,0,0,0],[1,1,0,0],[1,1,0,0],[1,0,0,1],[1,0,1,1],[1,0,1,0],[1,0,1,0],[1,1,1,1],[1,0,1,1]])
#targeted dataSet
pos = np.array([0,1,0])

dLen = np.size(dataSet,0) # all record count
dxLen = np.size(dataSet,1) # each record y axis

#class (-)
classA = []
#class (+)
classB = []

for i in dataSet:
    if(i[dxLen - 1] == 0):
        classA.append(i)
    else:
        classB.append(i)

classALen = np.size(classA,0)
classBLen = np.size(classB,0)

def classCon(arr):
    attri = []
    for i in range(dxLen - 1):
        attri.append(0)

    for i in arr:

        j = 0
        while(j < int(dxLen - 1)):
            if i[j] == pos[j]:
                attri[j] += 1
            j += 1

    total = int(1)
    for i in attri:
        print(str(i) + "/" + str(classALen) + " * ")
        total *= (i / classALen)

    print(str(classALen) + "/" + str(dLen))
    total *= (classALen / dLen)
    print("= " + str(total))
    print("---------")

classCon(classA)
classCon(classB)