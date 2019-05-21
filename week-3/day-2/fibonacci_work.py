def fi():
    my_list = [0, 1]
    s1 = 0
    s2 = 1
    i = 0
    while i <10:
        s3 = s1 + s2
        my_list.append(s3)
        s1 = s2
        s2 = s3
        i += 1
    return my_list