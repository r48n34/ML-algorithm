import numpy as np
import math

def splitINFO(p):
    sumINFO = int(0)
    totalSum = np.sum(p)

    for i in p:
        a = (np.sum(i) / totalSum)
        if a != 0:
            sumINFO += -1 * a * (math.log(a) / math.log(2) )
    
    return sumINFO

def entropyPt(c1,c2):
    total = c1 + c2

    pC1 = 0
    pC2 = 0

    if c1 != 0:
        pC1 = c1 / total

    if c2 != 0:
        pC2 = c2 / total
      
    e1 = 0
    e2 = 0

    if pC1 != 0:
        e1 = -1 * (pC1) * (math.log(pC1) / math.log(2) )

    if pC2 != 0: 
        e2 = -1 * (pC2) * (math.log(pC2) / math.log(2) )

    entropy = e1 + e2

    print("Entropy = -" + str(pC1) + "log2(" + str(pC1) + ") - " + str(pC2) + "log2(" + str(pC2) +") = " + str(entropy))

    return entropy

def GINIIndex(c1,c2):
    total = c1 + c2

    pC1 = 0
    pC2 = 0

    if c1 != 0:
        pC1 = c1 / total

    if c2 != 0:
        pC2 = c2 / total

    gini = 1 - (pC1**2) - (pC2**2)
    err = 1 - max(pC1,pC2)

    #print("p(C1) = " + str(pC1))
    #print("p(C2) = " + str(pC2))
    #print("Gini = 1 - " + str(pC1) + " - " + str(pC2) + " = " + str(gini))
    e = entropyPt(c1,c2)
    #print("Error = 1 - max(" + str(pC1) + "," + str(pC2) + ") = " + str(err))
    #print()
    return [gini,err]

def totalGain(pt, parentPt):
    totalPt = int(0)
    totalPtPrint = str("")
    totalPtErr = int(0)
    ptSum = np.sum(pt)

    for i in pt:
        a = GINIIndex(i[0],i[1])
        totalPt += a[0] * (np.sum(i) / ptSum)
        totalPtPrint += str(a[0]) + " * " + str(np.sum(i)) + "/" + str(ptSum) + " + "
        totalPtErr += a[1] * (np.sum(i) / ptSum)

    print("Parent: ")
    b = GINIIndex(parentPt[0],parentPt[1])
    parentGINI = b[0]

    print()
    print("parentGINI = " + str(parentGINI))
    print("* weighted GINI N1 N2 (Children) = " + totalPtPrint + " = " +str(totalPt))
    print()
    split = splitINFO(pt)
    print("splitINFO = " + str(split))
    print("Error GINI N1 N2 = " + str(totalPtErr))
    gain = parentGINI - totalPt
    print("Gain = parentGINI - totalPt = " + str(parentGINI) + " - " + str(totalPt) + " = " + str(gain))
    gainRATIO = gain / split
    print("GainRATIO = GainSplit / splitINFO = " + str(gain) + " / " + str(split) + " = " + str(gainRATIO))
    print("-------------------------------")

def yesNoFit(dataArr, pos):
    temp = np.array([[0,0],[0,0]])

    for i in dataArr:
        if i[0] > int(pos):
            if i[1] == 1:
                temp[0][1] += 1
            else:
                temp[1][1] += 1
        else:
            if i[1] == 1:
                temp[0][0] += 1
            else:
                temp[1][0] += 1
    
    return temp


# 0 = no, 1 = yes, offset is the tail and head Split Positions offset
#dataSet = np.array([[125,0],[100,0],[70,0],[120,0],[95,1],[60,0],[220,0],[85,1],[75,0],[90,1]])
#htOffset = 10

dataSet = np.array([[1,1],[3,0],[4,1],[4,1],[5,0],[6,0],[7,1],[7,0],[8,0]])
htOffset = 1

valuesSet = set([])
for i in dataSet:
    valuesSet.add(i[0])

sortedValues = []

for i in valuesSet:
    sortedValues.append(i)
sortedValues.sort()

splitPositions = []
splitPositions.append(sortedValues[0] - htOffset)
i = int(0)

while i < int(len(sortedValues) - 1):
    temp = int( (sortedValues[i] + sortedValues[i+1]) / 2 )
    splitPositions.append(temp)
    i += 1

splitPositions.append(sortedValues[i] + htOffset)

print(sortedValues)
print(splitPositions)
for i in splitPositions:
    print(str(i) + ":")
    arr = yesNoFit(dataSet, i)
    print(arr)
    print()
    arr[0][1] , arr[1][0] = arr[1][0], arr[0][1] 
    pptSum = np.sum(arr, axis=0)

    totalGain(arr, pptSum)
