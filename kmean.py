import math
import statistics
import numpy as np

def pointDiff(x,y):
    return math.sqrt( ((x[0]-y[0])**2)+((x[1]-y[1])**2) )

#       A     ,B    ,C    ,D    ,E
pt = [[1,1],[1,0],[0,2],[2,4],[3,5]]
selected = [pt[0],pt[2]]

#pt = [[1,1],[2,0],[0,1],[2,5],[1,5],[3,4]]
#selected = [pt[0],pt[3]]

# k = selected cluster
# Here k = loop count for after first-round-batch
k = 2

textList = []
print("k in round 1")

for i in pt:
    x1 = pointDiff(i,selected[0])
    x2 = pointDiff(i,selected[1])
    cl = int(0)

    if x1 > x2:
        cl = 2
    else:
        cl = 1
    textList.append([x1,x2,cl,i[0],i[1]])

new1 = []
new2 = []


for i in textList:
    if i[2] == 1:
        new1.append([i[3],i[4]])
    else:
        new2.append([i[3],i[4]])

c1Mean = np.mean(new1, axis = 0)
c2Mean = np.mean(new2, axis = 0)

print("list")
print("D1, D2, Belongs, X1, X2")
[ print(i) for i in textList]
# print(textList)

print(f"Cluster 1 pts = {new1}")
print(f"Cluster 1 Mean = {c1Mean}")

print(f"Cluster 2 pts = {new2}")
print(f"Cluster 2 Mean = {c2Mean}")

print("---------------------------------------")

j = int(1)

while (j < k):
    newi = j + 1
    print("k in round " + str(newi))
    textList2 = []

    for i in pt:
        x1 = pointDiff(i,c1Mean)
        x2 = pointDiff(i,c2Mean)
        cl = int(0)

        if x1 > x2:
            cl = 2
        else:
            cl = 1
        textList2.append([x1,x2,cl,i[0],i[1]])

    new1 = []
    new2 = []

    for i in textList2:
        if i[2] == 1:
            new1.append([i[3],i[4]])
        else:
            new2.append([i[3],i[4]])
    
    c1Mean = np.mean(new1, axis = 0)
    c2Mean = np.mean(new2, axis = 0)


    print("D1, D2, Belongs, X1, X2")
    [ print(i) for i in textList2]

    print(f"Cluster 1 pts = {new1}")
    print(f"Cluster 1 Mean = {c1Mean}")

    print(f"Cluster 2 pts = {new2}")
    print(f"Cluster 2 Mean = {c2Mean}")

    j += 1

print("End.")