import pandas as pd
# y = w1 * x1 + w2 * x2 + b

import numpy as np
import scipy.optimize
 
data = pd.read_csv("./codeNotes/university/4016hw1/ass1_data.csv")
data = np.array(data[:])

xs = data[:,0]
ys = data[:,1]
zs = data[:,2]

tmp_A = []
tmp_b = []

for i in range(len(xs)):
    tmp_A.append([xs[i], ys[i], 1])
    tmp_b.append(zs[i])

b = np.matrix(tmp_b).T
A = np.matrix(tmp_A)
fit = (A.T * A).I * A.T * b

print ("solution:")
print ("%f x1 + %f x2 + %f = z" % (fit[0], fit[1], fit[2]))
print("w1 = " , fit[0] , "w2 = ", fit[1], "b = " , fit[2])