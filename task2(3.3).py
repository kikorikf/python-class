import math
x = 3
y = 0.2
part1 = 5*x*y/(x**3-4)+ math.exp(x**2)
part2 = math.sqrt(math.cos(y)**2 - y**2)
print(part1 + part2)
