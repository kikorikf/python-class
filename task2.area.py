import math

shape = int(input("choose what do you need to find: \n1.triangle\n2.rectangle\n3.circle\n"))

if shape == 1: #triangle
    a = float(input ("give side a "))
    b = float(input ("give side b "))
    c = float(input ("give side c "))
    p = (a + b + c)/2
    print("The area of the triangle is ", math.sqrt(p*(p-a)*(p-b)*(p-c)))
elif shape == 2:
   a = float(input ("give side a "))
   b = float(input ("give side b "))
   c = float(input ("give side c "))
   d = float(input ("give side d "))
   print("The area of the rectangle is ", a*b*c*d)

#circle
else:
  r = float(input("give the value of radius "))
  print("The area of the circle is ", math.pi*r*2)


