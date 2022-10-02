# 1task
# class Rectangle:
#     def __init__ (self,color="green", width=100,height=100, addone = 0):
#         self.color = color
#         self.width = width
#         self.height = height
#         self.addone = addone
#     def square(self):
#         return self.width *self.height
#     def setaddone(self,number):
#         self.addone = number
#         print(self.addone)
# rect1 = Rectangle()
# print(rect1.color)
# print(rect1.square())
# rect1 = Rectangle("yellow",23,34)
# print(rect1.color)
# print(rect1.square())
# print(rect1.addone)
# rect1.setaddone(5)

# 2task
# class Name:
#     def __init__(self,f_name,l_name):
#         self.f_name = f_name[0].upper() + f_name[1:len(f_name)].lower()
#         self.l_name = l_name[0].upper() + l_name[1:len(l_name)].lower()
#     def __repr__(self):
#         print(f'{self.f_name} {self.l_name}')
# name = Name("ALINA","mITRoshina" )
# print(person.f_name)
# print(person.l_name)
# name.__repr__()



# 3task
# class Calculator:
#     def sum(self,num1,num2):
#         return  num1 + num2
#     def diff(self,num1,num2):
#         return num1 - num2
#     def multiply(self,num1,num2):
#         return  num1 * num2
#     def div(self,num1,num2):
#         return num1 / num2
# calc = Calculator()
# print(calc.sum(10,5))
# print(calc.diff(10,5))
# print(calc.multiply(10,5))
# print(calc.div(10,5))