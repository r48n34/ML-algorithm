import numpy as np
import math as ma

def probCal(a):
    return a / dLen

#your dataSet 
#let (+) = 1, (-) = 0 at last attrubutes (two class only and attributes 1 or 0 only)
dataSet = np.array([[1,0,1,0],[1,2,0,1],[1,1,0,1],[0,1,1,0],[0,0,0,0],[0,2,1,1],[1,1,0,0],[1,2,1,0],[0,2,0,1],[1,1,1,0]])
#targeted dataSet
pos = np.array([1,0,0])

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


def classCon(arr):
    classLen = np.size(arr,0)
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
        print(str(i) + "/" + str(classLen) + " * ")
        total *= (i / classLen)

    print(str(classLen) + "/" + str(dLen))
    total *= (classLen / dLen)
    print("= " + str(total))
    print("---------")

classCon(classA)
classCon(classB)
