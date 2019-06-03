import itertools
def foreach(fun, my_list):
    for i in my_list:
        fun(i)
    
# def foreach(fun, my_list):
#     itertools.groupby(my_list, fun) 

