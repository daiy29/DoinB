class Summoner:
    def __init__(self, name, summoner_id, haste, has_cosmic, has_ionians, summonerspells, team):
        self.name = name
        self.summoner_id = summoner_id
        self.haste = haste
        self.has_cosmic = has_cosmic
        self.has_ionians = has_ionians
        self.summonerspells = summonerspells
        self.team = team
    
    def set_name(self, x):
        self.name = x
    
    def set_haste(self,x):
        self.haste = x
    
    def set_summonerspells(self,x):
        self.summonerspells = x
    
    def set_cosmic(self, x):
        self.has_cosmic = x
    
    def set_ionians(self, x):
        self.has_ionians = x
    
    def set_team(self, x):
        self.team = x
    
    def get_name(self):
        return self.name
    
    def get_haste(self):
        return self.haste

    def get_cosmic(self):
        return self.has_cosmic
    
    def get_ionians(self):
        return self.has_ionians
    
    def get_summonerspells(self):
        return self.summonerspells
    
    def get_team(self):
        return self.team

    
