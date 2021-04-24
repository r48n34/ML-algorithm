import numpy as np
import math
def pointDiff(x,y):
    return math.sqrt( ((x[0]-y[0])**2)+((x[1]-y[1])**2) )

class Point:
    def __init__(self, point,cluster,minDest,minDestPt):
        self.point = point
        self.cluster = cluster
        self.minDest = minDest
        self.minDestPt = minDestPt
    
    def printAll(self):
        print(str(self.point) + " Cluster " + str(self.cluster) + " MinDest = " + str(self.minDest) + " with " + str(self.minDestPt))

#point
pt = [[2,10],[2,5],[8,4],[5,8],[7,5],[6,4],[1,2],[4,9]]
# threshold
t = 4


maxClass = int(1)
res = []

p = Point(pt[0],0,0,0)
res.append(p)


stPt = pointDiff(pt[1],pt[0])
if stPt > t: 
   pp = Point(pt[1],maxClass, stPt ,pt[0])
   res.append(pp)
   maxClass += 1 
else:
    pp = Point(pt[1],0, stPt, pt[0])
    res.append(pp)


i = int(2)
while i < int(len(pt)):
    minn = int(100000)
    minPol = []

    for k in res:
        dis = pointDiff(pt[i],k.point)

        if dis < minn:
            minn = dis
            minPol = k

    if minn > t:
        pp = Point(pt[i], maxClass, minn, minPol.point)
        res.append(pp)
        maxClass += 1
    else:
        pp = Point(pt[i], minPol.cluster, minn, minPol.point)
        res.append(pp)

    i += 1


for i in range(maxClass):
    for j in res:
        if j.cluster == i:
            j.printAll()
