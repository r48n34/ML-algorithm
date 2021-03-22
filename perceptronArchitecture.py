import numpy as np
import math

def decision(a):
    if a >= 0:
        return 1
    else:
        return 0

x = [1,1]

g1 = x[0] + x[1] - 0.5
g2 = x[0] + x[1] - 1.5

print("g1 = " + str(g1) + " Deci = " + str(decision(g1)) )
print("g2 = " + str(g2) + " Deci = " + str(decision(g2)) )


op = decision(g1) - decision(g2) - 0.5
print("op = " + str(decision(g1)) + " - " + str(decision(g2)) + " - 0.5 = " + str(op))
