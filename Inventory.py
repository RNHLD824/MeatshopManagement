from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QMessageBox, QApplication, QMainWindow, QPushButton
from Add import Ui_addWindow
from Update import Ui_updateWindow

class Ui_inventoryWindow(QMainWindow):

    def __init__(self):
        self.selected = ""

    def toAdd(self):
        self.add = QtWidgets.QMainWindow()
        self.ui = Ui_addWindow(self, self.selected)
        self.ui.setupUi(self.add) 
        self.add.show()
        self.this_window.hide()

    def toUpdate(self):
        self.update = QtWidgets.QMainWindow()
        self.ui = Ui_updateWindow(self, self.selected)
        self.ui.setupUi(self.update) 
        self.update.show()
        self.this_window.hide()

    def beefselected(self):
        self.selected = "beef"
        print(self.selected)

    def chickenselected(self):
        self.selected = "chicken"
        print(self.selected)

    def porkselected(self):
        self.selected = "pork"
        print(self.selected)
    
    def setupUi(self, inventoryWindow):

        self.this_window = inventoryWindow
        
        inventoryWindow.setObjectName("inventoryWindow")
        inventoryWindow.resize(720, 500)

        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(inventoryWindow.sizePolicy().hasHeightForWidth())

        inventoryWindow.setSizePolicy(sizePolicy)
        inventoryWindow.setMinimumSize(QtCore.QSize(720, 500))
        inventoryWindow.setMaximumSize(QtCore.QSize(720, 500))

        self.centralwidget = QtWidgets.QWidget(inventoryWindow)
        self.centralwidget.setObjectName("centralwidget")

        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(0, 0, 720, 500))

        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label.sizePolicy().hasHeightForWidth())

        self.label.setSizePolicy(sizePolicy)
        self.label.setMinimumSize(QtCore.QSize(720, 500))
        self.label.setMaximumSize(QtCore.QSize(720, 500))
        self.label.setObjectName("label")

        self.beef_pushbutton = QtWidgets.QPushButton(self.centralwidget, clicked=lambda func: self.beefselected())
        self.beef_pushbutton.setGeometry(QtCore.QRect(49, 190, 101, 41))

        font = QtGui.QFont()
        font.setFamily("Big Space")
        font.setPointSize(20)

        self.beef_pushbutton.setFont(font)
        self.beef_pushbutton.setStyleSheet("QPushButton {background-color: rgb(255, 38, 38);\n"
"                        color:rgb(255,255,255);                    \n"
"}\n"
"QPushButton:hover {background-color: rgb(218, 167, 0);\n"
"}")
        self.beef_pushbutton.setObjectName("beef_pushbutton")

        self.chicken_pushbutton = QtWidgets.QPushButton(self.centralwidget, clicked=lambda func: self.chickenselected())
        self.chicken_pushbutton.setGeometry(QtCore.QRect(49, 270, 101, 41))

        font = QtGui.QFont()
        font.setFamily("Big Space")
        font.setPointSize(20)

        self.chicken_pushbutton.setFont(font)
        self.chicken_pushbutton.setStyleSheet("QPushButton {background-color: rgb(255, 38, 38);\n"
"                        color:rgb(255,255,255);                    \n"
"}\n"
"QPushButton:hover {background-color: rgb(218, 167, 0);\n"
"}")
        self.chicken_pushbutton.setObjectName("chicken_pushbutton")

        self.pork_pushbutton = QtWidgets.QPushButton(self.centralwidget)
        self.pork_pushbutton.clicked.connect(lambda func: self.porkselected())
        self.pork_pushbutton.setGeometry(QtCore.QRect(49, 350, 101, 41))

        font = QtGui.QFont()
        font.setFamily("Big Space")
        font.setPointSize(20)

        self.pork_pushbutton.setFont(font)
        self.pork_pushbutton.setStyleSheet("QPushButton {background-color: rgb(255, 38, 38);\n"
"                        color:rgb(255,255,255);                    \n"
"}\n"
"QPushButton:hover {background-color: rgb(218, 167, 0);\n"
"}")
        self.pork_pushbutton.setObjectName("pork_pushbutton")

        self.inventory_table = QtWidgets.QTableWidget(self.centralwidget)
        self.inventory_table.setGeometry(QtCore.QRect(220, 120, 301, 351))

        font = QtGui.QFont()
        font.setFamily("Times New Roman")

        self.inventory_table.setFont(font)
        self.inventory_table.setStyleSheet("QTableWidget  {background-color: rgb(255, 38, 38);\n"
"                        border: none;\n"
"                        color:rgb(255,255,255);\n"
"                        gridline-color:rgb(255,255,255);\n"
"}\n"
"QHeaderView:section {border:none\n"
"                                    color:rgb(255,255,255);\n"
"}\n"
"QWidget {border:none\n"
"                color:rgb(255, 255, 255);\n"
"}")
        self.inventory_table.setObjectName("inventory_table")
        self.inventory_table.setColumnCount(3)
        self.inventory_table.setRowCount(0)

        item = QtWidgets.QTableWidgetItem()

        font = QtGui.QFont()
        font.setFamily("Eras Demi ITC")
        font.setPointSize(11)

        item.setFont(font)

        self.inventory_table.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()

        font = QtGui.QFont()
        font.setFamily("Eras Demi ITC")
        font.setPointSize(11)

        item.setFont(font)
        self.inventory_table.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()

        font = QtGui.QFont()
        font.setFamily("Eras Demi ITC")
        font.setPointSize(11)

        item.setFont(font)
        self.inventory_table.setHorizontalHeaderItem(2, item)

        self.add_pushbutton = QtWidgets.QPushButton(self.centralwidget, clicked = lambda func: self.toAdd())
        self.add_pushbutton.setGeometry(QtCore.QRect(570, 190, 101, 41))

        font = QtGui.QFont()
        font.setFamily("Big Space")
        font.setPointSize(20)

        self.add_pushbutton.setFont(font)
        self.add_pushbutton.setStyleSheet("QPushButton {background-color: rgb(255, 38, 38);\n"
"                        color:rgb(255,255,255);                    \n"
"}\n"
"QPushButton:hover {background-color: rgb(218, 167, 0);\n"
"}")
        self.add_pushbutton.setObjectName("add_pushbutton")
        self.add_pushbutton.clicked.connect(self.toAdd)

        self.update_pushbutton = QtWidgets.QPushButton(self.centralwidget)
        self.update_pushbutton.setGeometry(QtCore.QRect(570, 270, 101, 41))

        font = QtGui.QFont()
        font.setFamily("Big Space")
        font.setPointSize(20)

        self.update_pushbutton.setFont(font)
        self.update_pushbutton.setStyleSheet("QPushButton {background-color: rgb(255, 38, 38);\n"
"                        color:rgb(255,255,255);                    \n"
"}\n"
"QPushButton:hover {background-color: rgb(218, 167, 0);\n"
"}")
        self.update_pushbutton.setObjectName("update_pushbutton")
        self.update_pushbutton.clicked.connect(self.toUpdate)

        self.delete_pushbutton = QtWidgets.QPushButton(self.centralwidget)
        self.delete_pushbutton.setGeometry(QtCore.QRect(570, 350, 101, 41))

        font = QtGui.QFont()
        font.setFamily("Big Space")
        font.setPointSize(20)

        self.delete_pushbutton.setFont(font)
        self.delete_pushbutton.setStyleSheet("QPushButton {background-color: rgb(255, 38, 38);\n"
"                        color:rgb(255,255,255);                    \n"
"}\n"
"QPushButton:hover {background-color: rgb(218, 167, 0);\n"
"}")
        self.delete_pushbutton.setObjectName("delete_pushbutton")

        self.back_pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.back_pushButton.setGeometry(QtCore.QRect(20, 20, 101, 31))

        font = QtGui.QFont()
        font.setFamily("Fixedsys")

        self.back_pushButton.setFont(font)
        self.back_pushButton.setStyleSheet("QPushButton {background-color: rgb(255, 38, 38);\n"
"                        color:rgb(255,255,255);                                \n"
"}\n"
"QPushButton:hover {background-color: rgb(218, 167, 0);\n"
"}")
        self.back_pushButton.setObjectName("back_pushButton")
        inventoryWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(inventoryWindow)
        QtCore.QMetaObject.connectSlotsByName(inventoryWindow)

    def retranslateUi(self, inventoryWindow):
        _translate = QtCore.QCoreApplication.translate
        inventoryWindow.setWindowTitle(_translate("inventoryWindow", "MainWindow"))
        self.label.setText(_translate("inventoryWindow", "<html><head/><body><p><img src=\":/inv_src/mainwindow.jpg\"/></p></body></html>"))
        self.beef_pushbutton.setText(_translate("inventoryWindow", "BEEF"))
        self.chicken_pushbutton.setText(_translate("inventoryWindow", "CHICKEN"))
        self.pork_pushbutton.setText(_translate("inventoryWindow", "PORK"))
        item = self.inventory_table.horizontalHeaderItem(0)
        item.setText(_translate("inventoryWindow", "Name"))
        item = self.inventory_table.horizontalHeaderItem(1)
        item.setText(_translate("inventoryWindow", "Price"))
        item = self.inventory_table.horizontalHeaderItem(2)
        item.setText(_translate("inventoryWindow", "Stock"))
        self.add_pushbutton.setText(_translate("inventoryWindow", "ADD"))
        self.update_pushbutton.setText(_translate("inventoryWindow", "UPDATE"))
        self.delete_pushbutton.setText(_translate("inventoryWindow", "DELETE"))
        self.back_pushButton.setText(_translate("inventoryWindow", "Back"))

import inventory_source

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    inventoryWindow = QtWidgets.QMainWindow()
    ui = Ui_inventoryWindow()
    ui.setupUi(inventoryWindow)
    inventoryWindow.show()
    sys.exit(app.exec_())

