class PersonalComputer:   #最初は大文字
    def __init__(self, ram, storage):
        self.ram = ram
        self.storage = storage

    
    def ram_expansion(self,a):
         self.ram += a


pc = PersonalComputer(8, 128)
pc.ram_expansion(8)
print(pc.ram)
