from PyQt5 import QtWidgets
from classes.Pokemon import Pokemon
from classes.WBImages import WBImages


class SearchBar(QtWidgets.QWidget):
    class SearchBoxes(QtWidgets.QWidget):

        def __init__(self, mon):
            super().__init__()
            self.mon = mon
            self.img = WBImages(self.mon.img, 50, True)
            self.add_button = QtWidgets.QPushButton("Add", self.img)
    def __init__(self, dataset = None):
        super().__init__()

        self.dataset = dataset
        self.query_results = []

        self.search_bar = QtWidgets.QLineEdit(self)
        self.search_bar.textChanged.connect(self.on_text_changed)

        
        results_widg = QtWidgets.QColumnView()
        self.results_layout = QtWidgets.QHBoxLayout()
        results_widg.setLayout(self.results_layout)
        

        layout = QtWidgets.QVBoxLayout(self)
        layout.addWidget(self.search_bar)
        

    def on_text_changed(self, text):
        query = text.lower()
        self.query_results = [
            (name, self.dataset[name]) for name in self.dataset
            if query in name.lower()
        ]
        self.query_results = self.query_results[:10]
        for name in self.query_results:
            pk = Pokemon(name[1])
            self.results_layout.addWidget(self.SearchBoxes(pk))
