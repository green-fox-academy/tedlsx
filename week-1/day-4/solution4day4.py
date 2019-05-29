# -*- coding: utf-8 -*-
"""
Created on Thu May  9 09:46:15 2019

@author: Ted_Liu
"""
import re

## reserved admin
print (re.match( "[Aa]dmin" , "Admin") )
print (re.match("[Aa]dmin" , "admin") )



### numbers

for i in [0,9,55,100,101,-4]:
    print(re.match ("^(100|[1-9][0-9]|[0-9])$" , "%d"%i))



## mobile num

print (re.match("([0]{2}\s)?\+?[036]{1,2}\s[23701]{1,2}\s[1-7]{3}\s[1,2,4,6,7,8,9]{4}" , "+36 20 473 2746"))
print (re.match("([0]{2}\s)?\+?[036]{1,2}\s[23701]{1,2}\s[1-7]{3}\s[1,2,4,6,7,8,9]{4}" , "+36 30 217 4912"))
print (re.match("([0]{2}\s)?\+?[036]{1,2}\s[23701]{1,2}\s[1-7]{3}\s[1,2,4,6,7,8,9]{4}" , "00 36 70 381 1288"))
print (re.match("([0]{2}\s)?\+?[036]{1,2}\s[23701]{1,2}\s[1-7]{3}\s[1,2,4,6,7,8,9]{4}" , "00 36 31 471 2818"))
print (re.match("([0]{2}\s)?\+?[036]{1,2}\s[23701]{1,2}\s[1-7]{3}\s[1,2,4,6,7,8,9]{4}" , "+36 20 3173 4717"))
print (re.match("([0]{2}\s)?\+?[036]{1,2}\s[23701]{1,2}\s[1-7]{3}\s[1,2,4,6,7,8,9]{4}" , "+36 102 237 1121"))
print (re.match("([0]{2}\s)?\+?[036]{1,2}\s[23701]{1,2}\s[1-7]{3}\s[1,2,4,6,7,8,9]{4}" , "+49 20 483 1273"))
print (re.match("([0]{2}\s)?\+?[036]{1,2}\s[23701]{1,2}\s[1-7]{3}\s[1,2,4,6,7,8,9]{4}" , "36 70 381 2183"))



#### GFA email address

for i in ["john@greenfoxacademy.com","jane.doe@greenfoxacademy.com","jane@greenfox.academy", "john@wick.com", "jane@citromail.hu","janegreenfoxacademy.com"]:
    res = re.match("(\w+\\.?\w+)(?:\@greenfox\\.?academy(?:\\.com)?)" , i)
    if res is not None:
        print (res.groups()[0])


##### Image source
    
for i in ["<img src='dog.png'>" , "<img alt='Cat picture' src='./images/cat-01.png'>", "<script src='jquery.js'></script>"]:
     res1 = re.search("(src=\')" , i )
     res2 = re.search("\\.png"   ,  i)

     if res1 and res2 is not None:
         ind1 = res1.span()[1]
         ind2 = res2.span()[0]+4
         print ( i[ind1 : ind2] )
        


















 