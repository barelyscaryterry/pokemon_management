import PyQt5.QtWidgets as qtw
import PyQt5.QtGui as qtg
import PyQt5.QtCore as qtc

class WBImages(qtw.QWidget):
    def __init__(self,img_link, size=None, hasBorder=False, parent=None):
        super().__init__(parent)
        layout = qtw.QVBoxLayout()
        layout.setAlignment(qtc.Qt.AlignmentFlag.AlignCenter)
        layout.setAlignment(qtc.Qt.AlignmentFlag.AlignHCenter)
        pic_label = qtw.QLabel()
        pic_label.setPixmap(qtg.QPixmap(img_link))
        pic_label.setAlignment(qtc.Qt.AlignmentFlag.AlignCenter)
        pic_label.setAlignment(qtc.Qt.AlignmentFlag.AlignHCenter)
        pic_label.setScaledContents(True)
        if (size != None):
            pic_label.setFixedSize(size, size)
        if (hasBorder == True):
            pic_label.setStyleSheet("""
                QLabel {
                    border: 1px solid gray;
                    border-radius: 5px;
                }
            """)
        layout.addWidget(pic_label)
        self.setLayout(layout)
