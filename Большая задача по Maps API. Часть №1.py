import sys
from PyQt5 import uic
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QPixmap
from PyQt5.QtWidgets import QMainWindow, QApplication
import requests


class MyWidget(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi('task1.ui', self)
        self.response = None
        self.delta = 0.02
        self.latt = 0
        self.lonn = 0
        self.spnn = 1
        self.x = 125
        self.initUI()

    def initUI(self):
        self.setStyleSheet("QWidget { background-color: #ffd9b3}")
        self.sh.clicked.connect(self.showw)

    def keyPressEvent(self, e):
        if e.key() == Qt.Key_PageUp:
            self.upp()
        elif e.key() == Qt.Key_PageDown:
            self.downn()
        elif e.key() == Qt.Key_Right:
            self.right()
        elif e.key() == Qt.Key_Left:
            self.left()
        self.showw()

    def right(self):
        self.lat.setText(str(float(self.lat.text()) + 10))

    def left(self):
        self.lat.setText(str(float(self.lon.text()) - 10))

    def upp(self):
        x = float(self.spn.text())
        if x <= self.x / 1.5:
            self.spnn = float(x) * 1.5
        self.spn.setText(str(self.spnn))

    def downn(self):
        x = float(self.spn.text())
        if x > self.delta * 1.5:
            self.spnn = float(self.spn.text()) / 1.5
        self.spn.setText(str(self.spnn))

    def showw(self):
        api_server = "http://static-maps.yandex.ru/1.x/"
        self.latt, self.lonn, self.spnn = self.lat.text(), self.lon.text(), self.spn.text()

        params = {
            "ll": ",".join([self.lonn, self.latt]),
            "spn": ",".join([self.spnn, self.spnn]),
            "l": "map"
        }
        self.response = requests.get(api_server, params=params)
        pixm = self.writefile()
        self.pic.setPixmap(pixm.scaled(761, 541))

    def writefile(self):
        map_file = "map.png"
        try:
            with open(map_file, "wb") as file:
                file.write(self.response.content)
        except IOError as ex:
            self.res.setText('Object is not found')
        pixm = QPixmap('map.png')
        return pixm


app = QApplication(sys.argv)
ex = MyWidget()
ex.show()
sys.exit(app.exec())
