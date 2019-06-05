#Given a string, compute recursively a new string where all the 'x' chars have been removed.

def str_again(word):
    if len(word) == 1:
        return word[-1]
    else:
        if word[0] == "x":
            return str_again(word[1:])
        else:
            return word[0] + str_again(word[1:])

print(str_again("axe")) 