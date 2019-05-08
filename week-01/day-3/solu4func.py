
mylist = []

def subint(num , mylist):
    list_res =[]
    for i in mylist:
            inum = [int(j) for j in str(i)]
            if num in inum:
                list_res.append(mylist.index(i))
    return (list_res)      


subint(1,[1,11,34,52,61])
print(subint(9, [1, 11, 34, 52, 61]))




###

    
    