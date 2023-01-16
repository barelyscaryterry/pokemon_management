import PyQt5.QtGui as qtg
import PyQt5.QtWidgets as qtw
import PyQt5.QtCore as qtc
from WBImages import WBImages
#A container that displays the name, picture, and moves of a pokemon.  Used primarily in development
class PokeCard(qtw.QWidget):
    def __init__(self, pokemon, parent=None):
        super().__init__(parent)
        self.poke = pokemon

        layout = qtw.QVBoxLayout(self)
        layout.setAlignment(qtc.Qt.AlignmentFlag.AlignCenter)


        name_label = qtw.QLabel(f"No. {self.poke.Number}: {self.poke.Name}")
        name_label.setFont(qtg.QFont("Ariel", 14, 2))
        layout.addWidget(name_label)


        picture_label = WBImages(self.poke.img, 100, True)
        layout.addWidget(picture_label)
        
        types = self.TypeImages(self.poke.Type1, self.poke.Type2)
        layout.addWidget(types)


        moves_list = qtw.QListWidget()
        moves_list.addItems([
            "Waterfall",
            "Earthquake",
            "Sleep Powder",
            "Taunt"
        ])
        layout.addWidget(moves_list)
        
        remove_button = qtw.QPushButton("Remove")
        layout.addWidget(remove_button)
        remove_button.clicked.connect(self.remove_container)

        layout.setAlignment(qtc.Qt.AlignmentFlag.AlignHCenter)
        self.setLayout(layout)

       

    def remove_container(self):
        self.setParent(None)
        self.deleteLater()
    
    class IVStats(qtw.QWidget):
        def __init__(self, parents = None):
            super().__init__(parents)


    class TypeImages(qtw.QWidget):
        def __init__(self, type1, type2=None, parent=None):
            super().__init__(parent)
            layout = qtw.QHBoxLayout()
            layout.setAlignment(qtc.Qt.AlignmentFlag.AlignHCenter)
            type1_label = WBImages(f"images\\sm_icon\\{type1}_sm_icon.png", 50)
            type2_label = WBImages(f"images\\sm_icon\\{type2}_sm_icon.png", 50)
            layout.addWidget(type1_label)
            if (type2 != ""):
                layout.addWidget(type2_label)
            self.setLayout(layout)





