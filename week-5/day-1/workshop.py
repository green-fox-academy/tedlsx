# even number
my_list = [1, 3, -2, -4, -7, -3, -8, 12, 19, 6, 9, 10, 14]

even_list = filter(lambda x: x % 2 == 0 and x > 0, my_list)

print(list(even_list))

# squard value
postive_value = filter(lambda x: x > 0, my_list )
squard_value = map(lambda x: x ** 2, postive_value)
print(list(squard_value))

# squard above 20
squard_20 = filter(lambda x : x ** 2 > 20, my_list)
print(list(squard_20))

# Calculate the average of the odd numbers.
odd_num = filter(lambda x: x % 2 == 1 and x > 0, my_list)
print(sum(list(odd_num)) / len(my_list))

# Calculate the sum of the even numbers which are below or equal to 10.
even_below10 = filter(lambda x: x % 2 == 0 and x  <= 10 and x > 0, my_list)
# print(sum(list(even_below10)))

from functools import reduce
even_below10_ave = reduce(lambda x, y: x + y, even_below10)
print(even_below10_ave)

# Determine whether it contains even numbers or not using any().
def any(my_list):
    return list(filter(lambda x: x % 2 == 0 and x > 0, my_list)) is not None

print(any(my_list))

# Determine whether every number is positive or not using all().
def all(my_list):
    return list(filter(lambda x: x < 0, my_list)) is None 

print(all(my_list))

