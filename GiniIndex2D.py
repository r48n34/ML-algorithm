import numpy as np
import math

def splitINFO(p):
    sumINFO = int(0)
    totalSum = np.sum(p)

    for i in p:
        a = (np.sum(i) / totalSum)
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

    print("p(C1) = " + str(pC1))
    print("p(C2) = " + str(pC2))
    print("Gini = 1 - " + str(pC1) + " - " + str(pC2) + " = " + str(gini))
    e = entropyPt(c1,c2)
    print("Error = 1 - max(" + str(pC1) + "," + str(pC2) + ") = " + str(err))
    print()
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

    print("-------------------------------")
    print("parentGINI = " + str(parentGINI))
    print("* weighted GINI N1 N2 (Children) = " + totalPtPrint + " = " +str(totalPt))
    print()
    split = splitINFO(pt)
    print("splitINFO = " + str(split))
    print("Error GINI N1 N2 = " + str(totalPtErr))
    print() 

    gain = parentGINI - totalPt
    print("Gain = parentGINI - totalPt = " + str(parentGINI) + " - " + str(totalPt) + " = " + str(gain))
    gainRATIO = gain / split
    print("GainRATIO = GainSplit / splitINFO = " + str(gain) + " / " + str(split) + " = " + str(gainRATIO))


#p = np.array([[1,3],[8,0],[1,7]])
p = np.array([[3,3],[0,4]])
print(p)
#p = np.array([[4,5]])
ppt = np.sum(p, axis=0)

totalGain(p, ppt)
