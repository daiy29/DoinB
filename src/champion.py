class Champion:
    def __init__(self, name, haste, summonerspells):
        self.name = name
        self.haste = haste
        self.summonerspells = summonerspells
    
    def set_name(self, x):
        self.name = x
    
    def set_haste(self,x):
        self.haste = x
    
    def set_summonerspells(self,x):
        self.summonerspells = x
    
    def get_name(self):
        return self.name
    
    def get_haste(self):
        return self.haste
    
    def get_summonerspells(self):
        return self.summonerspells
