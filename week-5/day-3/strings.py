#Given a string, compute recursively (no loops) a new string where all the lowercase 'x' chars have been changed to 'y' chars.

def string(word):
    if len(word) == 1:
        return word[-1]
    else:
        if word[0] == "x":
            return "y" + string(word[1:])
        else:
            return word[0] + string(word[1:]) 
    
print(string("axe"))
