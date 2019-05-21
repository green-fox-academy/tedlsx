class cow:
    def __init__(self, state = "playing", num = ""):
        self.state = state
        self.num = num
        
    def guess(self, my_num = ""):
        c1 = 0
        c2 = 0
        for i in range(0, 4):
            if my_num[i] == self.num[i]:
                c1 += 1
                if c1 == 4:
                    self.state = "finished"
                    return self.state
                else:
                    pass
                     
            elif my_num[i] != self.num[i] and my_num[i] in self.num:
                c2 += 1
        
        return f"{c1} cow, {c2} bull"
        
a = cow(num="1234")

a.guess("1432")