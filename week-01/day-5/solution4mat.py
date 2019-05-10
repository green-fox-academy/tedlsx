# -*- coding: utf-8 -*-
"""
Created on Thu May  9 15:02:43 2019

@author: Ted_Liu
"""
## Add
x = [[12,7,3],
    [4 ,5,6],
    [7 ,8,9]]

y = [[5,8,1],
    [6,7,3],
    [4,5,9]]

result = [[0,0,0],
         [0,0,0],
         [0,0,0]]

for i in range(0 , len(x)):
    for j in range(0, len(x[0])):
        result[i][j] = x[i][j] + y[i][j]
        
print (result)
### sub
for i in range(0 , len(x)):
    for j in range(0, len(x[0])):
        result[i][j] = x[i][j] - y[i][j]
        
print (result)

### scalar multi
for i in range(0 , len(x)):
    for j in range(0, len(x[0])):
        result[i][j] = x[i][j] * y[i][j]
        
print (result)

# transposition
import numpy as np
d = np.zeros((len(x[0]) , len(x)))
print(d)
for i in range(0 , len(x)):
    for j in range(0, len(x[0])):   
        d[i][j] = x[j][i]
        
print (x)



## matrix multi
for i in range(0 , len(x)):
    for j in range(0, len(y[0])):
        for k in range(0, len(y)):
            result[i][j] += x[i][k]*y[k][j]

print(result)


### vertical flipping
for i in range(0, int(len(x)/2)):
    for j in range(0, len(x[0]) ):
        x[i][j] , x[len(x) - i - 1][j] = x[len(x) - i - 1 ][j] , x[i][j]
print (x)


#######3 Main anti-diagonal mirroring
for i in range(0 , len(x)):
    for j in range(0, len(x[0])):
        if i+j < len(x) -1:
            x[i][j] , x[len(x) - i - 1][j] = x[len(x) - i - 1 ][j] , x[i][j]        
print (x)



### horizontal flipping
for i in range(0, len(x)):
    for j in range(0, int(len(x[0])/2)):
        x[i][j] , x[i][len(x[0]) - j - 1] = x[i][len(x[0]) - j - 1] , x[i][j]
print (x)


### rotation  90 degree
result = np.zeros((len(x[0]) , len(x) ))
for i in range(0, len(x)):
    for j in range(0 , len(x[0])):
        result[i][j] = x[len(x) - j -1 ][i]
print (result)                























