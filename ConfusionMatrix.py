import math
def pointDiff(x,y):
    return math.sqrt( ((x[0]-y[0])**2)+((x[1]-y[1])**2) )
#    a  b
#   YES NO
y = [40,10] #YES
n = [10,40] #NO
#    c  d

accurate = (y[0] + n[1]) / (y[0] + y[1] + n[0] + n[1])
precision = y[0] / (y[0] + n[0])
recall = y[0] / (y[0] + y[1]) # ~Sensitivity = TP rate
specificity = n[1] / (n[1] + n[0]) # TN rate
fMeasure = (2 * y[0]) / ((2 * y[0]) + y[1] + n[0])

fpRate = 1 - specificity # ~a
fnRate = 1 - recall # ~b

power = 1 - fnRate
tprOverFPR = recall/fpRate

print("accurate = " + str(accurate) ) 
print("precision = " + str(precision) ) 
print("recall = " + str(recall) )
print("fMeasure = " + str(fMeasure) )

print("fpRate = " + str(fpRate) ) 
print("fnRate = " + str(fnRate) )
print("power = " + str(power) ) 
print("TPR / FPR = " + str(tprOverFPR) )