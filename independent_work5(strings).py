#independent work (5)
#task1
import re
txt = """First, I wake up. Then, I get dressed. I walk to school:
I do not ride a bike, I do not ride the bus, I like to go to school.
It rains: I do not like rain. I eat lunch: I eat a sandwich and an apple."""
print ("task 1: ",txt)
count = 0
for i in range(0, len(txt)): 
    if txt[i] == "e":
        count+=1
        
print ("the frequency of the letter 'e' is " ,count)


#task2
print ("\n task 2: ", txt.replace(':','%'))
replacement = 0
for x in txt:
    if x ==":":
        replacement += 1
    else: continue
print ("the frequency of replacement is ", replacement)

#task3
print("\n task 3: ", txt.replace('.',''))
remover = 0
for y in txt:
    if y == ".":
        remover += 1
    else: continue

print ("the frequency of removed dots is ", remover)

#task4
print ("\n task 4: ", txt.replace('a','o'))
replacement_o = 0
for x in txt:
    if x =="a":
        replacement_o += 1
    else: continue
print ("the frequency of replacement is ", replacement_o)

#task5
print("\n task 5: ", txt.lower())

#task6
print("\n task 6: ", txt.replace('a',''))
remover_a = 0
for y in txt:
    if y == "a":
        remover_a += 1
    else: continue

#task7
n = len(txt)
length = txt[:n//2].replace("n", "*") + txt[n//2:]
print("\n task 7: ", length)

#task8
string = "I wake up."
answer = len(string.split())
print ("\n task 8: ", string)
print ("the number of words in sentence:", answer)

#task9
txt9 = "dress, butter, dress, sun"
dress = txt9.count("dress")
print ("\n task 9: ", txt9)
print ("the frequency of the words 'dress' is " ,dress)

#task10
string = "did expect something but got nothing"
print ("\n task 10: ")
txt = string.split()
cout=list()
for word in txt:
    cout = list(word)
    cout[0] = cout[0].upper()
    print(''.join(cout))

#task11
my_str = """ nnnnnnnna n! naaaaaaaaaaaannn nann! nnnnann nnnx nvfnnn! nnwennnnn"""
print ("\n task 11: " ,my_str.replace("!","."))
last_char = "n"
current_seq_len = 0
max_seq_len = 0

for x in my_str:
    if x == "n":
        current_seq_len += 1
        if current_seq_len > max_seq_len:
            max_seq_len = current_seq_len
    else:
        current_seq_len = 1
        last_char = x
print("the largest number of the letter n is", max_seq_len)

#task12
string = "breakfast lol aghjjl sequence cruel"
print ("\n task 12: ")
txt = string.split()
for i in txt:
    if i.endswith ("l"):
        print (i)
    else: pass
    
#task13
txt = "please can you go (me alone)"
print (txt.split("(")[-1].split(")")[0])

#task14
string ="happy birthday, alina. i love you. you are my only samurai ."
for i in string.split():
    if i.startswith("a") or i.endswith("i"): 
        print("words that start with ''a'' or end with ''i'': ", i)

#task15
txt = str(input("enter some text "))
count = 0
while txt.find("t") != -1:
    txt = txt.replace("t", "", 1)
    count += 1
print(count)


