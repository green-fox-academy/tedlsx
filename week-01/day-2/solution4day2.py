# -*- coding: utf-8 -*-
"""
Created on Tue May  7 10:36:41 2019

@author: Ted_Liu
"""

## import some useful package

import statistics





print("Hello World")

print("Humpty Dumpty sat on a wall,")
print("Humpty Dumpty had a great fall.")
print("All the king's horses and all the king's men")
print("Couldn't put Humpty together again.")

#Hello Yuan , Suke, Changdong, Santy, Zilan, Sara, Panne
#my profile
print("""ted_liu
24
1.79m""")      

#2 num
print (13+22)
print(22-13)
print(22*13)
print(22/13)
print(22//13)
print(22%13)

#code hour
print(6*17*5) #5 work days per week
code_h=6*17*5
print(code_h/(52*17))

# favourite num
favourite_number = 7

print("My favourite number is: " ,favourite_number)

#swap
a=123
b=526

b,a=a,b # or  def a temp, temp=b, b=a,a=temp
print(a)
print(b)

#bmi
massInKg = 81.2
heightInM = 1.78
def bmi(heightInM,massInKg):
    print ("Your body mass index is: ",
           (massInKg)/(heightInM**2))


bmi(heightInM,massInKg)

#Intro 4 me
my_name="ted_liu"
my_age=24
my_height=1.79
amImarried = False


#variable_mutation
a=3
a += 10
print(a)

b=100
b += -7
print(b)

c=44
c *= 2
print(c)

d=125
d /= 5
print(d)

e=8
e **= 3
print (e)

f1=123
f2=345
if f1 > f2:
    print("f1 is bigger than f2")
else: 
    print("f1 is not bigger than f2")    

g1 = 350
g2 = 200
if g2 * 2 > g1 :
    print(True)
else:
    print(False)    


h = 1357988018575474
if h%11 == 0:
    print (True)
else:
    print(False)    

i1 = 10
i2 = 3
if i1 > i2**2 and i1 < i2**3:
    print(True)
else:
    print(False)    

j=1521
if j%3 ==0 | j%5 ==0:
    print (True)
else:
    print(False)    

# cuboid
width=0.0
length=0.0
height=0.0

def cub(width,length,height):
    sur=2*(width*length+height*width+height*length)
    vol=width*length*height
    print("Surface Area:",sur)
    print("Volume:", vol)    


cub(1.1,2.3,3.4)


##seconde in day
current_hours = 14;

current_minutes = 34

current_seconds = 42

def sec(current_hours, current_minutes,current_seconds):
    sec_1 = 60 - current_seconds
    sec_2 = 60*(60 - (current_minutes+1))
    sec_3 = 60*60*(24 - (current_hours+1))
    return (sec_1+sec_2+sec_3)

sec(14,34,42)        

# hello user

name = input("What is your name?")

print("Hello ", name)
    
# mile to km
distance =int( input("Please enter the distance in mile as a integer:"))
print("The distance in kilometers is ",distance/1000)


## animals and legs
chicken= int(input("Please enter the numbers of chicken"))
pig = int(input("Please enter the number of pigs"))
print("There're ",2*chicken+4*pig ,"legs !")



###
list= []
for i in range(0,5):
    integer = int(input("enter a number:" ))
    list.append(integer)

print ("Sum: ",sum(list),"Average: ",statistics.mean(list))


### odd even
number = int(input("enter a number:"))
if number == 0: 
    print("Even")
elif number % 2 ==0:
    print("Even")
elif number %2 == 1:
    print("Odds")
else:
    print("It is not a non-negative integer")    


# one two al ot
number = int(input("enter a number:"))

if number <= 0:
    print("Not enough")
if number == 1:
    print("One")
if number == 2:
    print("Two")
if number >2 :
    print("A lot")    


###bigger 
list =[]
for i in range(0,2):
    num = int(input("enter a number:"))
    list.append(num)

if  list[0] == list[1]:
    print("Two numbers are same and is ",list[0])
else:    
    print("the bigger one is ",max(list))

###party _ indicator
num_girls = int(input("enter the number of girls:"))
num_boys = int(input("enter the number of boys:"))    
if num_boys == num_girls and num_boys + num_girls >= 20 :
    print("The party is exellent")
elif num_boys != num_girls and num_boys + num_girls >= 20 :
    print("Quite cool party")
elif num_boys + num_girls < 20 :
    print("Average")
elif num_girls == 0 :
    print("Sausage party")
else:
    print("No type")    

###
a=24
out=0    
while a % 2 ==0 :
    out += 1
print(out)    


b = 13
out2 = ""

if b >= 10 and b <= 20 :
    out2 = "Sweet!"
elif b < 10 :
    out2 = "Less!"     
elif b >20 :
    out2 = "More!"
    
print(out2)


c = 123
credits = 100
is_bonus = False

if credits >= 50 and is_bonus == False :
    c -= 2
elif credits < 50 and is_bonus == False :
    c -= 1
elif is_bonus == True :
    c = c    
    
print (c)

d = 8 
time = 120
out3 = ""

if d % 4 == 0 and time <= 200 :
    out3 = "check"
elif time > 200 :
    out3 = "Time out"    
else:
    out3 = "Run Forest Run"

print(out3)

### I wont
for i in range(0,100):
    print("I wont't cheat on the exam")

###print_even
    
for i in range(0,501,2):
    print(i)

##mul table
num = 15
for i in range(1,11):
    print (i ," * ", num, " = ", i*num )

## count from
list = []
for i in range(0,2):
    num = int(  input( "enter a number:" ))
    list.append(num)
if list[0] >= list[1] :
    print("The second one should be bigger")
while list[0] < list[1] :
    print (list[0])
    list[0] += 1


## fizz_buzz

for i in range(1,101):
    if i % 3 == 0 :
        print("Fizz")
    elif i % 5 ==0 :
        print("Buzz")
    elif i % 3 and i % 5 ==0:
        print ("FizzBuzz")
    else:
        print(i)
    
## draw triangle

num = int(input("enter a number:"))

for i in range(1,num+1):
    print("*" * i)

## draw pyramid
num = int(input("enter a number:"))
j = num-1
for i in range(1 , num + 1):
    print(" " * j,"*" * (2*i-1)," " * j)    
    j -= 1
    
    
##    draw dimond 
    
num = int(input("enter a number:"))   

j = num -1
for i in range(1 , num + 1):
    print(" " * j,"*" * (2*i-1)," " * j)    
    j -= 1    
j = num - 1   
for i in range(1 , num + 1): 
    print(" " * i,"*" * (2*j-1)," " * i)
    j -= 1  
        
    
 ###  draw square 
    
    
num = int(input("enter a number:"))   

for i in range(1 , num+1):
    if i == 1 or i == num :
        print ("%" * num)
    else:
        print("%"+" "*(num-2)+"%")    
    
    
    
####     draw diagonal

num = int(input("enter a number:")) 
j = num
for i in range(1 , num+1):
    if i == 1 or i == num :
        print ("%" * num)
    else:
        print("%"+" " * (i-2) + "%" + " " * (j-2) +"%")    
    j -= 1 ## note that we always meet i=1 at first
    

###    Guess number

answer_num = 10
for i in range(1,100):    
    num = int(input("enter a number:"))    
    if num < answer_num :
        print ("The stored number is higher")
    elif num > answer_num :
        print ("The stored number is lower")
    elif num == answer_num :
        print ("You found the number:" ,answer_num)    
        
    
    
###   parametric_average
        
repeat_number = int(input("enter a number:"))    
list = []
for i in range(1,repeat_number+1) :
    num = int(input("enter a integer:"))
    list.append(num)    
print("Sum:", sum(list),"Average:",statistics.mean(list))    
    
### draw chess
row_num =     
col_num = 8   

for i in range(1,row_num+1):
    if i % 2 ==0:
        print (" %" * int((col_num / 2)))
    elif i % 2 ==1:
        print ("% " * int((col_num / 2)) )
    
    
    
## substr    

str = ""
keyword = ""

def substr(str, keyword):
    indexcount = 0
    ind = 0
    str_s = str.split()
    if keyword in str :
        for word in str_s:
            if word != keyword :
                ind = ind + len(str_s[indexcount]) + 1
            else:    
                return ( ind )
            indexcount += 1 
            
    else:
        return(-1)


print(substr("this is what I'm searching in", "searching"))
print(substr("this is what I'm searching in", "not"))























    











