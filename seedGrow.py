class PointCond:
    def __init__(self, value, isSeed):
        self.value = value
        self.isSeed = isSeed
    
    def setSeed(self):
        self.isSeed = True

def checkArrValid(currentPol, arr, eightOrFour):
    numPol = []
    if eightOrFour == "eight":
        numPol = [[-1,-1], [0,-1], [1,-1], [-1,0], [1,0], [-1,1],[0,1], [1,1]]
    elif eightOrFour == "four":
        numPol = [[0,-1],[-1,0],[1,0],[0,1]]

    validPt = []

    for i in numPol:
        nowX = currentPol[0] + i[0]
        nowY = currentPol[1] + i[1]

        if nowX < 0 or nowY < 0 or nowX >= int(len(arr)) or nowY >= int(len(arr[0])):
            continue
        else:
            validPt.append([nowX, nowY])
        
    return validPt      

def printCurrArr(classArr):
    finalValArr = []
    finalCondArr = [ [" "] + [str(i) for i in range(len(classArr[0]))] ]
 
    for indX, valueX in enumerate(classArr):
        valArr = []
        condArr = []

        condArr.append(str(indX))

        for indY, valueY in enumerate(valueX):
            valArr.append(valueY.value)
            if valueY.isSeed:
                condArr.append("O")
            else:
                condArr.append(" ")

        finalValArr.append(valArr)
        finalCondArr.append(condArr)
    
    return (finalValArr, finalCondArr)

def connectivityCal(arr, seedPolX, seedPolY, conditions, eightOrFour):
    classArr = []

    for i in arr:
        temp = [ PointCond(k, False) for k in i]
        classArr.append(temp)
    
    classArr[seedPolX][seedPolY].setSeed()
    
    finished = False

    while not finished:
        finished = True
        seedArr = []

        for indX, valueX in enumerate(classArr):
            for indY, valueY in enumerate(valueX):
                if valueY.isSeed:
                    seedArr.append([indX, indY])
        
        for i in seedArr:
            compPt = checkArrValid(i, arr, eightOrFour)

            for k in compPt:
                diffNum = abs( arr[k[0]][k[1]] - arr[i[0]][i[1]] )
                if diffNum <= conditions:

                    if not classArr[k[0]][k[1]].isSeed:
                        classArr[k[0]][k[1]].setSeed()
                        finished = False
        
        print("------------------")
        finalValArr, finalCondArr = printCurrArr(classArr)
        [print(k) for k in finalValArr]
        [print(k) for k in finalCondArr]

if __name__ == "__main__":
    arr = [
        [4,3,7,3,3],
        [1,7,8,7,5],
        [0,5,6,1,3],
        [2,2,6,0,4],
        [1,2,1,3,1],
    ]

    seedPolX = 1
    seedPolY = 2
    seed = arr[seedPolX][seedPolY]
    conditions = 1

    # arr = [
    #     [10,10,10,10,10,10,10],
    #     [10,10,10,69,70,10,10],
    #     [59,10,60,64,59,56,60],
    #     [10,59,10,60,70,10,62],
    #     [10,60,59,65,67,10,65],
    #     [10,10,10,10,10,10,10],
    #     [10,10,10,10,10,10,10],
    # ]

    # seedPolX = 3
    # seedPolY = 3
    # seed = arr[seedPolX][seedPolY]
    # conditions = 5

    connectivityCal(arr, seedPolX, seedPolY, conditions, "eight")
    connectivityCal(arr, seedPolX, seedPolY, conditions, "four")