import PyQt5.QtWidgets as qtw
from classes.box.SearchBar import SearchBar
from classes.pokemon.pokeCard import PokeCard
from classes.pokemon.Pokemon import Pokemon
class SearchWindow(qtw.QWidget):
    def __init__(self):
        super().__init__()
        self.searchBar = SearchBar()
        self.layout = qtw.QHBoxLayout()
        self.layout.addWidget(self.searchBar)
        self.layout.addWidget(qtw.QLabel(self.searchBar))
        self.setLayout(self.layout)


