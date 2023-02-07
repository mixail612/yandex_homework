from PyQt5.QtWidgets import QApplication, QMainWindow, QLabel
import sys
from PyQt5.QtCore import Qt
from utils import Map
from PyQt5 import uic
from PyQt5.QtGui import QPixmap


class Window(QMainWindow):
    def __init__(self):
        super().__init__()
        self._map = Map((37, 55), 10)
        # self._map_image = QLabel()
        uic.loadUi('window.ui', self)
        self.update_image()

    def keyPressEvent(self, event):
        if event.key() == Qt.Key_Plus:
            self._map.scale_up()

        elif event.key() == Qt.Key_Minus:
            self._map.scale_down()
        self.update_image()

    def update_image(self):
        image_bytes = self._map.get_image()
        image_pixmap = QPixmap()
        image_pixmap.loadFromData(image_bytes)
        self.label.setPixmap(image_pixmap)


app = QApplication(sys.argv)
window = Window()
window.show()
app.exec()
