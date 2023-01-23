import PyQt5.QtWidgets as qtw
from classes.box.SearchBar import SearchBar
from classes.pokemon.pokeCard import PokeCard
from classes.pokemon.Pokemon import Pokemon
class SearchWindow(qtw.QWidget):
    def __init__(self, db):
        super().__init__()
        self.searchBar = SearchBar(db)
        self.layout = qtw.QHBoxLayout()
        self.layout.addWidget(self.searchBar)
        self.layout.addWidget(PokeCard(Pokemon(self.searchBar.on_add_pressed)))
        self.setLayout(self.layout)

