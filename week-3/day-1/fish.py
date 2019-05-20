class fish:
    def __init__(self, name, weight, color):
        self.name = name 
        self.weight = weight
        self.color = color
    
    def status(self):
        return f"{self.name}, weight: {self.weight}, color: {self.color}, short-term memory loss: true"

    def feed(self):
        pass

