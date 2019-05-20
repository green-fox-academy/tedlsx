########### Bank account

class currency:
    def __init__(self, code, name, value):
        self.code = code
        self.name = name
        self.value = value

class USADollar(currency):
    def __init__(self, code = "USD", name = "Federal Reserve System", value = 0):
        currency.__init__(self, code, name, value)
        self.code = code
        self.name = name
        self.value = value

class HungarianForint(currency):
    def __init__(self, code = "HUF", name = "Hungarian National Bank", value = 0):
        currency.__init__(self, code, name, value)
        self.code = code
        self.name = name
        self.value = value

class bankaccount():
    def __init__(self, code, name, value):
        self.code = code
        self.name = name
        self.value = value

    def deposit(self, amount):
        if amount > 0:
            self.value += amount
        
    def withdraw(self, code, amount):
        if code == self.code:
            if amount <= self.value:
                self.value -= amount
                return self.value
            else:
                return 0
        else:
            return 0


class bank():
    def __init__(self, BankAccount_list):
        self.BankAccount_list = BankAccount_list

    def createAccount(self, BankAccount):
        self.BankAccount_list.append(BankAccount)

    def getAllMoney(self):
        sum_value = 0
        for bankaccount in self.BankAccount_list:
            sum_value += bankaccount.value
        return sum_value 

a = USADollar(value=1000)
b = HungarianForint(value=500)

test = bank([a,b])
test.getAllMoney()

