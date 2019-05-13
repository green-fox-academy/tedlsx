# -*- coding: utf-8 -*-
"""
Created on Mon May 13 16:19:38 2019

@author: Ted_Liu
"""
## Person
class Person():
    def __init__(self, name, age, gender):
        self.name = name
        self.age = age
        self.gender = gender
        
    def introduce(self):
        print ("Hi, I'm ", self.name, " a ", self.age, " year old ", self.gender)
        
    def get_goal(self):
        print ("My goal is: Live for the moment!" )
    
p1 = Person("Jane Doe", 30, "female")

p1.get_goal()


### Student

class Student(Person):
    def __init__(self, name, age, gender, previous_organization, skipped_days):
        Person.__init_(self, name, age, gender)
            
        self.previous_organization = previous_organization
        self.skipped_days = skipped_days
        
    def get_goal(self):
        print("Be a junior software developer.")
        
    def introduce(self):
        print("Hi, I'm ", self.name, " a ", self.age, " year old ", self.gender, " from ", self.previous_organization, " who skipped ", self.skipped_days, " days from the course already")
        
    def skipped_days(number_of_days):
        self.skipped_days += self.num_of_days
        
    
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        