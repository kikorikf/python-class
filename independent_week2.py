#independent work week 2
#task1
def add(*args):
    return sum(args)
print(" task 1:" ,add(1,2))
print(add(4,5,6))
print(add(5,4,3,9,10))

#task2
def change(list):
    size = len(list)
    temp = list[0]
    list[0] = list[size - 1]
    list[size - 1] = temp
    return list
     
list = [12, 35, 9, 56, 24]
print ("\n task 2: the original one:" ,list)
print("with swapping:" ,change(list))

#task3
#def to_list(*args):
#    return list(args)
#print(\n task 3:)
#print(to_list(1, 2 , 5, 6,))

#task4
def useless(*args):
    max = args[0]
    for i in args:
        if i > max:
            max = i
            temp = max/(len(args))
    return temp
    return max
    return sum
print ("\n task 4:")   
print(useless(1,2))
print(useless(4,5,6))
print(useless(5,4,3,9,10))

#task5
def list_sort(lst):
    lst.sort(key=lambda x: abs(x), reverse=True)
    return lst
print("\n task 5:")
print(list_sort([1, 3, 4 , 5, 6, 9]))


#task6
print("\n task 6:")

list = ["happy birthday", "flower", "sun"]
print([x.rjust(len(max(list, key = len)), '_') for x in list])


