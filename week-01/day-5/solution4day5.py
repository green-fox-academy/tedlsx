# -*- coding: utf-8 -*-
"""
Created on Thu May  9 13:26:10 2019

@author: Ted_Liu
"""

##  Bubble sort 
a= [3,2,1,4,5,6,8,7,9,0]

for i in range(0,len(a)):
    for j in range (0 , len(a)-i-1):
        if a[j] > a[j+1] :
            a[j] , a[j+1] = a[j+1] , a[j]
print (a)            


#### insteration sort
a= [3,2,1,4,5,6,8,7,9,0]

for i in range(1 , len(a)):
    while i >0 and a[i-1] > a[i]:
            a[i] , a[i-1]= a[i-1] , a[i]
            i -= 1        
print (a)        


###3 quick sort
a= [3,2,1,4,5,6,8,7,9,0]


def partition(a , left , right):
    i = left -1
    pivot = a[right]
    for j in range(left , right):
        if a[j] <= pivot:
            i += 1
            a[i], a[j] = a[j],a[i]
    a[i+1] , a[right] = a[right], a[left] 
    return i+1       
            
def quicksort(a , left , right):
    if left < right:
        p = partition(a , left , right)
        quicksort(a , left , p-1)
        quicksort(a ,p+1 , right)
    return a       
            
            
            
print (quicksort(a,0,len(a)-1))            
            


######### meerge sort

a= [3,2,1,4,5,6,8,7,9,0]

def mergeSort(a): 
    if len(a) >1: 
        mid = len(a)//2 
        L = a[:mid] 
        R = a[mid:]   
        mergeSort(L) 
        mergeSort(R)   
        i = j = k = 0            
        while i < len(L) and j < len(R): 
            if L[i] < R[j]: 
                a[k] = L[i] 
                i+=1
            else: 
                a[k] = R[j] 
                j+=1
            k+=1          
        while i < len(L): 
            a[k] = L[i] 
            i+=1
            k+=1
        while j < len(R): 
            a[k] = R[j] 
            j+=1
            k+=1            
    return a      
print(mergeSort(a))            
            
            
########## heapsort
a= [3,2,1,4,5,6,8,7,9,0]

def heapify(a, n, i): 
    largest = i   
    l = 2 * i + 1      
    r = 2 * i + 2      
    if l < n and a[i] < a[l]: 
        largest = l 
    if r < n and a[largest] < a[r]: 
        largest = r 
    if largest != i: 
        a[i],a[largest] = a[largest],a[i]  
        heapify(a, n, largest) 
   
def heapSort(a): 
    n = len(a)  
    for i in range(n, -1, -1): 
        heapify(a, n, i) 
    for i in range(n-1, 0, -1): 
        a[i], a[0] = a[0], a[i]   
        heapify(a, i, 0)            
    return a        


print (heapSort(a))            
            
            