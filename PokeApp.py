import PyQt5.QtWidgets as qtw
from classes.random_poke import RandomPokemonWindow
from box.SearchBar import SearchBar
import csv
# use classes in pyqt5

class MainWindow(qtw.QWidget):
    # Just some init jargon junk
    def init_db(self):
        clean_data = {}
        file = open("dataset\pokemon_csv.csv")
        db = csv.DictReader(file, ["Number", "Name","Type1","Type2","Total","HP","Attack","Defense","SpAtk","SpDef","Speed","Generation","Legendary"])
        for row in db:
            if (row["Name"] == "Name" or len(row["Name"].split()) > 1):
                continue
            else:
                clean_data[row["Name"]] = row
        return clean_data
    
    def __init__(self):
        super().__init__()
        self.db = self.init_db()
        self.setWindowTitle("Pokemon Manager")
        self.setLayout(qtw.QHBoxLayout())
        tabs = qtw.QTabWidget()
        tabs.addTab(RandomPokemonWindow(), "Random Pokemon")
        tabs.addTab(SearchBar(self.db), "Search")
        self.layout().addWidget(tabs)
        
        self.show()
app = qtw.QApplication([])

mw = MainWindow()

# Run app

app.exec_()