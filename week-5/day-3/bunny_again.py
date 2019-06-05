def bunny_again(n):
    if n == 0:
        return 0
    else:
        if n % 2 == 0:
            return 3 + bunny_again(n - 1)
        elif n % 2 == 1:
            return 2 + bunny_again(n - 1)

print(bunny_again(5))
