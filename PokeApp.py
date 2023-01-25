import PyQt5.QtWidgets as qtw
from classes.pokemon.random_poke import RandomPokemonWindow
from classes.box.searchWindow import SearchWindow
# use classes in pyqt5

class MainWindow(qtw.QWidget):
    # Just some init jargon junk
    
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Pokemon Manager")
        self.setLayout(qtw.QHBoxLayout())
        tabs = qtw.QTabWidget()
        tabs.addTab(RandomPokemonWindow(), "Random Pokemon")
        tabs.addTab(SearchWindow(), "Search")
        self.layout().addWidget(tabs)
        
        self.show()
app = qtw.QApplication([])

mw = MainWindow()

# Run app

app.exec_()