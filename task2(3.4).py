import math
x = 3
y = 5
num = math.atan(1/x)*math.log1p(x)
denom = x**y - y + 1
print((math.fabs(math.sqrt(y))+ num/denom)) 
