import PyQt5.QtWidgets as qtw
from classes.util.PokeData import PokeData
from classes.pokemon.Pokemon import Pokemon
from classes.util.WBImages import WBImages

class SearchBoxes(qtw.QWidget):
    def __init__(self, name):
        super().__init__()
        if name == "":
            pass
        else:
            self.db = PokeData()
            self.on_add_clicked = name
            self.mon = Pokemon(name)
            name_label = qtw.QLabel(f"#{self.mon.Number} {name.capitalize()}")
            wbimg = WBImages(self.mon.img, 75, True)
            add_button = qtw.QPushButton("Add")
            self.setFixedSize(110, 150)
            my_layout = qtw.QVBoxLayout()
            my_layout.addWidget(name_label)
            my_layout.addWidget(wbimg)
            my_layout.addWidget(add_button)
            self.setLayout(my_layout)
