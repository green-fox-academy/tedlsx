class fish:
    def __init__(self, name, weight, color, short_memory):
        self.name = name 
        self.weight = weight
        self.color = color
        self.short_memory = short_memory

    def status(self):
        print(f" {self.name}, weight: {self.weight}, color: {self.color}, short-term memory loss: {self.short_memory}")

    def feed(self):
        pass

class clownfish(fish):
    def __init__(self, name, weight, color):
        fish.__init__(self, name, weight, color)
        self.name = name
        self.weight = weight
        self.color = color

    def feed(self):
        self.weight += 1
        self.color = "blue"

class tang(fish):
    def __init__(self, name, weight, color):
        fish.__init__(self, name, weight, color)
        self.name = name
        self.weight = weight
        self.color = color

    def feed(self):
        self.weight += 1
        self.short_memory = True


class kong(fish):
    def __init__(self, name, weight, color):
        fish.__init__(self, name, weight, color)
        self.name = name
        self.weight = weight
        self.color = color

    def feed(self):
        self.weight += 2
        

class aquarium:
    def __init__(self, fish_list):
        self.fish_list = fish_list

    def feedall(self):
        for fish in self.fish_list:
            fish.feed()

    def remove(self):
        for fish in self.fish_list:
            if fish.weight >= 11:
                self.fish_list.remove(fish)
    
    def statusall(self):
        for fish in self.fish_list:
            fish.status()