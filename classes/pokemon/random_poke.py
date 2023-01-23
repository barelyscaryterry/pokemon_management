import PyQt5.QtWidgets as qtw
import PyQt5.QtGui as qtg
import classes.pokemon.Pokemon as pk
import csv
import random
from classes.pokemon.pokeCard import PokeCard
# use classes in pyqt5
def init_db():
        clean_data = {}
        file = open("dataset\pokemon_csv.csv")
        db = csv.DictReader(file, ["Number", "Name","Type1","Type2","Total","HP","Attack","Defense","SpAtk","SpDef","Speed","Generation","Legendary"])
        for row in db:
            if (row["Name"] == "Name" or len(row["Name"].split()) > 1):
                continue
            else:
                clean_data[row["Name"]] = row
        return clean_data
db = init_db()
class RandomPokemonWindow(qtw.QWidget):
    
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Pokedex")
        self.setLayout(qtw.QHBoxLayout())
        my_label = qtw.QLabel("Pokedex")
        my_label.setFont(qtg.QFont("Helvetica", 18))

        self.layout().addWidget(my_label)

        my_btn = qtw.QPushButton("Random Pokemon", 
            clicked = lambda: press_it())
        
        
        def press_it():
            # Add name to label
            random_mon = random.choice(list(db.keys()))
            mon = pk.Pokemon(db[random_mon])
            poke_container = PokeCard(mon)
           
            
            self.layout().addWidget(poke_container)

        self.layout().addWidget(my_btn)

# Run app
