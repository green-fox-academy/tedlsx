class sweet:
    def __init__(self, a_type, price, sugar):
        self.a_type = a_type
        self.price = price
        self.sugar = sugar

class lollipop(sweet):
    def __init__(self, a_type = "lollipop", price = 10, sugar = 5):
        sweet.__init__(self, a_type, price, sugar)
        self.a_type = a_type
        self.price = price
        self.sugar = sugar

class candie(sweet):
    def __init__(self, a_type = "candie", price = 20, sugar = 10):
        sweet.__init__(self, a_type, price, sugar)
        self.a_type = a_type
        self.price = price
        self.sugar = sugar

class candyshop:
    def __init__(self, sugar, income, inventory):
        self.sugar = sugar
        self.income = income
        self.inventory = inventory

    def creatSweet(self, a_type, price, Sweet):
        self.sugar -= Sweet
        self.inventory.append(sweet(a_type, price, sugar = Sweet))

    def raise_method(self, amount):
        for sweet in self.inventory:
            sweet.sugar += amount
        
    def sell(self, amount, a_type):
        if a_type == "lollipop":
            self.income += amount * 10
            while amount > 0:
                for sweet in self.inventory:
                    if sweet.__class__.__name__ == "lollipop":
                        self.inventory.remove(sweet)
                        amount -= 1
        else:
            self.income += amount * 20
            
            while amount > 0:
                for sweet in self.inventory:
                    if sweet.__class__.__name__ == "candie":
                        self.inventory.remove(sweet)
                        amount -= 1

    def buySugar(self, amount):
        self.sugar += amount
        self.income -= amount * 100 / 1000
        if self.income < 0:
            return "can not buy these sugar"

    def tostring(self):
        my_list = []
        for sweet in self.inventory:
            my_list.append(sweet.__class__.__name__)
        candie_count = my_list.count("candie")
        lolli_count = my_list.count("lollipop")
        return f"Inventory: {candie_count} candies, {lolli_count} lollipops, Income: {self.income}, Sugar: {self.sugar}"
    
a = lollipop()
b = candie()       
test = candyshop(400, 0, [a,a,a,b,b])
test.raise_method(2)
test.sell(1, "candie")
test.income
test.sugar
test.tostring()


