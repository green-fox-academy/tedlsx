#Write a recursive function that takes one parameter: n and adds numbers from 1 to n.
def num_add(n, a):
    if n >= 1:
        num_add(n - 1, a)
        print(n + a)
 
print(num_add(5, 5))

#Given a non-negative integer n, return the sum of its digits recursively (without loops).

def sum_dig(n):
    if n == 0:
        return 0
    else:
        last_dig = n % 10
        return last_dig + sum_dig(n // 10)

print(sum_dig(123))

#Given base and n that are both 1 or more, compute recursively (no loops) the value of base to the n power, so powerN(3, 2) is 9 (3 squared).
def powerN(n, p):
    if p == 0:
        return 1
    else:
        return n * powerN(n, p - 1)

print(powerN(2, 3))
        
# Find the greatest common divisor of two numbers using recursion.
def great_common_divisor(a, b):
    if b == 0:
        return a
    else:
        return great_common_divisor(a, a % b)

print(great_common_divisor(3, 4))

