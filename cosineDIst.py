###
#For the given data, x=(2,3,4,5,1,1,1), y=(2,4,3,5,2,2,2), please calculate the following
#distances;
#(a) Cosine distance
#(b) Correlation distance
#(c) L2 norm distance
###
import numpy as np
import math

x = np.array([2,3,4,5,1,1,1])
y = np.array([2,4,3,5,2,2,2])

#(a) Cosine distance
print("Cosine distance")
sumXY = 0

i = int(0)
stringPt = ""

while (i < int(len(x))):
    stringPt += str(x[i]) + "x" + str(y[i]) + "+"
    sumXY += x[i] * y[i]
    i += 1

print("x.y = ")
print(sumXY)
print("")

qSumx = 0
for k in x:
    qSumx += k**2

qSumx = math.sqrt(qSumx)

print("|| x || = ")
print(qSumx)
print("")

qSumy = 0
for k in y:
    qSumy += k**2
qSumy = math.sqrt(qSumy)
print("|| y || = ")
print(qSumy)
print("")

ans1 = sumXY / (qSumx * qSumy)
print("cos(x,y) = Cosine distance = ")
print(ans1)
print("------------------")

##################
#(b) Correlation distance
print("Correlation distance")

n = int(len(x))

xAvg = (1/n) * sum(x)
print("Avg X = ")
print(xAvg)
print("")

yAvg = (1/n) * sum(y)
print("Avg Y = ")
print(yAvg)
print("")

sxIn = int(0)
for k in x:
    sxIn += (k - xAvg) ** 2

sxFinal = math.sqrt(sxIn * (1/(n-1)))
print("Sx = ")
print(sxFinal)
print("")

syIn = int(0)
for k in y:
    syIn += (k - yAvg) ** 2

syFinal = math.sqrt(syIn * (1/(n-1)))
print("Sy = ")
print(syFinal)
print("")

i = int(0)
sxy = int(0)

while (i < int(len(x))):
    sxy += (x[i] - xAvg) * (y[i] - yAvg)
    i += 1

sxyFinal = sxy * (1/(n-1))
print("Sxy = ")
print(sxyFinal)
print("")

print("Correlation (x,y) = ")
ans2 = sxyFinal / (syFinal * sxFinal)
print(ans2)
print("------------------")

#################
#(c) L2 norm distance

ans3 = int(0)
i = int(0)

while (i < int(len(x))):
   ans3 +=  (x[i] - y[i]) ** 2
   i += 1

ans3 = ans3 ** 0.5
print("L2 norm distance")
print("L2(x,y) = [sigma(x-y)^2]^0.5 = ")
print(ans3)
print("------------------")
