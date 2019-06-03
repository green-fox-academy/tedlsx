def fizz_buzz():
    x = 0
    while True:
        x += 1
        if x % 3 == 0 and x % 5 == 0:
            yield "fizz and buzz"
        elif x % 3 == 0:
            yield "fizz"
        elif x% 5 == 0:
            yield "buzz"
        else:
            yield x

fb = fizz_buzz()
print(next(fb))
print(next(fb))
print(next(fb))
