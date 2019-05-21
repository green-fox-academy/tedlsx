def anagram(s1, s2):
    my_list1 = []
    my_list2 = []
    for i in s1:
        my_list1.append(i)

    for j in s2:
        my_list2.append(j)

    return sorted(my_list1) == sorted(my_list2)
