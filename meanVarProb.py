import math
import numpy as np
import statistics

def normaldis(target, mean, var):
    left = 1 / ( math.sqrt( (2 * math.pi * var) ) )
    rtop = ((target - mean) ** 2) / (2 * var)
    right = np.exp(rtop)
    return left * right

db = np.array([125,100,70,120,95,60,220,85,75,90])
dbClass = np.array([0,0,0,0,1,0,0,1,0,1]) #0 = no , 1 = yes
tar = 120 # your target value

arrNo = np.array([])
arrYes = np.array([])

for i in range(len(dbClass)):
    if dbClass[i] == 0:
        arrNo = np.append(arrNo, db[i])
    else:
        arrYes = np.append(arrYes, db[i])


meanNo = np.mean(arrNo, axis=0)
varNo = statistics.variance(arrNo)

meanYes = np.mean(arrYes, axis=0)
varYes = statistics.variance(arrYes)

print("mean No =", meanNo, "variance of No =" , varNo)
print("mean Yes =", meanYes, "variance of Yes =" , varYes)
print()
print("P(No) = ", normaldis(tar, meanNo, varNo))
print("P(Yes) = ", normaldis(tar, meanYes, varYes))




