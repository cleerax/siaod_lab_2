from PyQt5 import QtCore, QtGui, QtWidgets
from circle import CircleList, Node


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 600)
        MainWindow.setCursor(QtGui.QCursor(QtCore.Qt.ArrowCursor))
        MainWindow.setStyleSheet("")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.tabWidget = QtWidgets.QTabWidget(self.centralwidget)
        self.tabWidget.setGeometry(QtCore.QRect(0, 0, 791, 601))
        self.tabWidget.setObjectName("tabWidget")
        self.tab = QtWidgets.QWidget()
        self.tab.setObjectName("tab")
        self.lineEdit = QtWidgets.QLineEdit(self.tab)
        self.lineEdit.setGeometry(QtCore.QRect(10, 10, 251, 31))
        self.lineEdit.setObjectName("lineEdit")
        self.pushButton = QtWidgets.QPushButton(self.tab)
        self.pushButton.setGeometry(QtCore.QRect(270, 0, 141, 51))
        self.pushButton.setObjectName("pushButton")
        self.pushButton.clicked.connect(self.btn1Clicked)
        self.label = QtWidgets.QLabel(self.tab)
        self.label.setGeometry(QtCore.QRect(10, 50, 121, 16))
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.tab)
        self.label_2.setGeometry(QtCore.QRect(10, 200, 131, 16))
        self.label_2.setObjectName("label_2")
        self.pushButton_2 = QtWidgets.QPushButton(self.tab)
        self.pushButton_2.setGeometry(QtCore.QRect(10, 150, 401, 51))
        self.pushButton_2.setObjectName("pushButton_2")
        self.pushButton_2.clicked.connect(self.btn2Clicked)
        self.plainTextEdit = QtWidgets.QPlainTextEdit(self.tab)
        self.plainTextEdit.setGeometry(QtCore.QRect(10, 70, 401, 71))
        self.plainTextEdit.setReadOnly(True)
        self.plainTextEdit.setObjectName("plainTextEdit")
        self.plainTextEdit.viewport().setCursor(QtCore.Qt.ArrowCursor)
        self.plainTextEdit_2 = QtWidgets.QPlainTextEdit(self.tab)
        self.plainTextEdit_2.setGeometry(QtCore.QRect(10, 220, 401, 71))
        self.plainTextEdit_2.setReadOnly(True)
        self.plainTextEdit_2.setObjectName("plainTextEdit_2")
        self.plainTextEdit_2.viewport().setCursor(QtCore.Qt.ArrowCursor)
        self.tabWidget.addTab(self.tab, "")
        self.tab_2 = QtWidgets.QWidget()
        self.tab_2.setObjectName("tab_2")
        self.tabWidget.addTab(self.tab_2, "")
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        self.tabWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Лабораторная работа номер два))))))))))))))))))))))))00"))
        self.pushButton.setText(_translate("MainWindow", "Сформировать\nсписок"))
        self.label.setText(_translate("MainWindow", "Созданный список"))
        self.label_2.setText(_translate("MainWindow", "Полученный список"))
        self.pushButton_2.setText(_translate("MainWindow", "Вычесть из каждого\nпоследующего элемента предыдущий"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), _translate("MainWindow", "Кольцевой односвязный список"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), _translate("MainWindow", "Бинарное дерево"))

    crcl = None

    def btn1Clicked(self):
        try:
            self.crcl = CircleList()
            s = self.lineEdit.text()
            if s == "":
                raise Exception("ничего не введено")

            arr = list(map(int, s.split()))
            s = ""
            for i in arr:
                self.crcl.push(i)
                s += str(i) + ", "
            s = s[:-2]
            self.plainTextEdit.setPlainText(s)
        except ValueError:
            self.plainTextEdit.setPlainText("Список должен состоять из натуриальных чисел, введенных через пробел")
        except Exception as e:
            self.plainTextEdit.setPlainText("Ошибка: " + str(e))

    def btn2Clicked(self):
        try:
            if not self.crcl:
                raise Exception("список не заполнен")
            self.plainTextEdit_2.setPlainText(self.crcl.action())
        except Exception as e:
            self.plainTextEdit_2.setPlainText("Ошибка: " + str(e))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
