import math
import statistics
import numpy as np

pt = [[8,7],[3,7],[4,9],[9,6],[8,5],[5,8],[7,3],[8,4],[7,5],[4,5]]

#c1 = pt[9], c2 = pt[4]
#selected = [pt[9],pt[4]]

def kMedoids (selected):
    arr = []
    cost = int(0)
    for i in pt:
        a = abs(i[0] - selected[0][0]) + abs(i[1] - selected[0][1])
        b = abs(i[0] - selected[1][0]) + abs(i[1] - selected[1][1])
        cl = "C1"

        if a > b:
            cl = "C2"
        cost += min(a,b)

        arr.append([i[0],i[1],a,b,cl])

    print(arr)
    print("Cost = ")
    print(cost)

kMedoids ([pt[9],pt[4]])
kMedoids ([pt[9],pt[7]])
kMedoids ([pt[2],pt[4]])