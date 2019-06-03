a = 0 

def increment(amount):
    global a
    a = a + 1
    print(a)

increment(1)
increment(1)

from collections import namedtuple

Person = namedtuple('Person', 'name age')

p1 = Person(name="John", age=10)
print(p1)
# p1.name = "Bob"
# p2 = Person(naem="Bob", age=24)


def pure_increment(input, amount):
    return input + amount

from collections import namedtuple

Person = namedtuple("Person", "name age")


numbers = [1, 2, 3, 4, 5]

def bigger_than_3(n):
    return n > 3

bigger_numbers = filter(bigger_than_3, numbers)

print(numbers)
print(type(bigger_numbers))

bigger_numbers = filter(lambda n: n >3, numbers)
