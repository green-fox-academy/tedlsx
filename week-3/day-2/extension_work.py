def add(a, b):
    return a + b

def max_of_three(a, b, c):
    if a > b:
        if a > c:
                return a
        else:
                return c
    elif c < b:
        return b
    else:
        return c

import statistics

def median(pool):
    return statistics.median(pool)

def is_vovel(char):
    return char in ['a', 'u', 'o', 'e', 'i']

def translate(hungarian):
    teve = hungarian
    for char in teve:
        if is_vovel(char):
            teve = (char+'v'+char).join(teve.split(char))
    return teve
