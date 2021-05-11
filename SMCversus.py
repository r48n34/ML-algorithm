x = [1,0,0,0,0,0,0,0,0,0]
y = [0,0,0,0,0,0,1,0,0,1]

i = int(0)
f01 = int(0)
f10 = int(0)
f00 = int(0)
f11 = int(0)

while (i < int(len(x))):
    if x[i] == 0 and y[i] == 1:
        f01 += 1
    elif x[i] == 1 and y[i] == 0:
        f10 += 1
    elif x[i] == 0 and y[i] == 0:
        f00 += 1
    elif x[i] == 1 and y[i] == 1:
        f11 += 1

    i += 1

print("f01 = " + str(f01))
print("f10 = " + str(f10))
print("f00 = " + str(f00))
print("f11 = " + str(f11))

smc = (f11 + f00) / (f01 + f10 + f11 + f00)
j = f11 / (f01 + f10 + f11)

print("SMC = (", f11, "+", f00, ") / (", f01, "+", f10, "+", f11, "+", f00, ") = ", smc)
print("J = ", f11, " / (", f01 , "+", f10 , "+", f11 , ") = " , j )
