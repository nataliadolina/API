import sys
from PyQt5 import uic
from PyQt5.QtGui import QPixmap
from PyQt5.QtWidgets import QMainWindow, QApplication
import requests


class MyWidget(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi('task1.ui', self)
        self.response = None
        self.delta = 0
        self.latt = 0
        self.lonn = 0
        self.spnn = 1
        self.x = 180
        self.initUI()

    def initUI(self):
        self.setStyleSheet("QWidget { background-color: #ffd9b3}")
        self.sh.clicked.connect(self.showw)
        self.up.clicked.connect(self.upp)
        self.down.clicked.connect(self.downn)

    def upp(self):
        x = float(self.spn.text())
        if x < self.x - self.delta:
            self.spnn = float(self.spn.text())*1.5
        self.spn.setText(str(self.spnn))

    def downn(self):
        x = float(self.spn.text())
        if x > self.delta:
            self.spnn = float(self.spn.text())/1.5
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
        file = None
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
