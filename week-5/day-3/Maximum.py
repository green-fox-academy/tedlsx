#Write a function that finds the largest element of an array using recursion.

def max_find(n):
    if len(n) == 1:
        return n[0]
    else:
        if n[0] > n[1]:
            n[1] = n[0]
            return max_find(n[1:])
        else:
            return max_find(n[1:])
    # return max_find(n[1:])

print(max_find([2,3,5,1]))