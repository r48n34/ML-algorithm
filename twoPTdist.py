import math
def pointDiff(x,y):
    return math.sqrt( ((x[0]-y[0])**2)+((x[1]-y[1])**2) )

one = [0,0]
two = [1,1]

print(pointDiff(one,two)) 

