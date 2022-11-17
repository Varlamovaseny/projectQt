from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtGui import *
from PyQt5.QtCore import *
import sys
from PyQt5.QtWidgets import *


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1000, 700)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.pushButton_14 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_14.setGeometry(QtCore.QRect(230, 400, 131, 131))
        self.pushButton_14.setText("")
        self.pushButton_14.setObjectName("pushButton_14")
        self.pushButton_1 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_1.setGeometry(QtCore.QRect(100, 30, 131, 131))
        self.pushButton_1.setText("")
        self.pushButton_1.setObjectName("pushButton_1")
        self.pushButton_7 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_7.setGeometry(QtCore.QRect(360, 160, 131, 121))
        self.pushButton_7.setText("")
        self.pushButton_7.setObjectName("pushButton_7")
        self.pushButton_4 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_4.setGeometry(QtCore.QRect(490, 30, 131, 131))
        self.pushButton_4.setText("")
        self.pushButton_4.setObjectName("pushButton_4")
        self.pushButton_3 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_3.setGeometry(QtCore.QRect(361, 30, 131, 131))
        self.pushButton_3.setText("")
        self.pushButton_3.setObjectName("pushButton_3")
        self.pushButton_6 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_6.setGeometry(QtCore.QRect(230, 161, 131, 121))
        self.pushButton_6.setText("")
        self.pushButton_6.setObjectName("pushButton_6")
        self.pushButton_12 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_12.setGeometry(QtCore.QRect(490, 280, 131, 121))
        self.pushButton_12.setText("")
        self.pushButton_12.setObjectName("pushButton_12")
        self.pushButton_2 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_2.setGeometry(QtCore.QRect(230, 30, 131, 131))
        self.pushButton_2.setText("")
        self.pushButton_2.setObjectName("pushButton_2")
        self.pushButton_16 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_16.setGeometry(QtCore.QRect(490, 400, 131, 131))
        self.pushButton_16.setText("")
        self.pushButton_16.setObjectName("pushButton_16")
        self.pushButton_13 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_13.setGeometry(QtCore.QRect(100, 400, 131, 131))
        self.pushButton_13.setText("")
        self.pushButton_13.setObjectName("pushButton_13")
        self.pushButton_5 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_5.setGeometry(QtCore.QRect(100, 160, 131, 121))
        self.pushButton_5.setText("")
        self.pushButton_5.setObjectName("pushButton_5")
        self.pushButton_11 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_11.setGeometry(QtCore.QRect(360, 280, 131, 121))
        self.pushButton_11.setText("")
        self.pushButton_11.setObjectName("pushButton_11")
        self.pushButton_10 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_10.setGeometry(QtCore.QRect(230, 280, 131, 121))
        self.pushButton_10.setText("")
        self.pushButton_10.setObjectName("pushButton_10")
        self.pushButton_8 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_8.setGeometry(QtCore.QRect(490, 160, 131, 121))
        self.pushButton_8.setText("")
        self.pushButton_8.setObjectName("pushButton_8")
        self.pushButton_15 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_15.setGeometry(QtCore.QRect(360, 400, 131, 131))
        self.pushButton_15.setText("")
        self.pushButton_15.setObjectName("pushButton_15")
        self.pushButton_9 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_9.setGeometry(QtCore.QRect(100, 280, 131, 121))
        self.pushButton_9.setText("")
        self.pushButton_9.setObjectName("pushButton_9")
        self.textEdit = QtWidgets.QTextEdit(self.centralwidget)
        self.textEdit.setGeometry(QtCore.QRect(660, 100, 321, 281))
        self.textEdit.setObjectName("textEdit")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(670, 20, 260, 61))
        font = QtGui.QFont()
        font.setFamily("Sitka Small")
        font.setPointSize(30)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(670, 390, 161, 71))
        font = QtGui.QFont()
        font.setFamily("Sitka Banner")
        font.setPointSize(30)
        self.label_2.setFont(font)
        self.buttons = [
            self.pushButton_1, self.pushButton_2, self.pushButton_3, self.pushButton_4,
            self.pushButton_5, self.pushButton_6, self.pushButton_7, self.pushButton_8,
            self.pushButton_9, self.pushButton_10, self.pushButton_11, self.pushButton_12,
            self.pushButton_13, self.pushButton_14, self.pushButton_15, self.pushButton_16
        ]
        for elem in self.buttons:
            elem.setFont(font)
        self.label_2.setObjectName("label_2")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)

        self.time_label = QLabel(self)
        self.time_label.setGeometry(670, 470, 250, 90)
        self.time_label.setStyleSheet("border : 4px solid black;")
        self.time_label.setText(str(self.count))
        self.time_label.setFont(font)
        self.time_label.setAlignment(Qt.AlignCenter)

        self.menubar.setGeometry(QtCore.QRect(0, 0, 1000, 18))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Судоку"))
        self.label.setText(_translate("MainWindow", "Рейтинг"))
        self.label_2.setText(_translate("MainWindow", "Время"))


if __name__ == "__main__":
    import sys

    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
