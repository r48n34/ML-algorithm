import math
def pointDiff(x,y):
    return math.sqrt( ((x[0]-y[0])**2)+((x[1]-y[1])**2) )

arr = [[0,0],[1,0],[1,1],[2,2],[3,1],[3,0],[0,1],[3,2],[6,3]]
e = 1
minPts = 3

i = int(0)
k = int(0)
finaltext = []
finalPt = []

while (i < int(len(arr))):
    tempText = []
    tempPt = []
    k = int(0)

    while (k < int(len(arr))):
        if pointDiff(arr[i],arr[k]) <= e:
            text = "x" + str(k)
            tempText.append(text)
            tempPt.append(arr[k])
        k += 1

    finaltext.append(tempText)
    finalPt.append(tempPt)

    i += 1

print("pt =  care x start from 0!!")
for x in finaltext:
    print(x)

print("pt numbers = ")
for x in finalPt:
    print(x)
print("--------")


print("Core point:")
for x in finalPt:
    if int(len(x)) >= minPts:
        print(x)

# given a point p, p is said to be a border point if it is not a core point but
# N(p) contains at least one core point.

#Border Points:
#{x4, x6}

#Noise Points:
#{x9}
