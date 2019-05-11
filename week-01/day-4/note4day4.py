# -*- coding: utf-8 -*-
"""
Created on Thu May  9 09:18:24 2019

@author: Ted_Liu
"""

import re

my_string = "o hello world"

# p for pattern
p = re.compile("hello")


p.match("hello world") ## match
p.match("o hello") ### wont match
print ( re.match("[^abc]" , "da"))


print ( p.match(my_string) )

print(p.search(my_string))


print ( re.match( r"\section" , "\section" ))


my_string = "this is 123 , 4456"
m = re.compile(my_string)

print(m)
print(m.group())


my_string = "this is 123 ,qwe"
re.sub("[\d]+" , " <sensitive data>" , my_string)

##    
my_string = " the wether is is nice"
m = re.search(r"(\w+)\s\1" , my_string)
print (m)



