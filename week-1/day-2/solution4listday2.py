# -*- coding: utf-8 -*-
"""
Created on Tue May  7 21:26:11 2019

@author: Ted_Liu
"""
###
numbers = [4, 5 ,6 ,7]

print(numbers)


## third
q = [4,5 ,6, 7]
q[2]


## compare length 

p1 = [1,2,3]
p2 = [4,5]
if len(p2) > len(p1):
    print ("p2 is longer")
    
## sum length    
r = [54 , 23, 66, 12]    
print (r[1]+r[2])


## change elements

s = [1,2,3,8,5,6]

s[3] = 4
print(s)
print(s[5])

## increment 
t = [1,2,3,4,5]
t[2] = t[2] + 10
print(t[2])

###  diagonal 

N = 4
myList = [[0] * N for i in range(N)]

print(myList)

for row in range(N):
    for col in range(N):
        if row == col:
            myList[row][col] = 1

print(myList)


####double item
j = 0
numList = [3,4 ,5,6,7]
for i in numList:
    numList[j] = 2*i
    j += 1
    
print(numList)    
    
    
### color 
colors = [0]*3

colors[0] =["'lime', 'forest green', 'olive', 'pale green', 'spring green'"]
colors[1] = ['"orange red", "red", "tomato"']
colors[2] = ['"orchid", "violet", "pink", "hot pink"'    ]

print(colors)    


## append
j=0
animals = ["koal", "pand", "zebr"]    
for i in animals:
    animals[j]  = i + "a"
    j += 1
print(animals)    
    
### swap element

abc = ["first", "second", "third"]    
abc[0] , abc[2] = abc[2] , abc[0]   
    
print(abc)


## sum 

ai = [3, 4, 5, 6, 7]
print (sum(ai))

## reverse 

aj = [3,4,5,6,7]
aj.reverse() 
print(aj)







