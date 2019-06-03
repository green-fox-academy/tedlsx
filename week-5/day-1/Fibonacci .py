# a = 1
# b = 1

# def fibonacci():
#     global a, b
#     a, b = b, a + b
#     return b 

def fibonacci():
    a, b = 1, 1
    while True:
        a, b = b, a + b
        yield b

fi = fibonacci()
print(next(fi))
print(next(fi))
print(next(fi))
print(next(fi))
print(next(fi))