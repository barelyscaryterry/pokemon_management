import PyQt5.QtWidgets as qtw
from random_poke import RandomPokemonWindow
# use classes in pyqt5

class MainWindow(qtw.QWidget):
    # Just some init jargon junk
    
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Pokemon Manager")
        self.setLayout(qtw.QHBoxLayout())
        tabs = qtw.QTabWidget()
        tabs.addTab(RandomPokemonWindow(), "Random Pokemon")
        self.layout().addWidget(tabs)
        
        self.show()
app = qtw.QApplication([])

mw = MainWindow()

# Run app

app.exec_()