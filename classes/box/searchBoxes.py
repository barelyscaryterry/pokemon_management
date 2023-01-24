import PyQt5.QtWidgets as qtw
from classes.util.PokeData import PokeData
from classes.pokemon.Pokemon import Pokemon
from classes.util.WBImages import WBImages

class SearchBoxes(qtw.QWidget):
    def __init__(self, name = ""):
        super().__init__()
        self.db = PokeData()
        self.on_add_clicked = ""
        self.name = name
        self.mon = Pokemon(self.name)
        name_label = qtw.QLabel(self.name)
        wbimg = WBImages(self.mon.img, 70, True)
        add_button = qtw.QPushButton("Add")
        add_button.connect(self.add_btn_clicked())
        my_layout = qtw.QVBoxLayout()
        my_layout.addWidget(name_label)
        my_layout.addWidget(wbimg)
        my_layout.addWidget(add_button)
        self.setLayout(my_layout)
    def add_btn_clicked(self):
        if self.name == "":
            pass
        else:
            self.on_add_clicked = self.name
