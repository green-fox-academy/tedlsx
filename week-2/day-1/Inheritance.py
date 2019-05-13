# -*- coding: utf-8 -*-
"""
Created on Mon May 13 16:19:38 2019

@author: Ted_Liu
"""
## Person
class Person():
    def __init__(self, name = "Jane Doe", age = 30, gender = "female"):
        self.name = name
        self.age = age
        self.gender = gender
        
    def introduce(self):
        print ("Hi, I'm ", self.name, " a ", self.age, " year old ", self.gender)
        
    def get_goal(self):
        print ("My goal is: Live for the moment!" )
    



### Student

class Student(Person):
    def __init__(self, name = "Jane Doe", age = 30, gender = "female", previous_organization = "The School of life", skipped_days = 0):
        Person.__init__(self, name, age, gender)
            
        self.previous_organization = previous_organization
        self.skipped_days = skipped_days
        
    def get_goal(self):
        print("Be a junior software developer.")
        
    def introduce(self):
        print("Hi, I'm ", self.name, " a ", self.age, " year old ", self.gender, " from ", self.previous_organization, " who skipped ", self.skipped_days, " days from the course already")
        
    def skip_days(self, number_of_days):
        self.skipped_days += number_of_days
        

    
        
#########  Mentor        
        
class Mentor(Person):
    def __init__(self, name = "Jane Doe", age = 30, gender = "female", level = "intermediate"):
        Person.__init__(self,  name, age, gender)
        
        self.level = level
        
    def get_goal(self):
        print( "Educate brilliant junior software developers.")
        
    def introduce(self):
        print( "Hi, I'm ", self.name,  " a ", self.age, " year old ", self.gender, self.level, " mentor.")
        


####### Sponsor

class Sponsor(Person):
    def __init__(self, name = "Jane Doe", age = 30, gender = "female", company = "Google", hired_students = 0):
        Person.__init__(self,  name, age, gender)
        self.company = company
        self.hired_students = hired_students
        
    def introduce(self):
        print("Hi, I'm ", self.name, " a ", self.age, " year old ", self.gender, " who represents ", self.company, " and hired ", self.hired_students, " students so far.")

    def hire(self):
        self.hired_students += 1
        
        
    def get_goal(self):
        print("Hire brilliant junior software developers.")
            

        
## Cohort

class Cohort():
    def __init__(self, name, students = [], mentors = []):
        self.name = name
        self.students = students
        self.mentors = mentors
        
    def add_student(self, Student):
        self.students.append(Student)
        
    def info(self):
        print("The ", self.name, " cohort has ", len(self.students), " students and ", len(self.mentors), " mentors.")
        
        
# Test 
people = []

mark = Person('Mark', 46, 'male')
people.append(mark)
jane = Person()
people.append(jane)
john = Student('John Doe', 20, 'male', 'BME')
people.append(john)
student = Student()
people.append(student)
gandhi = Mentor('Gandhi', 148, 'male', 'senior')
people.append(gandhi)
mentor = Mentor()
people.append(mentor)
sponsor = Sponsor()
elon = Sponsor('Elon Musk', 46, 'male', 'SpaceX')
people.append(elon)
student.skip_days(3)

for i in range(5):
    elon.hire()

for i in range(3):
    sponsor.hire()

for person in people:
    person.introduce()
    person.get_goal()

      
        
        
        
# garden

class Garden():
    def __init__(self, flowers = ["yellow Flower ", "blue Flower "], trees = ["purple Tree", "orange Tree"], flowers_warter = [0, 0], trees_warter = [0, 0]):
        self.flowers = flowers
        self.trees = trees
        self.flowers_warter = flowers_warter
        self.trees_warter = trees_warter
        
    def check(self):
        for i in range(0,2):
            if self.flowers_warter[i] < 5 :
                print("The ", self.flowers[i], " needs warter")
            else:
                print("The ", self.flowers[i], " doesnt need water")
                
        for i in range(0,2):    
            if self.trees_warter[i] < 10 :
                print("The ", self.trees[i], " needs warter")
            else:
                print("The ", self.trees[i], " doesnt need water")
                
       
    def warter(self, amount):
        
        if self.flowers_warter[0] < 5 and self.trees_warter[0] < 10:    
            self.flowers_warter[0] += 0.75 * 0.25 * amount
            self.flowers_warter[1] += 0.75 * 0.25 * amount
            self.trees_warter[0] += 0.75 * 0.25 * amount
            self.trees_warter[1] += 0.75 * 0.25 * amount
            print ( self.flowers_warter, self.trees_warter)

        elif self.flowers_warter[0] >= 5 and self.trees_warter[0] < 10:            
             self.trees_warter[0] += 0.75 * 0.5 * amount
             self.trees_warter[1] += 0.75 * 0.5 * amount  
        print ("Wartering with ", amount)
        
        
garden = Garden()        
garden.check()        

garden.warter(40)
garden.check()        

garden.warter(70)
garden.check() 














