# -*- coding: utf-8 -*-
"""
Created on Fri May 10 09:52:16 2019

@author: Ted_Liu
"""
import random
import unittest


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
fleet.add(Thing("Remove the obstacles"))
fleet.add(Thing("Stand up"))
fleet.add(Thing("Eat lunch"))

        
fleet.things[2].complete()       
fleet.things[3].complete()  
print(fleet)


# Create a fleet of things to have this output:

# 1. [ ] Get milk

# 2. [ ] Remove the obstacles

# 3. [x] Stand up

# 4. [x] Eat lunch

### DiceSet

class DiceSet(object):
    
    def __init__(self, dice_list = []):
        self.dice_list = dice_list
    
    def roll(self):
        for i in range(0,6):
            self.dice_list.append(random.randint(1,6))
        
    def get_current(self):
        return self.dice_list
    
    def reroll(self, which_dice):
            self.dice_list[which_dice] = random.randint(1,6)


Dice = DiceSet()    
Dice.roll()    
Dice.get_current()    
Dice.reroll(1)    
Dice.get_current()    

######### to roll all dices to 6
for i in range (0, 1000):
    current_dice = Dice.get_current()
    for j in range(0,6):
        if current_dice[j] != 6:
            Dice.reroll(j)
                
    
print (Dice.dice_list)   



#### Dominoes 

class Domino:
    num_1 = 0
    num_2 = 0
    def __init__(self, num_1, num_2):
        self.num_1 = num_1
        self.num_2 = num_2
        self.values = [num_1, num_2]
    def __repr__(self):
        return '[{}, {}]'.format(self.values[0], self.values[1])    
        

def initialize_dominoes():
    dominoes = []
    dominoes.append(Domino(5, 2))
    dominoes.append(Domino(4, 6))
    dominoes.append(Domino(1, 5))
    dominoes.append(Domino(6, 7))
    dominoes.append(Domino(2 ,4))
    dominoes.append(Domino(7, 1))
    return dominoes

dominoes = initialize_dominoes()        

print(dominoes)    
dominoes[6].num_1

my_domino = []
my_domino = [[5,2]]



for i in range(0, len(dominoes)):
    for j in range(1, len(dominoes)):
        if my_domino[i][1] == dominoes[j].num_1:
            my_domino += [[dominoes[j].num_1, dominoes[j].num_2]]
            
                
print (my_domino)    
    
###### complex 
###  Teacher Student

class Student:
    def learn(self):
        return "I have learned this method"
    def question(self, teacher):
        teacher.answer()
    
    
    
class Teacher:
    def teach(self, student):
        Student.learn()
    def answer(self):
        return "I am answing you"
        

student = Student()
teacher = Teacher()        

student.question(teacher)

#### Petrol station
        
class Station:
    def __init__(self, gas_amount):
        self.gas_amount = gas_amount
        
    def refill(self, car):
        car.capacity -= car.gas_amount
        car.gas_amount += 1


class Car:
    def __init__(self, gas_amount = 0, capacity = 100):
        self.gas_amount = gas_amount
        self.capacity = capacity
        
station = Station(20)        

car = Car()        

station.refill(car)        

print (car.gas_amount)        
        
        
#####   Sharpie Set

class SharpieSet:
    def __init__(self, sharpie_list = [0,1,0,2]):
        self.sharpie_list = sharpie_list
        
    def count_usable(self):
        for i in range(0, len(self.sharpie_list)):
            if self.sharpie_list[i] != 0:
                print("usable")
            else: 
                print("not usable")
                
        
    def remove_trash(self):
        count = 0
        for i in range(0, len(self.sharpie_list)):
            if self.sharpie_list[i] == 0:
                count += 1
        for i in range(0 ,count):
            self.sharpie_list.remove(0)                

sh = SharpieSet()        
sh.count_usable()        
sh.remove_trash()        
print(sh.sharpie_list)        


####      Farm

class Farm:
    def __init__(self, animal_list, slots):
        self.animal_list = animal_list
        self.slots = slots
        
    def breed(self):
        if self.slots != 0:
            pass

    def slaughter(self):
        for i in range(0, len(self.animal_list)):
            self.animal_list[i] = Animal()
            while self.animal_list[i].hunger == 0:
                del self.animal_list[i]


farm = Farm(["a","b"],2)

farm.slaughter()

BlogPost.author_name

##### Blog
class Blog:
    def __init__(self, blog_list = ["a", "b", "c"]):
        self.blog_list = blog_list
    def delete(self, int):
        del self.blog_list[int]
        
    def update(self, int, BlogPost):
        self.blog_list.insert(int, BlogPost)
        
        


### Pirates
        
class Pirate:
    def __init__(self, intoxicates = 0, state = "alive"):
        self.intoxicates = intoxicates 
        self.state = state
        
    def drink_some_rum(self):
        self.intoxicates += 1
        
    def hows_it_going_mate(self):
        if self.intoxicates <= 4:
            return "Pour me anudder!"
        else:
            return  "'Arghh, I'ma Pirate. How d'ya d'ink its goin?', the pirate passes out and sleeps it off"

    def die(self):
        self.state = "dead"
    
    def brawl(self, x):
        i = random.randint(1,3)
        if i == 1:
            self.die()
        elif i ==2:
            self.die()
            x.die()
        else:
            self.state = "pass out"
            x.state = "pass out"
        
        
##### Pirates place
            

class Ship:
    def __init__(self, state_list, pirate_list, captain_index):
        self.state_list = state_list
        self.pirate_list = pirate_list
        self.captain_index = captain_index
        
    def fill_ship(self):
        for i in random.randint(1,100):
            self.pirate_list.append(Pirate())
            print (i)

    def Score(self):
        count_pass_out = 0
        count_alive = 0
        for i in self.state_list:
            if i == "pass out":
                count_pass_out += 1
            elif i =="alive":
                count_alive += 1
        score = self.pirate_list[self.captain_index] + count_alive + count_pass_out
        return score
        
    def battle(self, otherShip):   
        if Ship.Score() > otherShip.Score():
             
            losser = otherShip
            
        else:
            
            losser = self
        
        losses = random.randint(0, len(self.Alive))
        losser.Alive -= losses
        win_rum = random.randint(0, 10)
        losser.pirate_list[self.captain_index] += win_rum    
            
        
        
        
### BattleApp
        
        
        
## Armada
        
## WarApp
    



























        



  
        
        
        
        
        
        
        

