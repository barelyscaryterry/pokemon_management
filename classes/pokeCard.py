import PyQt5.QtGui as qtg
import PyQt5.QtWidgets as qtw
import PyQt5.QtCore as qtc
from classes.WBImages import WBImages
#A container that displays the name, picture, and moves of a pokemon.  Used primarily in development
class PokeCard(qtw.QWidget):
    def __init__(self, pokemon, parent=None):
        super().__init__(parent)
        self.poke = pokemon

        layout = qtw.QVBoxLayout(self)
        layout.setAlignment(qtc.Qt.AlignmentFlag.AlignCenter)


        name_label = qtw.QLabel(f"No. {self.poke.Number}: {self.poke.Name}")
        name_label.setFont(qtg.QFont("Ariel", 12, 2))
        layout.addWidget(name_label)

        stat_img = qtw.QWidget()
        stats_img_layout = qtw.QHBoxLayout()
        stats_img_layout.setAlignment(qtc.Qt.AlignmentFlag.AlignCenter)
        stats_label = self.PokeCardIVs(self.poke)


        picture_label = WBImages(self.poke.img, 150, True)
        
        stats_img_layout.addWidget(stats_label)
        stats_img_layout.addWidget(picture_label)

        stat_img.setLayout(stats_img_layout)

        layout.addWidget(stat_img)

        
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
    
    class TypeImages(qtw.QWidget):
        def __init__(self, type1, type2=None, parent=None):
            super().__init__(parent)
            layout = qtw.QHBoxLayout()
            layout.setAlignment(qtc.Qt.AlignmentFlag.AlignHCenter)
            type1_label = WBImages(f"images\\sm_icon\\{type1}_sm_icon.png", 70)
            type2_label = WBImages(f"images\\sm_icon\\{type2}_sm_icon.png", 70)
            layout.addWidget(type1_label)
            if (type2 != ""):
                layout.addWidget(type2_label)
            self.setLayout(layout)

    class PokeCardIVs(qtw.QWidget):
        def __init__(self,poke):
            super().__init__()
            layout = qtw.QHBoxLayout()
            stats = ["Speed", "SpAtk", "SpDef", "Attack", "Defense", "HP"]
            for stat in stats:
                setattr(self, stat, getattr(poke, stat))
            poke_stat = ""
            IV_label = qtw.QLabel()
            for stat in stats:
                poke_stat += f"\n{stat}: \n{str(getattr(self, stat))}"
            IV_label.setText(poke_stat)
            layout.addWidget(IV_label)
            self.setLayout(layout)
            







