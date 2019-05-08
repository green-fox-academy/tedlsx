
## doubling 

base_num = 123

def doubling(para ):
    return (2*para)
    

print (doubling(base_num))


###  greet 
al = "Greenfox"

def greet( para):
    return "Greetings, dear "+para

greet(al)


####  append 

typo = "Chinchill"

def append_a_func(s):
    return s+"a"

print(append_a_func(typo))

## sum

def sum_new( para ):
    a=0
    for i in range(0,para+1):
        a = a + i
    return a

sum_new(5)    


#### factorio
def factorio( para ):
    a = 1
    for i in range(1, para+1):
        a = a*i
    return a

factorio(5)


## print arguments 
def print_params( *para ):
    return ( para )

print_params("a",123)






def subint(num , mylist):
    list_res =[]
    for i in mylist:
            inum = [int(j) for j in str(i)]
            if num in inum:
                list_res.append(mylist.index(i))
    return (list_res)      


subint(1,[1,11,34,52,61])
print(subint(9, [1, 11, 34, 52, 61]))




### unique
def unique(arr):
    uni_list =[]
    for i in arr:
        if i not in uni_list:
            uni_list.append(i)
    return uni_list

 
print(unique([1, 11, 34, 11, 52, 61, 1, 34]))       
        

#### anagram 
   
def anagram( s1, s2 ):
    if sorted(list(s1)) == sorted(list(s2)):
        return True
    else:
        return False
        
anagram("dog","god") 
anagram("green" , "fox")  

######### palindrome builder
def palindrom(s):
    l = list(s)
    l_new = l[::-1]
    sep = ""
    l_word = sep.join(l_new)
    return (s + l_word)

palindrom("greenfox")    
palindrom("123")

### Palindrome seacher
def search_palindrome( para):
    mylist = []
    for i in range(0,len(para)):
        s_1 = ""        
        for j in range(i+1 , len(para)):
            s_1 += para[j]
            s_2 = para[i] + s_1
            pal = palindrom(s_2)
            pal = str(pal)
            len_pal = len(pal)
            pal_new = pal[ :(int((len_pal/2)-1))] + pal[int(len_pal/2) : ]

            if int(len_pal/2) > len(s_2):
                continue
            elif pal_new in para:
                mylist.append(pal_new)
    return mylist            
            
        

search_palindrome("dog goat dad duck doodle never")
search_palindrome("apple")
search_palindrome("racecar")





#### sort list
def bubble(arr):
    for i in range(0, len(arr)):
        for j in range(0, len(arr)-i-1):
            if i+1 >= len(arr):
                break
            elif arr[j] > arr[j+1]:
                arr[j],arr[j+1] = arr[j+1],arr[j]
    return arr                
            
def advanced_bubble(arr, b=False):
    for i in range(0, len(arr)):
        for j in range(0, len(arr)-i-1):
            if i+1 >= len(arr):
                break
            elif arr[j] > arr[j+1]:
                arr[j],arr[j+1] = arr[j+1],arr[j]
    if b == True:
        arr = arr[::-1]
        return arr            
    else:    
        return arr
            
bubble([43, 12, 24, 9, 5])


print(advanced_bubble([43, 12, 24, 9, 5], True))






    
    