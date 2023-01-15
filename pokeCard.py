import PyQt5.QtGui as qtg
import PyQt5.QtWidgets as qtw
import PyQt5.QtCore as qtc
#A container that displays the name, picture, and moves of a pokemon.  Used primarily in development
class PokeCard(qtw.QWidget):
    def __init__(self, pokemon, parent=None):
        super().__init__(parent)
        self.poke = pokemon

        layout = qtw.QVBoxLayout(self)
        layout.setAlignment(qtc.Qt.AlignmentFlag.AlignHCenter)
        name_label = qtw.QLabel(f"#{self.poke.Number} - {self.poke.Name}")
        

        layout.addWidget(name_label)

        picture_label = qtw.QLabel()
        picture_label.setPixmap(qtg.QPixmap(self.poke.img))
        picture_label.setAlignment(qtc.Qt.AlignmentFlag.AlignHCenter)
        picture_label.setFixedSize(100,100)
        



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
        

        layout.setAlignment(qtc.Qt.AlignmentFlag.AlignHCenter)
        self.setLayout(layout)

        remove_button = qtw.QPushButton("Remove")
        layout.addWidget(remove_button)
        remove_button.clicked.connect(self.remove_container)

    def remove_container(self):
        self.setParent(None)
        self.deleteLater()

    class TypeImages(qtw.QWidget):
        def __init__(self, type1, type2=None, parent=None):
            super().__init__(parent)
            layout = qtw.QHBoxLayout()
            layout.setAlignment(qtc.Qt.AlignmentFlag.AlignHCenter)
            type1_img = qtg.QPixmap(f"images\\sm_icon\\{type1}_sm_icon.png")
            type2_img = qtg.QPixmap(f"images\\sm_icon\\{type2}_sm_icon.png")
            type1_label = qtw.QLabel()
            type2_label = qtw.QLabel()
            type1_label.setPixmap(type1_img)
            type2_label.setScaledContents(True)
            type2_label.setFixedSize(50, 50)
            type1_label.setScaledContents(True)
            type1_label.setFixedSize(50, 50)
            type2_label.setPixmap(type2_img)
            layout.addWidget(type1_label)
            if (type2 != ""):
                layout.addWidget(type2_label)
            self.setLayout(layout)





