class sharpie(object):
    def __init__(self, color="", width=0.0 , ink_amount = 100.0):
        self.color = color
        self.width = width
        self.ink_amount = ink_amount

    def use(self):
        self.ink_amount -= 1
        return ("amount of ink left is %d"%self.ink_amount)
    