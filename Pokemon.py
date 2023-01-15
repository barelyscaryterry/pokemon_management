class Pokemon:
    def __init__(self, data):
        super()
        for key, value in data.items():
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
        self.img = f"C:\\Users\\terre\\OneDrive\\Desktop\\workspace\\pokemon\\images\\{self.Name.lower()}.png"
