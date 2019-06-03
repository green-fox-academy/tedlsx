# Students
from collections import namedtuple
from functools import reduce

Person = namedtuple("person", "name age gender grades")

p1 = Person(name="John", age=16, gender= "male", grades = [5,5,4,2])
p2 = Person(name="Jane", age=15, gender= "female", grades = [4,3,4,4,5])
p3 = Person(name="Bob", age=17, gender= "male", grades = [2,2,3,1])
##### boy list
bot_list = []
def gen(x):
    if x.gender == "male":
        return x
    else:
        pass

my_list = [p1, p2, p3]
boy_list = list(filter(gen, my_list))
print(boy_list)


import itertools
print(itertools.groupby(my_list, gen))

# name start with j 
def name_J(x):
    if x.name[0] == "J":
        return x
    else:
        pass

people_J_list = list(filter(name_J, my_list))
print(people_J_list)

#gilrs
def gilrs(x):
    if x.gender == "female":
        return x
    else:
        pass
gilrs_list = list(filter(gilrs, my_list))
print(gilrs_list)

#average grad above 4
def average_grad_above_4(x):
    if reduce(lambda a, b: a + b, x.grades) / len(x.grades) > 4:
        return x

grade_above_4_list = list(filter(average_grad_above_4, my_list))
print(grade_above_4_list)

#boy name start with J
def boy_name_J(x):
    if x.gender == "male" and x.name[0] == "J":
        return x
    else:
        pass

boy_name_J_list = list(filter(boy_name_J, my_list))
print(boy_name_J_list)

#gilrs who grade above 4
def girl_grade_above_4(x):
    if x.gender == "female" and reduce(lambda a, b: a + b, x.grades) / len(x.grades) > 4:
        return x
    else:
        pass

girl_grade_above_4_list = list(filter(girl_grade_above_4, my_list))
print(girl_grade_above_4_list)

# at least two 5s
def least_two_5(x):
    if len(list(filter(lambda x: x == 5, x.grades))) >= 2:
        return x
    else:
        pass

least_two_5_list = list(filter(least_two_5, my_list))
print(least_two_5_list)

# grade average is above 4 and at at least got two 5s
def above_4_least_2_5s(x):
    if reduce(lambda a, b: a + b, x.grades) / len(x.grades) > 4 and len(list(filter(lambda x: x == 5, x.grades))) >= 2:
        return x
    else:
        pass

above_4_least_2_5s_list = list(filter(above_4_least_2_5s, my_list))
print(above_4_least_2_5s_list)