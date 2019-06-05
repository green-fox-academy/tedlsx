# Find the greatest common divisor of two numbers using recursion.
def great_common_divisor(a, b):
    r = a % b
    if r == 0:
        return a
    elif r == 1:
        return 1
    else:
        return great_common_divisor(b, r)

print(great_common_divisor(64, 18))

