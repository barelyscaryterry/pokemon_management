import PyQt5.QtWidgets as qtw
import PyQt5.QtGui as qtg
import PyQt5.QtCore as qtc
from random_poke import RandomPokemonWindow
# use classes in pyqt5

class MainWindow(qtw.QWidget):
    # Just some init jargon junk
    
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Pokedex")
        self.setLayout(qtw.QHBoxLayout())
        self.random_pokemon_tab = RandomPokemonWindow()
        self.tabs = qtw.QTabWidget(self)
        self.tabs.addTab(qtw.QMainWindow(), "Welcome")
        self.welcome_label = qtw.QLabel("Welcome to the pokedex!")
        self.tabs.addTab(self.random_pokemon_tab, "Random Pokemon")
        self.layout().addWidget(self.tabs)
        
        self.show()
app = qtw.QApplication([])

mw = MainWindow()

# Run app

app.exec_()