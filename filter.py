# Assume all filter are in 3x3
import numpy as np
import statistics


def zeroPaddArr(arr):
    return np.pad(arr, 1 , mode='constant', constant_values=0)

def replicatePaddArr(arr):
    return np.pad(arr, 1 , mode='edge')

def getCurrentArr(img, i, k):
    return [
        img[i - 1][k - 1], img[i][k - 1] , img[i + 1][k - 1] ,
        img[i - 1][k], img[i][k], img[i + 1][k],
        img[i - 1][k + 1], img[i][k + 1], img[i + 1][k + 1] 
    ]

def paddingArrayApply(img, mode):
    if mode == "zero":
        return zeroPaddArr(img)
    elif mode == "repl":
        return replicatePaddArr(img)
    
    return img


def meanFilter(img, mode):
    img = paddingArrayApply(img, mode)

    newImg = []

    for i in range(1, len(img) - 1):
        tempArr = []
        for k in range(1, len(img[i]) - 1):
            currArr = getCurrentArr(img, i, k)
            tempArr.append( float ( sum(currArr) / 9) )  
        newImg.append(tempArr)

    return newImg

def geometricMeanFilter(img, mode):

    img = paddingArrayApply(img, mode)

    newImg = []

    for i in range(1, len(img) - 1):
        tempArr = []

        for k in range(1, len(img[i]) - 1):
            currArr = getCurrentArr(img, i, k)
            finalNum = np.float64( 1 )
            for num in currArr:
                finalNum *= num
            tempArr.append( float ( finalNum ** (1/9) ) ) 

        newImg.append(tempArr)

    return newImg

def harmonicMeanFilter(img, mode):

    img = paddingArrayApply(img, mode)

    newImg = []

    for i in range(1, len(img) - 1):
        tempArr = []

        for k in range(1, len(img[i]) - 1):
            currArr = getCurrentArr(img, i, k)
            finalNum = np.float64( 0 )

            for num in currArr:
                finalNum += (1 / num)

            tempArr.append( float ( 9 / finalNum ) ) 

        newImg.append(tempArr)

    return newImg

def midPointFilter(img, mode):

    img = paddingArrayApply(img, mode)

    newImg = []

    for i in range(1, len(img) - 1):
        tempArr = []
        for k in range(1, len(img[i]) - 1):
            currArr = getCurrentArr(img, i, k)
            tempArr.append( float( 0.5 * (min(currArr) + max(currArr) )) )  
        newImg.append(tempArr)

    return newImg

def minFilter(img, mode):

    img = paddingArrayApply(img, mode)

    newImg = []

    for i in range(1, len(img) - 1):
        tempArr = []
        for k in range(1, len(img[i]) - 1):
            currArr = getCurrentArr(img, i, k)
            tempArr.append( min(currArr) )  
        newImg.append(tempArr)

    return newImg

def maxFilter(img, mode):

    img = paddingArrayApply(img, mode)

    newImg = []

    for i in range(1, len(img) - 1):
        tempArr = []
        for k in range(1, len(img[i]) - 1):
            currArr = getCurrentArr(img, i, k)
            tempArr.append( max(currArr) )  
        newImg.append(tempArr)

    return newImg

def medianFilter(img, mode):

    img = paddingArrayApply(img, mode)

    newImg = []

    for i in range(1, len(img) - 1):
        tempArr = []
        for k in range(1, len(img[i]) - 1):
            currArr = getCurrentArr(img, i, k)
            tempArr.append( statistics.median(currArr) )  
        newImg.append(tempArr)

    return newImg

def laplacianFilter(img, mode):

    img = paddingArrayApply(img, mode)

    newImg = []

    for i in range(1, len(img) - 1):
        tempArr = []
        for k in range(1, len(img[i]) - 1):
            tempArr.append( float(img[i][k]*-4 + img[i][k - 1] + img[i][k + 1] + img[i - 1][k] + img[i + 1][k] ) ) 
        newImg.append(tempArr)

    return newImg

def alphaTrimmedMeanFilter(img, mode, d):

    img = paddingArrayApply(img, mode)

    newImg = []

    for i in range(1, len(img) - 1):
        tempArr = []
        for k in range(1, len(img[i]) - 1):
            currArr = getCurrentArr(img, i, k)
            currArr.sort()
            leftArr = currArr[ int( (d/2))  : int(len(currArr) - (d/2))]
            tempArr.append( float(sum(leftArr) / (9 - d)) )  
        newImg.append(tempArr)

    return newImg

# arr = np.array([
#     [1,1,1,8,7,4],
#     [2,255,2,3,3,3],
#     [3,3,255,4,3,3],
#     [3,3,3,255,4,6],
#     [3,3,4,5,255,8],
#     [2,3,4,6,7,8],
# ])

# print( minFilter(arr, "repl") )
# print( harmonicMeanFilter(arr, "repl" ) )

arr = np.array([
    [2,5,5,7,1],
    [3,4,7,6,2],
    [4,6,5,4,2],
    [9,7,4,3,1],
    [8,6,3,2,3],
])

print( midPointFilter(arr, "repl") )
print( medianFilter(arr, "zero") )

# mode "zero" or repl""
# qOne = meanFilter(arr, "repl")
# qTwo = midPointFilter(arr, "repl")
# qThree = medianFilter(arr, "zero")
# qFour = laplacianFilter(arr, "zero")
# qFive = alphaTrimmedMeanFilter(arr, "zero", 4)


# print( meanFilter(arr, "repl") )
# print( midPointFilter(arr, "repl") )
# print( medianFilter(arr, "zero") )
# print( laplacianFilter(arr, "zero") )
# print( alphaTrimmedMeanFilter(arr, "zero", 4) )

# print( minFilter(arr3, "") )
# print( maxFilter(arr3, "") )
# print( geometricMeanFilter(arr2, "zero" ) )
# print( harmonicMeanFilter(arr2, "zero" ) )
# print( medianFilter( arrQ26 , "zero" ) )

# arr2 = np.array([
#     [1,200,200],
#     [200,200,200],
#     [200,200,200],
# ])

# arr2 = np.array([
#     [1,1,1],
#     [1,1,1],
#     [1,1,200],
# ])

arr3 = np.array([
    [1,2,1,4,3],
    [1,2,2,3,4],
    [5,7,6,8,9],
    [5,7,6,8,8],
    [5,6,7,8,9]
])
