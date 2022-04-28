import math
import numpy as np

def pointDiff(x,y):
    return math.sqrt( ((x[0]-y[0])**2)+((x[1]-y[1])**2) )

def calculateDiff(ptArray, c1Mean, c2Mean):
    arr = []

    for i in ptArray:
        x1 = pointDiff(i,c1Mean)
        x2 = pointDiff(i,c2Mean)
        cl = int(0)

        if x1 > x2:
            cl = 2
        else:
            cl = 1
        arr.append([x1,x2,cl,i[0],i[1]])
    
    return arr

def classificateCluster(arr):
    new1 = []
    new2 = []

    for i in arr:
        if i[2] == 1:
            new1.append([i[3],i[4]])
        else:
            new2.append([i[3],i[4]])
    
    return (new1, new2)

def kMeans(pt, selected, round = 2):

    c1Mean = selected[0]
    c2Mean = selected[1]

    for j in range(round):
 
        print("k in round " + str(int(j + 1)))
        textList = calculateDiff(pt, c1Mean, c2Mean)
        new1, new2 = classificateCluster(textList)

        c1Mean = np.mean(new1, axis = 0)
        c2Mean = np.mean(new2, axis = 0)

        print("D1, D2, Belongs, X1, X2")
        [ print(i) for i in textList]

        print(f"Cluster 1 pts = {new1} \nCluster 1 Mean = {c1Mean}")
        print(f"Cluster 2 pts = {new2} \nCluster 2 Mean = {c2Mean}")
        print("---------------------------------------")

    print("End.")

if __name__ == "__main__":
    #       A     ,B    ,C    ,D    ,E
    pt = [[1,1],[1,0],[0,2],[2,4],[3,5]]
    selected = [pt[0],pt[2]]

    #pt = [[1,1],[2,0],[0,1],[2,5],[1,5],[3,4]]
    #selected = [pt[0],pt[3]]

    kMeans(pt, selected, 2)