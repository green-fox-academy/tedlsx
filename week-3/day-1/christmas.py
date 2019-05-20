class kid:
    def __init__(self, name, age, is_good, is_happy = "not happy"):
        self.name = name
        self.age = age
        self.is_good = is_good
        self.is_happy = is_happy

    def get_gift(self):
        self.is_happy = "happy!"

    def introduction(self):
        return f"My name is {self.name}, I am {self.age} years old. I am {self.is_happy}"

class santa:
    def __init__(self, name, age, num_gifts = 100):
        self.name = name
        self.age = age
        self.num_gift = num_gift

    def introduction(self):
        return f"My name is {self.name}, I am {self.age} years old. I have {self.num_gift} gifts in my bag."

    def assign_gift(self, kid_list):
        total_gift = self.num_gift
        for kid in kid_list:
            if self.num_gift > 0:
                if kid.is_good == "good":
                    kid.get_gift()
                    self.num_gift -= 1
            else:
                return "no enough gifts"
        return total_gift - self.num_gift 

class school:
    def __init__(self, kid_list):
        self.kid_list = kid_list

    def enroll(self, name, age, is_good, is_happy = "not happy"):
        k = kid(name, age, is_good, is_happy)
        kid_list.append(k)

    def christmas(self, name, age, num_gifts = 100):
        s = santa(name, age, num_gifts = 100)
        s.assign_gift(self.kid_list)


