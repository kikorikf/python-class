import cmath  
a = float(input('enter a: '))  
b = float(input('enter b: '))  
c = float(input('enter c: '))  
  

d = (b**2) - (4*a*c)  
if(d > 0):
    print(' real and different root')
elif(d==0):
    print ('roots the same')
else:
    print('complex roots')
x1=(-b-cmath.sqrt(d))/(2*a)  
x2=(-b+cmath.sqrt(d))/(2*a)

print(f"The solution are {x1}, {x2}")  
