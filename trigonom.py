import math

x = float(input('x = '))
y = float(input('y = '))
y_rad = math.radians(y) #get radians

h_part1 = math.exp(x)+math.exp(-x)
h_part2 = math.cos(2*y)+math.sin(4*y)

h_numerator = math.sqrt(h_part2+math.sqrt(h_part1))
h_denominator = pow(h_part1,3)*pow(h_part2-2,2)
h = h_numerator/h_denominator

print(h)
