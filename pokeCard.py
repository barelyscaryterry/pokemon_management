import PyQt5.QtGui as qtg
import PyQt5.QtWidgets as qtw

class PokeCard(qtw.QWidget):
    def __init__(self, pokemon, parent=None):
        super().__init__(parent)
        self.poke = pokemon

        layout = qtw.QVBoxLayout(self)
        layout.setContentsMargins(10,10,10,10)
        self.setStyleSheet("""
                    QWidget {
                        border: 1px solid gray;
                        border-radius: 5px;
                    }
            """)
        name_label = qtw.QLabel(self.poke.Name)
        

        layout.addWidget(name_label)

        picture_label = qtw.QLabel()
        picture_label.setPixmap(qtg.QPixmap(self.poke.img))
        picture_label.setStyleSheet("""
            QLabel {
                border: 1px solid gray;
                border-radius: 5px;
            }
        """)

        layout.addWidget(picture_label)

        moves_list = qtw.QListWidget()
        moves_list.addItems([
            "Waterfall",
            "Earthquake",
            "Sleep Powder",
            "Taunt"
        ])
        layout.addWidget(moves_list)
        self.setLayout(layout)

        remove_button = qtw.QPushButton("Remove")
        layout.addWidget(remove_button)
        remove_button.clicked.connect(self.remove_container)

    def remove_container(self):
        self.setParent(None)
        self.deleteLater()

