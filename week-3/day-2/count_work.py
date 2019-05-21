def count_str(s):
    my_dic = {}
    for i in s:
        my_dic[i] = s.count(i)
    return my_dic

