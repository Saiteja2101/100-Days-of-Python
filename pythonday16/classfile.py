class Family:
    def __init__(self,name,wife,child1,child2):
        self.name = name
        self.wife = wife
        self.child1 = child1
        self.child2 = child2
    
    def familynames(self):
        print(f"Father_name: {self.name}\nMother_name: {self.wife}\nFirst_child_name: {self.child1}\nSecond_child_name: {self.child2}")
