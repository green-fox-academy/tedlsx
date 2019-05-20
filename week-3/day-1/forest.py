class tree:
    def __init__(self, height = 0):
        self.height = height

    def irrigate(self):
        pass

    def getHeight(self):
        return self.height

class whitebarkPine(tree):
    def __init__(self, height):
        tree.__init__(self, height)
        self.height = height

    def irrigate(self):
        self.height += 2

class foxtailPine(tree):
    def __init__(self, height):
        tree.__init__(self, height)
        self.height = height

    def irrigate(self):
        self.height += 1

class lumberjack:
    def __init__(self):
        pass

    def canCut(tree):
        return tree.height > 4

class forest():
    def __init__(self, tree_list):
        self.tree_list = tree_list

    def rain(self):
        for tree in self.tree_list:
            tree.irrigate()

    def cutTrees(lumberjack):
        for tree in self.tree_list:
            if tree.canCut():
                self.tree_list.remove(tree)
    
    def isEmpty(self):
        return  len(self.tree_list) == 0

    def getStatus(self):
        for tree in self.tree_list:
            print(f"There is a {tree.height} tall {tree.__class__.__name__} in the forest.")

    
a = whitebarkPine(10)
b = foxtailPine(15)

test = forest([a,b])
test.getStatus()