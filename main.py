from PyQt5 import QtCore, QtGui, QtWidgets
from circle import CircleList
from binarytree import TreeNode


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(432, 342)
        MainWindow.setCursor(QtGui.QCursor(QtCore.Qt.ArrowCursor))
        MainWindow.setStyleSheet("QPushButton {border: 1px solid grey; border-radius: 5px; background-color: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1, stop: 0 #f6f7fa, stop: 1 #dadbde)}\n"
"QPushButton:pressed { background-color: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1, stop: 0 #dadbde, stop: 1 #E5CCFF) }")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.tabWidget = QtWidgets.QTabWidget(self.centralwidget)
        self.tabWidget.setGeometry(QtCore.QRect(0, 0, 431, 341))
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
        self.lineEdit_2 = QtWidgets.QLineEdit(self.tab_2)
        self.lineEdit_2.setGeometry(QtCore.QRect(10, 30, 91, 31))
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.pushButton_3 = QtWidgets.QPushButton(self.tab_2)
        self.pushButton_3.setGeometry(QtCore.QRect(170, 30, 101, 31))
        self.pushButton_3.setObjectName("pushButton_3")
        self.pushButton_3.clicked.connect(self.btn3Clicked)
        self.pushButton_4 = QtWidgets.QPushButton(self.tab_2)
        self.pushButton_4.setGeometry(QtCore.QRect(110, 100, 221, 51))
        self.pushButton_4.setObjectName("pushButton_4")
        self.pushButton_4.clicked.connect(self.btn4Clicked)
        self.listWidget = QtWidgets.QListWidget(self.tab_2)
        self.listWidget.setGeometry(QtCore.QRect(10, 100, 91, 201))
        self.listWidget.setObjectName("listWidget")
        self.label_3 = QtWidgets.QLabel(self.tab_2)
        self.label_3.setGeometry(QtCore.QRect(10, 80, 91, 16))
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(self.tab_2)
        self.label_4.setGeometry(QtCore.QRect(110, 160, 221, 141))
        self.label_4.setText("")
        self.label_4.setAlignment(QtCore.Qt.AlignHCenter|QtCore.Qt.AlignTop)
        self.label_4.setWordWrap(True)
        self.label_4.setObjectName("label_4")
        self.tabWidget.addTab(self.tab_2, "")
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        self.tabWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Лабораторная работа номер два))))))))))))))))))))))))00"))
        self.pushButton.setText(_translate("MainWindow", "Сформировать\n"
"список"))
        self.label.setText(_translate("MainWindow", "Созданный список"))
        self.label_2.setText(_translate("MainWindow", "Полученный список"))
        self.pushButton_2.setText(_translate("MainWindow", "Вычесть из каждого\n"
"последующего элемента предыдущий"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), _translate("MainWindow", "Кольцевой односвязный список"))
        self.pushButton_3.setText(_translate("MainWindow", "Добавить лист"))
        self.pushButton_4.setText(_translate("MainWindow", "Удалить вершины, содержащие\n"
"максимальный\n"
"и минимальный элемент"))
        self.label_3.setText(_translate("MainWindow", "Вывод дерева"))
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
        except AttributeError:
            self.plainTextEdit_2.setPlainText("Ошибка: список не заполнен")
        except Exception as e:
            self.plainTextEdit_2.setPlainText("Ошибка: " + str(e))

    tree = TreeNode()
    arr = []

    def outTree(self, tree):
        if tree.left:
            self.outTree(tree.left)
        self.arr.append(tree.key)
        if tree.right:
            self.outTree(tree.right)

    def btn3Clicked(self):
        try:
            self.tree.insert(int(self.lineEdit_2.text().strip()))
            self.arr = []
            self.outTree(self.tree)
            self.listWidget.clear()
            for i in self.arr:
                self.listWidget.addItem(str(i))
            self.label_4.setText("")
        except Exception:
            self.label_4.setText("Ошибка: неправильно введен лист дерева")

    '''def delMin(self, tree):
        if not tree.left:
            if not tree.right:
                tree = None
            else:
                tree = tree.right
        else:
            self.delMin(tree.left)

    def delMax(self, tree):
        if not tree.right:
            if not tree.left:
                tree = None
            else:
                tree = tree.left
        else:
            self.delMax(tree.right)'''

    def btn4Clicked(self):
        try:
            if len(self.arr) == 0:
                raise Exception("в дереве нет элементов")
            #self.delMin(self.tree)
            #self.delMax(self.tree)
            self.tree = self.tree.delMin()
            self.tree = self.tree.delMax()
            self.arr = []
            self.outTree(self.tree)
            self.listWidget.clear()
            for i in self.arr:
                self.listWidget.addItem(str(i))
            self.label_4.setText("")
        except Exception as e:
            self.label_4.setText("Ошибка: " + str(e))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())