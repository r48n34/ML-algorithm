import numpy as np

def countFrequencyDomain(arr):
    unique, counts = np.unique(arr, return_counts=True)

    print(unique, counts)

    cumNum = 0
    cumArr = []
    cumSumArr = []
    for ind, items in enumerate(counts):
        cumNum += counts[ind]
        cumArr.append( items / sum(counts) )
        cumSumArr.append( (cumNum / sum(counts) ) * max(unique) )

    print("Frequency")
    print("num freq pr(rk) Tr")
    freqArr = np.asarray((unique, counts, cumArr, cumSumArr)).T

    print(freqArr)

def countThreshold(arr, threshold):
    unique, counts = np.unique(arr, return_counts=True)

    # number, then occur frequency
    backgroundArr = []
    foregroundArr = []

    for i in range(len(unique)):
        if unique[i] < threshold:
            backgroundArr.append([unique[i], counts[i]])
        else:
            foregroundArr.append([unique[i], counts[i]])

    totalBg = sum([i[1] for i in backgroundArr])
    totalFg = sum([i[1] for i in foregroundArr])
    
    weightBg = totalBg / sum(counts)
    weightFg = totalFg / sum(counts)

    meanBg = sum([i[0] * i[1] for i in backgroundArr]) / totalBg
    meanFg = sum([i[0] * i[1] for i in foregroundArr]) / totalFg

    varianceBg = sum([ (i[0] - meanBg)**2 * i[1] for i in backgroundArr] ) / totalBg
    varianceFg = sum([ (i[0] - meanFg)**2 * i[1] for i in foregroundArr] ) / totalFg

    withinClassVariance = weightBg * varianceBg + weightFg * varianceFg
    betweenClassVariance = weightBg * weightFg * (meanBg - meanFg)**2

    print(f'Background: weight = {weightBg}, Mean = {meanBg}, Variance = {varianceBg}')
    print(f'Foreground: weight = {weightFg}, Mean = {meanFg}, Variance = {varianceFg}')
    print(f'Within-Class Variance = {withinClassVariance}')
    print(f'Between-Class Variance = {betweenClassVariance}')


if __name__ == "__main__":
    arr2 = np.array([
        [1,2,1,3,6,6],
        [1,2,2,4,5,7],
        [1,0,2,5,6,7],
        [0,2,3,6,6,7],
        [3,0,4,4,5,7],
        [1,4,3,5,7,7],
    ])

    # Lec 2
    countFrequencyDomain(arr2)

    # Lec 8
    # Within ClassVariance smaller = better 
    # Between ClassVariance bigger = better 
    countThreshold(arr2, 3)


