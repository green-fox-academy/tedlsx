#Given a string, compute recursively a new string where all the adjacent chars are now separated by a *

def str_again_again(word):
    if len(word) == 1:
        return word[-1]
    else:
        return word[0] + "*" + str_again_again(word[1:])
    
print(str_again_again("axe"))