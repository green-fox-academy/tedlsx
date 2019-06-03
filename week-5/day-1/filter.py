def my_filter(fun, my_list):
    for i in my_list:
        if fun(i) == True:
            return i
        else:
            pass