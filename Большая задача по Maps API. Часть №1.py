import sys
from PyQt5 import uic
from PyQt5.QtGui import QPixmap
from PyQt5.QtWidgets import QMainWindow, QApplication, QLabel, QPushButton
from django.contrib.sites import requests


class MyWidget(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi('task1.ui', self)
        self.response = None
        self.initUI()

    def initUI(self):
        self.setStyleSheet("QWidget { background-color: #ffd9b3}")
        self.sh.clicked.connect(self.show1)

    def show1(self):
        coords, spn = self.coords.text(), self.spn.text()
        map_request = "http://static-maps.yandex.ru/1.x/?ll={}&spn={}&l=map".format(coords, spn)
        self.response = requests.get(map_request)
        pixm = self.writefile()
        self.pic.setPixmap(pixm.scaled(761, 541))

    def writefile(self):
        map_file = "map.png"
        try:
            with open(map_file, "wb") as file:
                file.write(self.response.content)
        except IOError as ex:
            self.res.setText('Object is not found')
            sys.exit(2)
        pixm = QPixmap(file)
        return pixm


app = QApplication(sys.argv)
ex = MyWidget()
ex.show()
sys.exit(app.exec())
