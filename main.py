import random
import sys
from PyQt5 import QtCore, QtGui, QtWidgets
from sudoku import Ui_MainWindow
from PyQt5.QtCore import Qt
from PyQt5.QtCore import *


class MainWindow(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self):
        self.data = [
            [[2, 3, 4, 1], [1, 4, 3, 2], [4, 2, 1, 3], [3, 1, 2, 4]],
            [[3, 2, 4, 1], [1, 4, 3, 2], [2, 3, 1, 4], [4, 1, 2, 3]],
            [[1, 2, 3, 4], [3, 4, 1, 2], [2, 1, 4, 3], [4, 3, 2, 1]],
            [[4, 3, 1, 2], [2, 1, 4, 3], [3, 4, 2, 1], [1, 2, 3, 4]],
            [[3, 4, 1, 2], [1, 2, 3, 4], [4, 3, 2, 1], [2, 1, 4, 3]]
        ]

        self.check_data = [
            [[2, 3, 4, 1], [1, 4, 3, 2], [4, 2, 1, 3], [3, 1, 2, 4]],
            [[3, 2, 4, 1], [1, 4, 3, 2], [2, 3, 1, 4], [4, 1, 2, 3]],
            [[1, 2, 3, 4], [3, 4, 1, 2], [2, 1, 4, 3], [4, 3, 2, 1]],
            [[4, 3, 1, 2], [2, 1, 4, 3], [3, 4, 2, 1], [1, 2, 3, 4]],
            [[3, 4, 1, 2], [1, 2, 3, 4], [4, 3, 2, 1], [2, 1, 4, 3]]
        ]
        super().__init__()
        self.count = 0
        self.amount = 0
        self.records = []
        self.setupUi(self)
        self.createfield()
        self.initUI()
        self.num = 0
        MainWindow.setStyleSheet(self, "background-color: #ff9900")

    def initUI(self):
        self.pushButton_1.clicked.connect(self.click1)
        self.pushButton_2.clicked.connect(self.click2)
        self.pushButton_3.clicked.connect(self.click3)
        self.pushButton_4.clicked.connect(self.click4)
        self.pushButton_5.clicked.connect(self.click5)
        self.pushButton_6.clicked.connect(self.click6)
        self.pushButton_7.clicked.connect(self.click7)
        self.pushButton_8.clicked.connect(self.click8)
        self.pushButton_9.clicked.connect(self.click9)
        self.pushButton_10.clicked.connect(self.click10)
        self.pushButton_11.clicked.connect(self.click11)
        self.pushButton_12.clicked.connect(self.click12)
        self.pushButton_13.clicked.connect(self.click13)
        self.pushButton_14.clicked.connect(self.click14)
        self.pushButton_15.clicked.connect(self.click15)
        self.pushButton_16.clicked.connect(self.click16)

        timer = QTimer(self)
        timer.timeout.connect(self.showTime)
        timer.start(100)

    def createfield(self):
        for el in self.buttons:
            el.setStyleSheet("border : 4px solid black;"
                             "background-color: white")
        self.field = self.data[random.randint(0, 3)][:]
        self.index = self.data.index(self.field)
        field1 = self.field[:]
        self.field_check = self.check_data[self.index][:]

        for i in range(8):
            elem = random.choice(field1)
            index = field1.index(elem)
            elem[random.randint(0, 3)] = ""
            field1[index] = elem
        self.pushButton_1.setText(str(field1[0][0])), self.pushButton_2.setText(
            str(field1[0][1])), self.pushButton_3.setText(
            str(field1[0][2]))
        self.pushButton_4.setText(str(field1[0][3])), self.pushButton_5.setText(str(field1[1][0]))
        self.pushButton_6.setText(str(field1[1][1])), self.pushButton_7.setText(str(field1[1][2]))
        self.pushButton_8.setText(str(field1[1][3])), self.pushButton_9.setText(str(field1[2][0]))
        self.pushButton_10.setText(str(field1[2][1])), self.pushButton_11.setText(str(field1[2][2]))
        self.pushButton_12.setText(str(field1[2][3])), self.pushButton_13.setText(str(field1[3][0]))
        self.pushButton_14.setText(str(field1[3][1])), self.pushButton_15.setText(str(field1[3][2]))
        self.pushButton_16.setText(str(field1[3][3]))
        self.flag = True
        self.count = 0
        self.amount = 0
        for elem in field1:
            self.amount += elem.count("")

    def click1(self):
        if self.num != 0 and self.pushButton_1.text() != str(self.field_check[0][0]):
            self.pushButton_1.setText(self.num)
            if int(self.pushButton_1.text()) != self.field_check[0][0]:
                self.pushButton_1.setStyleSheet("background-color: red;" 
                                                "border : 4px solid black")

            else:
                self.pushButton_1.setStyleSheet("background-color: green;" 
                                                "border: 4px solid black")
                self.amount -= 1
                if self.amount == 0:
                    self.stop()

    def click2(self):
        if self.num != 0 and self.pushButton_2.text() != str(self.field_check[0][1]):
            self.pushButton_2.setText(self.num)
            if int(self.pushButton_2.text()) != self.field_check[0][1]:
                self.pushButton_2.setStyleSheet("background-color: red;"
                                                "border: 4px solid black")

            else:
                self.pushButton_2.setStyleSheet("background-color: green;"
                                                "border: 4px solid black")
                self.amount -= 1
                if self.amount == 0:
                    self.stop()

    def click3(self):
        if self.num != 0 and self.pushButton_3.text() != str(self.field_check[0][2]):
            self.pushButton_3.setText(self.num)
            if int(self.pushButton_3.text()) != self.field_check[0][2]:
                self.pushButton_3.setStyleSheet("background-color: red;"
                                                "border: 4px solid black")

            else:
                self.pushButton_3.setStyleSheet("background-color: green;"
                                                "border: 4px solid black")
                self.amount -= 1
                if self.amount == 0:
                    self.stop()

    def click4(self):
        if self.num != 0 and self.pushButton_4.text() != str(self.field_check[0][3]):
            self.pushButton_4.setText(self.num)
            if int(self.pushButton_4.text()) != self.field_check[0][3]:
                self.pushButton_4.setStyleSheet("background-color: red;"
                                                "border: 4px solid black")
            else:
                self.pushButton_4.setStyleSheet("background-color: green;"
                                                "border: 4px solid black")
                self.amount -= 1
                if self.amount == 0:
                    self.stop()

    def click5(self):
        if self.num != 0 and self.pushButton_5.text() != str(self.field_check[1][0]):
            self.pushButton_5.setText(self.num)
            if int(self.pushButton_5.text()) != self.field_check[1][0]:
                self.pushButton_5.setStyleSheet("background-color: red;"
                                                "border: 4px solid black")
            else:
                self.pushButton_5.setStyleSheet("background-color: green;"
                                                "border: 4px solid black")
                self.amount -= 1
                if self.amount == 0:
                    self.stop()

    def click6(self):
        if self.num != 0 and self.pushButton_6.text() != str(self.field_check[1][1]):
            self.pushButton_6.setText(self.num)
            if int(self.pushButton_6.text()) != self.field_check[1][1]:
                self.pushButton_6.setStyleSheet("background-color: red;"
                                                "border: 4px solid black")
            else:
                self.pushButton_6.setStyleSheet("background-color: green;"
                                                "border: 4px solid black")
                self.amount -= 1
                if self.amount == 0:
                    self.stop()

    def click7(self):
        if self.num != 0 and self.pushButton_7.text() != str(self.field_check[1][2]):
            self.pushButton_7.setText(self.num)
            if int(self.pushButton_7.text()) != self.field_check[1][2]:
                self.pushButton_7.setStyleSheet("background-color: red;"
                                                "border: 4px solid black")
            else:
                self.pushButton_7.setStyleSheet("background-color: green;"
                                                "border: 4px solid black")
                self.amount -= 1
                if self.amount == 0:
                    self.stop()

    def click8(self):
        if self.num != 0 and self.pushButton_8.text() != str(self.field_check[1][3]):
            self.pushButton_8.setText(self.num)
            if int(self.pushButton_8.text()) != self.field_check[1][3]:
                self.pushButton_8.setStyleSheet("background-color: red;"
                                                "border: 4px solid black")
            else:
                self.pushButton_8.setStyleSheet("background-color: green;"
                                                "border: 4px solid black")
                self.amount -= 1
                if self.amount == 0:
                    self.stop()

    def click9(self):
        if self.num != 0 and self.pushButton_9.text() != str(self.field_check[2][0]):
            self.pushButton_9.setText(self.num)
            if int(self.pushButton_9.text()) != self.field_check[2][0]:
                self.pushButton_9.setStyleSheet("background-color: red;"
                                                "border: 4px solid black")
            else:
                self.pushButton_9.setStyleSheet("background-color: green;"
                                                "border: 4px solid black")
                self.amount -= 1
                if self.amount == 0:
                    self.stop()

    def click10(self):
        if self.num != 0 and self.pushButton_10.text() != str(self.field_check[2][1]):
            self.pushButton_10.setText(self.num)
            if int(self.pushButton_10.text()) != self.field_check[2][1]:
                self.pushButton_10.setStyleSheet("background-color: red;"
                                                 "border: 4px solid black")
            else:
                self.pushButton_10.setStyleSheet("background-color: green;"
                                                 "border: 4px solid black")
                self.amount -= 1
                if self.amount == 0:
                    self.stop()

    def click11(self):
        if self.num != 0 and self.pushButton_11.text() != str(self.field_check[2][2]):
            self.pushButton_11.setText(self.num)
            if int(self.pushButton_11.text()) != self.field_check[2][2]:
                self.pushButton_11.setStyleSheet("background-color: red;"
                                                 "border: 4px solid black")
            else:
                self.pushButton_11.setStyleSheet("background-color: green;"
                                                 "border: 4px solid black")
                self.amount -= 1
                if self.amount == 0:
                    self.stop()

    def click12(self):
        if self.num != 0 and self.pushButton_12.text() != str(self.field_check[2][3]):
            self.pushButton_12.setText(self.num)
            if int(self.pushButton_12.text()) != self.field_check[2][3]:
                self.pushButton_12.setStyleSheet("background-color: red;"
                                                 "border: 4px solid black")
            else:
                self.pushButton_12.setStyleSheet("background-color: green;"
                                                 "border: 4px solid black")
                self.amount -= 1
                if self.amount == 0:
                    self.stop()

    def click13(self):
        if self.num != 0 and self.pushButton_13.text() != str(self.field_check[3][0]):
            self.pushButton_13.setText(self.num)
            if int(self.pushButton_13.text()) != self.field_check[3][0]:
                self.pushButton_13.setStyleSheet("background-color: red;"
                                                 "border: 4px solid black")
            else:
                self.pushButton_13.setStyleSheet("background-color: green;"
                                                 "border: 4px solid black")
                self.amount -= 1
                if self.amount == 0:
                    self.stop()

    def click14(self):
        if self.num != 0 and self.pushButton_14.text() != str(self.field_check[3][1]):
            self.pushButton_14.setText(self.num)
            if int(self.pushButton_14.text()) != self.field_check[3][1]:
                self.pushButton_14.setStyleSheet("background-color: red;"
                                                 "border: 4px solid black")
            else:
                self.pushButton_14.setStyleSheet("background-color: green;"
                                                 "border: 4px solid black")
                self.amount -= 1
                if self.amount == 0:
                    self.stop()

    def click16(self):
        if self.num != 0 and self.pushButton_16.text() != str(self.field_check[3][3]):
            self.pushButton_16.setText(self.num)
            if int(self.pushButton_16.text()) != self.field_check[3][3]:
                self.pushButton_16.setStyleSheet("background-color: red;"
                                                 "border: 4px solid black")
            else:
                self.pushButton_16.setStyleSheet("background-color: green;"
                                                 "border: 4px solid black")
                self.amount -= 1
                if self.amount == 0:
                    self.stop()

    def click15(self):
        if self.num != 0 and self.pushButton_15.text() != str(self.field_check[3][2]):
            self.pushButton_15.setText(self.num)
            if int(self.pushButton_15.text()) != self.field_check[3][2]:
                self.pushButton_15.setStyleSheet("background-color: red;"
                                                 "border: 4px solid black")
            else:
                self.pushButton_15.setStyleSheet("background-color: green;"
                                                 "border: 4px solid black")
                self.amount -= 1
                if self.amount == 0:
                    self.stop()

    def keyPressEvent(self, event):
        if event.key() == Qt.Key_1:
            self.num = "1"
        if event.key() == Qt.Key_2:
            self.num = "2"
        if event.key() == Qt.Key_3:
            self.num = "3"
        if event.key() == Qt.Key_4:
            self.num = "4"

    def showTime(self):
        if self.flag:
            self.count += 1

        text = str(self.count / 10)

        self.time_label.setText(text)

    def stop(self):
        self.flag = False
        self.createfield()
        self.records.append(float(self.time_label.text()))
        self.records = sorted(self.records)
        self.textEdit.setText(
            "\n".join(
                list(map(lambda x: f"{self.records.index(x) + 1}: {str(x)}", self.records))))


def run():
    app = QtWidgets.QApplication(sys.argv)
    ex = MainWindow()
    ex.show()
    sys.exit(app.exec_())


if __name__ == '__main__':
    run()
