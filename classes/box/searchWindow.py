import PyQt5.QtWidgets as qtw
import PyQt5.QtGui as qtg
from classes.util.PokeData import PokeData
from classes.box.searchBoxes import SearchBoxes
from classes.pokemon.pokeCard import PokeCard
from classes.pokemon.Pokemon import Pokemon
from classes.util.WBImages import WBImages
class SearchWindow(qtw.QWidget):
    def __init__(self):
        super().__init__()
        self.searchBar = self.SearchBar()
        self.layout = qtw.QHBoxLayout()
        
        self.added_mons = ""
        self.card_widg = qtw.QWidget()
        self.card = qtw.QVBoxLayout()
        self.card_widg.setLayout(self.card)
        self.layout.addWidget(self.searchBar)
        self.layout.addWidget(qtw.QLabel(self.searchBar))
        self.layout.addWidget(self.card_widg)
        self.setLayout(self.layout)
    class SearchBar(qtw.QWidget):
        def __init__(self):
            super().__init__()
            self.data = PokeData()
            self.dataset = self.data.fetch_keys()
            self.query_results = []
            self.results_view = qtw.QWidget()
        

            self.search_bar = qtw.QLineEdit(self)
            self.search_bar.textChanged.connect(self.on_text_changed)

            self.query_copy = qtw.QLabel("")
        
            self.layout = qtw.QVBoxLayout(self)
            self.layout.addWidget(self.search_bar)
            self.showing_label = qtw.QLabel("")
            self.showing_label.setFont(qtg.QFont("Helvetica", 20))
            self.layout.addWidget(self.showing_label)
            
        def on_text_changed(self, text):
            self.showing_label.setText(f"Showing results for '{text}': ")
            query = text.lower()
            
            self.query_results = list(filter(lambda x: query in x, self.dataset))

            self.query_results = self.query_results[:10]
            self.layout.removeWidget(self.results_view)
            self.results_view.deleteLater()
            self.results_view = qtw.QWidget()
            self.results_view.setFixedSize(500, 300)
            query_images_layout_first5 = qtw.QGridLayout()
            
            if len(self.query_results) != 0 and query != "":
                for number in range(len(self.query_results)):
                    if number > 4:
                        row = 1
                    else :
                        row = 0
                    pname = self.query_results[number]
                    sb = SearchBoxes(pname)
                    query_images_layout_first5.addWidget(sb, row, number % 5)
            else:
                none_found = qtw.QLabel(F"Nothing found for '{query}' ")
                if (query == ""):
                    none_found.setText("Search for a Pokemon above!")
                query_images_layout_first5.addWidget(none_found)
                none_found.setFont(qtg.QFont("Helvetica", 20))
            
            self.results_view.setLayout(query_images_layout_first5)
            self.layout.addWidget(self.results_view)
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
                add_button.clicked.connect(self.on_add_clicked(name))
                self.setFixedSize(110, 150)
                my_layout = qtw.QVBoxLayout()
                my_layout.addWidget(name_label)
                my_layout.addWidget(wbimg)
                my_layout.addWidget(add_button)
                self.setLayout(my_layout)
    def on_add_button_clicked(self, name):
        self.card_widg.deleteLater()
        self.card_widg = qtw.QWidget()
        layout = qtw.QVBoxLayout()
        layout.addWidget(PokeCard(name))
        self.card_widg.setLayout(layout)

    


