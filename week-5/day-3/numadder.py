#Write a recursive function that takes one parameter: n and adds numbers from 1 to n.
def num_add(n, a):
    if n >= 1:
        num_add(n - 1, a)
        print(n + a)
 
print(num_add(5, 5))