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
fMeasure = (2 * recall * precision) / (recall + precision)

fpRate = 1 - specificity # ~a
fnRate = 1 - recall # ~b
power = 1 - fnRate

tprOverFPR = recall/fpRate

print("Care if like 1 - 0.8 = 0.1999...6 => 0.2") 
print("--------------------")

print('{} + {} / {} + {} + {} + {}'.format(y[0], n[1],y[0] , y[1] , n[0] , n[1]))
print("accurate = " + str(accurate) )
print()

print('{} / ({} + {}) '.format(y[0] , y[0] , n[0]))
print("precision = " + str(precision) )
print()


print('{} / ({} + {}) '.format(y[0] , y[0] , y[1]))
print("recall = " + str(recall) )
print()


print('{} / ({} + {}) '.format(n[1] , n[0] , n[1]))
print("specificity = " + str(specificity) )
print()


print('2 * {} * {} / ({} + {}) '.format(recall, precision , recall , precision))
print("fMeasure = " + str(fMeasure) )
print()


print('1 - {}'.format(specificity))
print("fpRate = " + str(fpRate) )
print()


print('1 - {}'.format(recall))
print("fnRate = " + str(fnRate) )
print()


print('1 - {}'.format(fnRate))
print("power = " + str(power) )
print()

print('{} / {}'.format(recall,fpRate))
print("TPR / FPR = " + str(tprOverFPR) )
