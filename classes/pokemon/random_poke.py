import PyQt5.QtWidgets as qtw
import PyQt5.QtGui as qtg
from classes.pokemon.Pokemon import Pokemon
from classes.util.PokeData import PokeData
import random
from classes.pokemon.pokeCard import PokeCard
# use classes in pyqt5
class RandomPokemonWindow(qtw.QWidget):
    
    def __init__(self):
        self.db = PokeData()
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
            random_mon = random.choice(self.db.fetch_keys())
            poke_container = PokeCard(random_mon)
           
            
            self.layout().addWidget(poke_container)

        self.layout().addWidget(my_btn)

# Run app
