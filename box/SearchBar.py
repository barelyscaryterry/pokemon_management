from PyQt5 import QtWidgets
from classes.Pokemon import Pokemon
from classes.WBImages import WBImages

class SearchBar(QtWidgets.QWidget):
    def __init__(self, dataset = None):
        super().__init__()
        self.dataset = dataset
        self.query_results = []
        self.results_view = QtWidgets.QWidget()

        self.search_bar = QtWidgets.QLineEdit(self)
        self.search_bar.textChanged.connect(self.on_text_changed)
       
        self.layout = QtWidgets.QVBoxLayout(self)
        self.layout.addWidget(self.search_bar)
        

    def on_text_changed(self, text):
       
        query = text.lower()
        self.query_results = [
            (name, self.dataset[name]) for name in self.dataset
            if query in name.lower()
        ]

        self.query_results = self.query_results[:10]
        self.layout.removeWidget(self.results_view)
        self.results_view.deleteLater()
        self.results_view = QtWidgets.QWidget()
        query_images_layout_first5 = QtWidgets.QHBoxLayout()
        
        if len(self.query_results) != 0:
            for name in self.query_results:
                pk = Pokemon(name[1])
                pokeimg = WBImages(pk.img, 70, True)
                query_images_layout_first5.addWidget(pokeimg)
        else:
            query_images_layout_first5.addWidget(QtWidgets.QLabel("None found"))
        
        self.results_view.setLayout(query_images_layout_first5)
        self.layout.addWidget(self.results_view)
