from classes.util.PokeData import PokeData

class Pokemon:
    def __init__(self, name):
        super().__init__()
        dataset = PokeData()
        pk_stats = dataset.fetch_data(name)
        for key, value in pk_stats.items():
            if key in ['#', 'Total', 'HP', 'Attack', 'Defense', 'Sp. Atk', 'Sp. Def', 'Speed', 'Generation']:
                if key == '#':
                    key = 'Number'
                elif key == 'Sp. Atk':
                    key = 'SpAtk'
                elif key == 'Sp. Def':
                    key = 'SpDef'
                value = int(value)
            if key == "Type 1":
                key = "Type1"
            elif key == "Type 2":
                key = "Type2"
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
        self.Name = name.replace("'", "")
        self.img = f"images\\sprites\\{self.Name.lower()}.png"
