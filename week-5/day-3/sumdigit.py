#Given a non-negative integer n, return the sum of its digits recursively (without loops).

def sum_dig(n):
    if n == 0:
        return 0
    else:
        last_dig = n % 10
        return last_dig + sum_dig(n // 10)

print(sum_dig(123))