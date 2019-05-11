# -*- coding: utf-8 -*-
"""
Created on Fri May 10 09:52:16 2019

@author: Ted_Liu
"""

### Post-it

class PostIt():
    background_color = ""
    text_color = ""
    text =""
    
p1 = PostIt()
p2 = PostIt()
p3 = PostIt()
    
p1.background_color = "orange"
p1.text = "Idea 1"
p1.text_color = "blue"
    
p2.background_color = "pink"
p2.text = "Awesome"
p2.text_color = "black"
    
p3.background_color = "yellow"
p3.text = "Superb!"
p3.text_color = "green"
    
print("a "+p1.background_color ,"with "+ p1.text_color +  "text: ",  '"%s"'%p1.text)
print("a "+p2.background_color ,"with "+ p2.text_color +  "text: ",  '"%s"'%p2.text)
print("a "+p3.background_color ,"with "+ p3.text_color +  "text: ",  '"%s"'%p3.text)

### Blogpost

class BlogPost():
    author_name =""
    title = ""
    text = ""
    publication_data = ""
    
bp1 = BlogPost()    
bp2 = BlogPost()    
bp3 = BlogPost()    

bp1.author_name = "John Doe" 
bp1.title = "Lorem Ipsum"
bp1.text = "Lorem ipsum dolor sit amet"
bp1.publication_data =   "2000.05.04."

bp2.author_name = "Tim Urban" 
bp2.title = "Wait but why"
bp2.text = "A popular long-form, stick-figure-illustrated blog about almost everything"
bp2.publication_data = "2010.10.10."
    
bp3.author_name =  "William Turton"   
bp3.title = "One Engineer Is Trying to Get IBM to Reckon With Trump"
bp3.text = "Daniel Hanley, a cybersecurity engineer at IBM, doesn’t want to be the center of attention. When I asked to take his picture outside one of IBM’s New York City offices, he told me that he wasn’t really into the whole organizer profile thing."
bp3.publication_data = "2017.03.28."

print ('"%s"'%bp1.title, "titled by "+bp1.author_name, "at "+'"%s"'%bp1.publication_data, "\n"+bp1.text   )   
print ('"%s"'%bp2.title, "titled by "+bp2.author_name, "at "+'"%s"'%bp2.publication_data, "\n"+bp2.text   )   
print ('"%s"'%bp3.title, "titled by "+bp3.author_name, "at "+'"%s"'%bp3.publication_data, "\n"+bp3.text   )   
    
    
 #### Animal
  
    
class Animal(object):
    def __init__(self, hunger=50, thirst=50):
        self.hunger = hunger
        self.thirst = thirst

    def eat(self):
        self.hunger -= 1
        return ("hunger is %d"%self.hunger)

    def drink(self):
        self.thirst -= 1
        return ("thirst is %d"%self.thirst)

    def play(self):
        self.hunger += 1
        self.thirst += 1
        return ("hunger is %d"%self.hunger, "thirst is %d"%self.thirst)

a = Animal()    
a.eat()
a.drink()
a.play()

# Sharpie


class Sharpie(object):
    def __init__(self, color="", width=0.0 , ink_amount = 100.0):
        self.color = color
        self.width = width
        self.ink_amount = ink_amount

    def use(self):
        self.ink_amount -= 1
        return ("amount of ink left is %d"%self.ink_amount)
    
a = Sharpie()
a.use()


####  Counter

class Counter(object):
    def __init__(self, int_num = 0 ):
        self.int_num = int_num
        self.int = int_num
    def add(self, number = 1):
        self.int_num += number
        return self.int_num
    def get(self):
        return self.int_num
    def reset(self):
        self.int_num = self.int
        return self.int_num

a = Counter(int_num = 1)    
a.add(2)    
a.add()
a.get()
a.reset()

### Test counter
import unittest

class TestCounter(unittest.TestCase):

    def setUp(self):
        self.c = Counter()

    def test_addMore(self):
        self.c.add(5)
        self.assertEqual(self.c.get(), 5)

    def test_addOne(self):
        self.c.add()
        self.assertEqual(self.c.get(), 1)

    def test_getZero(self):
        self.assertEqual(self.c.get(), 0)

    def test_getInit(self):
        c = Counter(7)
        self.assertEqual(c.get(), 7)

    def test_resetToZero(self):
        self.c.add()
        self.c.reset()
        self.assertEqual(self.c.get(), 0)

    def test_resetToInit(self):
        c = Counter(7)
        self.c.add(5)
        self.c.reset()
        self.assertEqual(c.get(), 7)

if __name__ == '__main__':
    unittest.main()   
    
    
######### Pokemon
global str
class Pokemon(object):
    def __init__(self, Name, Type, EffectiveAgainst):
        self.Name = str(Name)
        self.Type = str(Type)
        self.EffectiveAgainst = str(EffectiveAgainst)

    def Name(self):
        return self.Name

    def Type(self):
        return self.Type

    def EffectiveAgainst(self):
        return self.EffectiveAgainst
    
    def isEffectiveAgainst(self, anotherPokemon):
        return self.EffectiveAgainst == anotherPokemon.Type

def initializePokemons():
        pokemon = []
        pokemon.append(Pokemon("Balbasaur", "leaf", "water"))
        pokemon.append(Pokemon("Pikatchu", "electric", "water"))
        pokemon.append(Pokemon("Charizard", "fire", "leaf"))
        pokemon.append(Pokemon("Balbasaur", "water", "fire"))
        pokemon.append(Pokemon("Kingler", "water", "fire"))
        return pokemon
pokemon = initializePokemons()

# Every pokemon has a name and a type.
# Certain types are effective against others, e.g. water is effective against fire.
# Ash has a few pokemon.
# A wild pokemon appeared!
wildPokemon = Pokemon("Oddish", "leaf", "water")
# Which pokemon should Ash use?
for i in range(0,5):
    if pokemon[i].isEffectiveAgainst(wildPokemon) == True:
        print("I choose you, ", pokemon[i].Name)  



######### Fleet of things

class Fleet(object):
    def __init__(self):
        self.things = []
    def add(self, thing):
        self.things.append(thing)
    def __str__(self):
        result = ""
        for i in range(0, len(self.things)):
            result += str(i + 1) + ". " + self.things[i].__str__() + "\n"
        return result
    

class Thing:
    def __init__(self, name):
        self.name = name
        self.completed = False
    def complete(self):
        self.completed = True
    def __str__(self):
        return ("[x] " if self.completed else "[ ] ") + self.name
    


fleet = Fleet()
fleet.add(Thing("get milk"))
fleet.add("Remove the obstacles")
fleet.add("Stand up")
fleet.add("Eat lunch")

for i in range(0,len(fleet.things)):    
    print(type(fleet.things[i]))
    
    thing_name = str(fleet.things[i])
    print(thing_name)
    if fleet.things[i] == "Stand up" or "Eat lunch":
        thing = Thing(fleet.things[i])
        thing_reslut = thing.complete()
        print(thing_reslut)
        print(thing)
    else:
        print(thing)
# Create a fleet of things to have this output:

# 1. [ ] Get milk

# 2. [ ] Remove the obstacles

# 3. [x] Stand up

# 4. [x] Eat lunch

print(thing)

print(fleet)        

type(thing.name)

thing_reslut = thing.complete()
print(thing_reslut)
thing_str = thing_reslut.__str__
print(thing_str)
