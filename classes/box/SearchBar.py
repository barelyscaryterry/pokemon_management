from PyQt5 import QtWidgets
import PyQt5.QtGui as qtg
from classes.pokemon.Pokemon import Pokemon
from classes.util.WBImages import WBImages
from classes.pokemon.pokeCard import PokeCard
class SearchBar(QtWidgets.QWidget):
    def __init__(self, dataset = None):
        super().__init__()
        self.dataset = dataset
        self.query_results = []
        self.results_view = QtWidgets.QWidget()
        self.on_add_pressed = self.dataset["Chesnaught"]

        self.search_bar = QtWidgets.QLineEdit(self)
        self.search_bar.textChanged.connect(self.on_text_changed)

        self.query_copy = QtWidgets.QLabel("")
       
        self.layout = QtWidgets.QVBoxLayout(self)
        self.layout.addWidget(self.search_bar)
        self.showing_label = QtWidgets.QLabel("")
        self.showing_label.setFont(qtg.QFont("Helvetica", 20))
        self.layout.addWidget(self.showing_label)
        
    def on_text_changed(self, text):
        self.showing_label.setText(f"Showing results for '{text}': ")
        query = text.lower()
        
        self.query_results = [
            (name, self.dataset[name]) for name in self.dataset
            if query in name.lower()
        ]

        self.query_results = self.query_results[:10]
        self.layout.removeWidget(self.results_view)
        self.results_view.deleteLater()
        self.results_view = QtWidgets.QWidget()
        self.results_view.setFixedSize(500, 300)
        query_images_layout_first5 = QtWidgets.QGridLayout()
        
        if len(self.query_results) != 0 and query != "":
            for number in range(len(self.query_results)):
                if number > 4:
                    row = 1
                else :
                    row = 0
                pk = Pokemon(self.query_results[number][1])
                pokeimg = WBImages(pk.img, 70, True) #Where to swap in widget
                pokeimg.layout().addWidget(QtWidgets.QLabel(pk.Name))
                add_button = QtWidgets.QPushButton("Add")
                pokeimg.layout().addWidget(add_button) #show pokemon in detail (pokeCard)
                pokeimg.setFixedHeight(130)
                query_images_layout_first5.addWidget(pokeimg, row, number % 5)
        else:
            none_found = QtWidgets.QLabel(F"Nothing found for '{query}' ")
            if (query == ""):
                none_found.setText("Search for a Pokemon above!")
            query_images_layout_first5.addWidget(none_found)
            none_found.setFont(qtg.QFont("Helvetica", 20))
        
        self.results_view.setLayout(query_images_layout_first5)
        self.layout.addWidget(self.results_view)
    def open_pokecard(self, mon):
        self.on_add_pressed = mon
