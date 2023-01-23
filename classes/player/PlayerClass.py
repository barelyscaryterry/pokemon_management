from classes.pokemon.Pokemon import Pokemon

class Player:
    def __init__(self) -> None:
        self.Name = "" #unchangeable?
        self.xp = 0 #will likely be implemented later along with locked items in shop
        self.gym_type = "" #chosen at begining of game
        self.lvl = 0 #up to 100
        self.team = self.PlayerTeam() #max length of six
        self.inventory = []
    class PlayerTeam:
        def __init__(self):
            super().__init__()
            self.mons = []
        def remove_mon(self, pos = 0):
            self.mons[pos] = ""
        def add_mon(self, mon, pos=0):
            if self.mons[pos] == "":
                self.mons[pos] = mon
            elif len(self.mons) < 6:
                self.mons.append(mon)
            else:
                print("not ready yet!")
            
