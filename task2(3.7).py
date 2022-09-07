import math
x = 0.8
y = 0.1
z = 4
num = 1 - x + math.atan(1/x - 7*y)
denom = 4*x*z - math.log1p(y)**2
print ((math.pow(math.sqrt(num/denom),5)) )
