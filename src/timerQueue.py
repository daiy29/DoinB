from conversion import msToTime

class timerQueue:
    def __init__(self, champions, spell, time):
        self.champions = champions
        self.spell = spell
        self.time = time
    
    def getChampions(self):
        return self.champions
    
    def setChampions(self,x):
        self.champions = x
    
    def getSpells(self):
        return self.spell
    
    def setSpells(self, x):
        self.spell = x
    
    def getTimes(self):
        return self.time
    
    def setTimes(self,x):
        self.time = x
    
    def appendChampions(self,x):
        self.champions.append(x)
    
    def appendSpell(self,x):
        self.spell.append(x)
    
    def appendTime(self,x):
        self.time.append(x)
    
    def popQueue(self):
        self.champions.pop(0) 
        self.spell.pop(0)
        self.time.pop(0)
    
    def removeFromQueue(self,x):
        self.champions.pop(x)
        self.spell.pop(x)
        self.time.pop(x)
    
    def timeCollector(self, x):
        for times in range(0,len(self.time)):
            if self.time[times] <= x:
                self.time.pop(times)
                self.champions.pop(times)
                self.spell.pop(times)

    def toStr(self):
        myStr = []
        for entry in range(0,len(self.time)):
            myStr.append("%s %s %s"%(self.champions[entry],self.spell[entry],msToTime(self.time[entry])))
        listToStr = ' '.join(map(str, myStr))
        return listToStr
