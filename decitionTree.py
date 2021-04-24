import numpy as np
import math as ma
def prob(a):
    return a / dLen

def giniCal(p):
    return 1 - p ** 2 - (1 - p)**2

def entropyCal(p):
    if p == 0 or p == 1:
        print("Error = 0")
        return 0

    a = -1 * p * ( ma.log(p) / ma.log(2) )
    b = (1 - p) * ( ma.log(1 - p) / ma.log(2) )
    print("Error = " + str(a) + " - " + str(b) )
    return a - b

def errorCal(p):
    return 1 - max(p, (1-p))


#yes,true... = 1. else 0
#last attribute = class
dataSet = np.array([[1,1,1,0],[1,1,0,0],[0,0,1,1],[1,0,0,1]])

dLen = np.size(dataSet,0)
dLenX = np.size(dataSet,1)
dProbCount = dataSet.sum(axis = 0)
dProb = prob(dProbCount)

print(dProb)
print("---------------------------")
print("Parents")
print("Error parents = " + str(entropyCal(dProb[dLenX - 1])))
print("---------------------------")

#attritube x,y,z...
for i in range(int(dLenX - 1)):
    print("Attribute " + str(i))
    left = []
    leftProb = int(0)
    right = []
    rightProb = int(0)

    for k in dataSet:

        if k[i] == 0:
            left.append(k) 
        else:
            right.append(k)
    
    pl = int(0)
    for u in left:
        if u[dLenX - 1] == 0:
            pl += 1
    possl = pl / int(len(left))
    eLeft = entropyCal(possl)
    print("E left = " + str(eLeft))
    print()

    pr = int(0)
    for j in right:
        if j[dLenX - 1] == 0:
            pr += 1
    possr = pr / int(len(right))
    eRight = entropyCal(possr)
    print("E right = " + str(eRight))
    print()

    gpl = int(len(left)) / dLen
    gpr = int(len(right)) / dLen

    gain = 1 - (gpl * eLeft) - (gpr * eRight)
    print("gain = " + str(gain))
    print("---------------------------")

