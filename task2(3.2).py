import math

x = 1

y = 4

z = 3
part1 = math.pow(math.fabs(math.sqrt(1/(math.tan(y))+6)),3)
numerator =(x+1)**3
denominator = 4*y - 2*z
part2 = math.sqrt(numerator/denominator)
print(part1 + part2)
