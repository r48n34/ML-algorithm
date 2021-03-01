import math
import numpy as np

def pointDiff(x,y):
    return math.sqrt( ((x[0]-y[0])**2)+((x[1]-y[1])**2) )

def weight (o1,c1,c2):
    top = pointDiff(o1,c2)**2
    down = pointDiff(o1,c2)**2 + pointDiff(o1,c1)**2
    return top / down

#        a      b     c     d       e       f
arr = [[3,3],[4,10],[9,6],[14,8],[18,11],[21,7]]
time = int(0)

outA = arr[0]
outB = arr[1]

while time < 3:
    print("--------------" + str(time) + " times loop -----------------")
    a = outA
    b = outB
    #let c1 = a, c2 = b

    i = int(0)
    m = []

    while i < int(len(arr)):
        big = weight (arr[i],a,b)
        m.append([big, 1-big])
        i += 1

    for i in m: 
        print(i)

    mt = np.transpose(m)
    print(mt)

    i = int(0)

    #topleft,downleft,topright,downright
    c1 = [0,0,0,0]
    c2 = [0,0,0,0]

    while i < int(len(arr)):
        c1[0] += (mt[0][i]**2) * arr[i][0]
        c1[1] += mt[0][i]**2

        c1[2] += (mt[0][i]**2) * arr[i][1]
        c1[3] += mt[0][i]**2

        ##############

        c2[0] += (mt[1][i]**2) * arr[i][0]
        c2[1] += mt[1][i]**2

        c2[2] += (mt[1][i]**2) * arr[i][1]
        c2[3] += mt[1][i]**2

        i += 1

    c1x = c1[0] / c1[1]
    c1y = c1[2] / c1[3]

    c2x = c2[0] / c2[1]
    c2y = c2[2] / c2[3]

    print("c1 = (" + str(c1x) + "," + str(c1y) + ")")
    print("c2 = (" + str(c2x) + "," + str(c2y) + ")")

    outA = [c1x,c1y]
    outB = [c2x,c2y]
    print("-----------------------------")
    time += 1
