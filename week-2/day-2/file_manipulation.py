# -*- coding: utf-8 -*-
"""
Created on Tue May 14 09:15:28 2019

@author: Ted_Liu
"""


#### Divide by zero ## print(line, end="")
def my_fun(num):
    try:
        print( 10/num )
    except ZeroDivisionError:
        print("fail")
    finally:
        pass


my_fun(0)



#### print each line


my_file = open("my-file.txt", "r")

try: 
 my_file.readlines()
except FileNotFoundError:
    print("Unable to read file: my-file.txt")


### count_lines
    
def my_func(filename = ""):
    my_file = open(filename, "r")
    try:
        my_file.readlines()
    except IOError:
        return 0
    except:
        pass
    finally:
        pass
    

###write_single_line.py
        
def my_func2(filename=""):
    my_file = open(filename, "a")
    
    try:
        my_file.write("ted\n")
    except:
        print("Unable to write file: my-file.txt")
        
    my_file.close()
    
    
my_func2("my-file.txt")    
my_file.write("ted\n")


###  mutiple_lines

def my_fun3(path, word, num):
    my_file = open(path, "w")
    try: 
        for i in range(0, num):
            my_file.write(word)
    except:
        print("could not write the file")
    finally:
        my_file.close()
    

    
###  copy_file
        
def my_fun4(filename, target):
    my_file = open(filename, "r")
    my_target = open(target, "w")
    
    try:
        word = my_file.read()
        my_target.write(word)
        print(True)
    except:
        print(False)
        
        
#  tic tac      
def tic_tac_result(filename):
    my_file = open(filename, "r")
    my_text = my_file.readlines()
    for j in range(0, 3):
        if my_text[0][j] == my_text[1][j] and my_text[1][j] == my_text[2][j]:
            return (my_text[0][j])
    for i in range(0, 3):
        if my_text[i][0] == my_text[i][1] and my_text[i][1] == my_text[i][2]:
            return (my_text[i][0])
    if my_text[0][0] == my_text[1][1] and my_text[1][1] == my_text[2][2]:
        return (my_text[0][0])
    elif my_text[0][2] == my_text[1][1] and my_text[1][1] == my_text[2][0]:
        return (my_text[0][2])
    
    return "Draw"

    
tic_tac_result("win-o.txt")       
tic_tac_result("win-x.txt")       
tic_tac_result("draw.txt")       
  
        
###  
import numpy


def log_fun():
    my_file = open("log.txt", "r")
    my_text = my_file.readlines()
    return numpy.unique(my_text)
        


def ration_fun():
    my_file = open("log.txt", "r")
    my_text = my_file.readlines()
    count_get = 0
    count_post = 0
    for i in  my_text:
        if "GET" in i:
            count_get += 1
        else:
            count_post += 1
        
    return count_get / count_post    
        
        
log_fun()        

ration_fun()   
    


###  doubled

def decrpt(file_name):
    my_file = open(file_name, "r")
    my_text = my_file.readlines()
    for line in my_text:
        word_list = []
        new_line = line.split()
        for word in new_line:
            list_of_output = []
            for i in range(0, len(word)):
                    if i == len(word) - 1:
                        list_of_output.append(word[-1])
                    elif  word[i] != word[i+1]:
                        list_of_output.append(word[i - 1])

            output_string = "".join(list_of_output)
            word_list.append(output_string)

        line_list = " ".join(word_list)
        print(line_list)    

    
print(decrpt("duplicated-chars.txt"))









   
    
    
    
    
    
    
    
    
    