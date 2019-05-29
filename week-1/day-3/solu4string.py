# -*- coding: utf-8 -*-
"""
Created on Wed May  8 15:12:37 2019

@author: Ted_Liu
"""

## ### simple replace

example = "In a dishwasher far far away"
print( example.replace("dishwasher" , "galaxy"))

## url fixer

url = "https//www.reddit.com/r/nevertellmethebots"

print(url.replace("bots" , "odds"))

### take longer 

quote = "Hofstadter's Law: It you expect, even when you take into account Hofstadter's Law."

index = quote.find("you")
print(index)
quote = quote[:index] + " always takes longer than " + quote[index:]


print(quote)

####  to do list
todotext = " - Buy milk\n"
todotext = "My todo:\n" + todotext[:] 
todotext = todotext[:] + " - Download games\n"
todotext = todotext[:] + " - Diablo\n"

print(todotext)


### reverse 

reversed = ".eslaf eb t'ndluow ecnetnes siht ,dehctiws erew eslaf dna eurt fo sgninaem eht fI"
def reverse( s ):
    return s[::-1]


print(reverse(reversed)) 


####  Data structure 
names = []
print(len(names))
names = names + ["William"]
##   or names.append(["William"])
print (len(names))
names = names + ["John"]
names = names + ["Amanda"]
print(len(names))

print ( names[2])

for i in names:
    print (i)

j = 0
for i in names:
    j += 1
    print (j, ". " , i)
    
names = names[:1] + names[2:]    

for i in range(len(names)-1 ,-1,-1):
        print(names[i])

names =[1,2]
names.clear() 
del names[:]
print(names)
###    Map 
M = {}
print ( len(M))

M  = { "97": "a", "98": "b", "99": "c", "65": "A", "66": "B", "67": "C"}

print(M.keys())

print(M.values())

M["68"] = "D"

print(M)

print(len(M))

print (M.get("99"))

del M["97"]
print (M)


"100" in M.keys()

M.clear()

#####
 ##  list intro 2
listA = ["Apple", "Avocado", "Blueberries", "Durian", "Lychee"]
listB = listA

"Durian" in listA

listB.remove("Durian")

print(listB)

listA.insert(4, "Kiwifruit")
print(listA)

len(listA) - len(listB)

listA.index("Durian")

listB.extend(["Passion Fruit","Pummelo"])

print(listA[2])


###### Map intro 2

M2 = {"978-1-60309-452-8":"A Leter to Jo", "978-1-60309-459-7": "Lupus", "978-1-60309-444-3":"Red Panda and Moon Bear" , "978-1-60309-461-0": "The Lab" }

for i in M2.keys():
    print(  M2[i] , "(ISBN: ",i,")")


del M2["978-1-60309-444-3"]

j = 0
for i in M2.keys():
    if M2[i] == "The Lab":
        j = i
del M2[j]

print(M2)


M["978-1-60309-450-4"] = "They Called Us Enemy"

M["978-1-60309-453-5"] = "Why Did We Trust Him?"

"478-0-61159-424-8" in M.keys()


M["978-1-60309-453-5"]

### personal finance 

mylist = [500, 1000, 1250, 175, 800 , 120]

sum(mylist)

max(mylist)

min(mylist)

import statistics as sta

sta.mean(mylist)

### telo phone
M = {"William A. Lathan": "405-709-1865", "John K. Miller": "402-247-8568", "Hortensia E. Foster":"606-481-6467","Amanda D. Newland":"319-243-5613","Brooke P. Askew":"307-687-2982" }

M["John K. Miller"]


for i in M.keys():
    if M[i] == "307-687-2982":
        print (i)

"Chris E. Myer" in M.keys()

##### shopping list:

mylist = ["Eggs", "milk", "fish", "apples", "bread", "chicken"]

"milk" in mylist

"bananas" in mylist


### product database 

M ={"eggs":200 , "milk": 200, "fish":400, "apples":150, "bread": 50 , "chicken": 550}

M["fish"]

m = max(M.values())
for i in M.keys():
    if M[i] == m:
        print (i)


sta.mean(M.values())

mylist = []
for i in M.keys():
    if M[i] < 300 :
        mylist.append(i)
print(mylist)

125 in M.values()

m = min(M.values())
for i in M.keys():
    if M[i] == m:
        print (i)

### database 2
    
mylist = []
for i in M.keys():
    if M[i] < 201 :
        mylist.append(i)
print(mylist)


mylist = []
for i in M.keys():
    if M[i] > 150 :
        mylist.append(i)
print(mylist)


#### sets
sample = set()
sample.add("a")
sample.add("b")
sample.add("c")
sample.add("d")

sample.remove("a")

for i in sample:
    print (i)

sample.remove(42)


####### bags 

s1 =set()
s1.add("laptop")
s1.add("notebook")
s1.add("pen")
s1.add("sunglasses")
s1.add("hand sanitizer")

s2=set()
s2.add("sunglasses")
s2.add("notebook")
s2.add("phone")

s3 =set()
s3.add("laptop")
s3.add("sunglasses")
s3.add("hand sanitizer")

 

s1
s2

s1 - s2

s1 and s2 and s3

s = ["a","a","b","c"]

def unique(list1):  
    unique_list = []       
    for x in list1: 
        if x not in unique_list: 
            unique_list.append(x) 
    return unique_list
myset =set()
for i in unique(s):
    myset.add(i)
print (myset)



































