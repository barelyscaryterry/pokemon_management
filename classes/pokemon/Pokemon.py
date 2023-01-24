from classes.util.PokeData import PokeData

class Pokemon:
    def __init__(self, name):
        super().__init__()
        dataset = PokeData()
        pk_stats = dataset.fetch_data(name)
        for key, value in pk_stats.items():
            if key in ['Number', 'Total', 'HP', 'Attack', 'Defense', 'SpAtk', 'SpDef', 'Speed', 'Generation']:
                value = int(value)
            setattr(self, key, value)
        self.nature = ""
        self.ability = ""
        self.nick = ""
        self.held_item = ""
        self.weight = ""
        self.height = ""
        self.base_happiness = ""
        self.moves = []
        self.level = "1"
        self.Name = self.Name.replace("'", "")
        self.img = f"images\\sprites\\{self.Name.lower()}.png"
