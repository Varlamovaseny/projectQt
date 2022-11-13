import sys
from PyQt5 import QtCore, QtGui, QtWidgets
from sudoku import Ui_MainWindow
from PyQt5.QtGui import QPixmap
from PyQt5.QtWidgets import QLabel


class MainWindow(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self):
        self.data = [
            [[2, 3, 4, 1], [1, 4, 2, 3], [4, 2, 1, 3], [3, 1, 2, 4]],
            [[3, 2, 4, 1], [1, 4, 3, 2], [2, 3, 1, 4], [4, 1, 2, 3]],
            [[1, 2, 3, 4], [3, 4, 1, 2], [2, 1, 4, 3], [4, 3, 2, 1]],
            [[4, 3, 1, 2], [2, 1, 4, 3], [3, 4, 2, 1], [1, 2, 3, 4]],
            [[3, 4, 1, 2], [1, 2, 3, 4], [4, 3, 2, 1], [2, 1, 4, 3]]
        ]
        self.coords = [

        ]
        super().__init__()
        self.setupUi(self)
        self.initUI()

    def initUI(self):
        self.pixmap = QPixmap('field.jpg')
        self.image = QLabel(self)
        self.image.move(40, 50)
        self.image.resize(350, 350)
        self.image.setText("")
        self.image.setPixmap(self.pixmap)
        self.eraser.setStyleSheet("background-image: url(eraser.jpg)")


def run():
    app = QtWidgets.QApplication(sys.argv)
    ex = MainWindow()
    ex.show()
    sys.exit(app.exec_())


if __name__ == '__main__':
    run()
