from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QMessageBox, QApplication, QMainWindow, QPushButton
import pymysql
from Inventory import Ui_inventoryWindow

class Ui_transactionWindow(QMainWindow):

    def __init__(self, Login):
        self.login = Login

    def logOut(self):
        self.Dialog.hide()
        self.login.show()
        return None

    def toInventory(self):
        self.inventory = QtWidgets.QMainWindow()
        self.ui = Ui_inventoryWindow()
        self.ui.setupUi(self.inventory)
        self.inventory.show()
        self.this_window.hide()
        
    def setupUi(self, transactionWindow):

        self.this_window = transactionWindow

        transactionWindow.setObjectName("transactionWindow")
        transactionWindow.resize(850, 500)

        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(transactionWindow.sizePolicy().hasHeightForWidth())

        transactionWindow.setSizePolicy(sizePolicy)
        transactionWindow.setMinimumSize(QtCore.QSize(850, 500))
        transactionWindow.setMaximumSize(QtCore.QSize(850, 500))

        self.centralwidget = QtWidgets.QWidget(transactionWindow)
        self.centralwidget.setObjectName("centralwidget")

        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(0, 0, 850, 500))

        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label.sizePolicy().hasHeightForWidth())

        self.label.setSizePolicy(sizePolicy)
        self.label.setMinimumSize(QtCore.QSize(850, 500))
        self.label.setMaximumSize(QtCore.QSize(850, 500))
        self.label.setObjectName("label")

        self.beef_pushbutton = QtWidgets.QPushButton(self.centralwidget)
        self.beef_pushbutton.setGeometry(QtCore.QRect(10, 180, 91, 41))

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

        self.chicken_pushbutton = QtWidgets.QPushButton(self.centralwidget)
        self.chicken_pushbutton.setGeometry(QtCore.QRect(10, 250, 91, 41))

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
        self.pork_pushbutton.setGeometry(QtCore.QRect(10, 320, 91, 41))

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

        self.products_table = QtWidgets.QTableWidget(self.centralwidget)
        self.products_table.setGeometry(QtCore.QRect(110, 120, 301, 341))
        self.products_table.setStyleSheet("QTableWidget  {background-color: rgb(255, 38, 38);\n"
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
        self.products_table.setObjectName("products_table")
        self.products_table.setColumnCount(3)
        self.products_table.setRowCount(0)

        item = QtWidgets.QTableWidgetItem()

        font = QtGui.QFont()
        font.setFamily("Eras Demi ITC")
        font.setPointSize(11)

        item.setFont(font)
        self.products_table.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()

        font = QtGui.QFont()
        font.setFamily("Eras Demi ITC")
        font.setPointSize(11)

        item.setFont(font)
        self.products_table.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()

        font = QtGui.QFont()
        font.setFamily("Eras Demi ITC")
        font.setPointSize(11)

        item.setFont(font)
        self.products_table.setHorizontalHeaderItem(2, item)
        self.orders_table = QtWidgets.QTableWidget(self.centralwidget)
        self.orders_table.setGeometry(QtCore.QRect(500, 120, 301, 341))
        self.orders_table.setStyleSheet("QTableWidget  {background-color: rgb(255, 38, 38);\n"
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
        self.orders_table.setObjectName("orders_table")
        self.orders_table.setColumnCount(3)
        self.orders_table.setRowCount(0)

        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setFamily("Eras Demi ITC")
        font.setPointSize(11)

        item.setFont(font)
        self.orders_table.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()

        font = QtGui.QFont()
        font.setFamily("Eras Demi ITC")
        font.setPointSize(11)

        item.setFont(font)
        self.orders_table.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()

        font = QtGui.QFont()
        font.setFamily("Eras Demi ITC")
        font.setPointSize(11)

        item.setFont(font)
        self.orders_table.setHorizontalHeaderItem(2, item)
        self.add_pushbutton = QtWidgets.QPushButton(self.centralwidget)
        self.add_pushbutton.setGeometry(QtCore.QRect(400, 210, 91, 81))

        font = QtGui.QFont()
        font.setFamily("Eras Demi ITC")
        font.setPointSize(9)

        self.add_pushbutton.setFont(font)
        self.add_pushbutton.setStyleSheet("QPushButton{background-color: transparent;\n"
"background-image: url(:/arr_right/Arrow_right.PNG);}")
        self.add_pushbutton.setObjectName("add_pushbutton")

        self.remove_pushbutton = QtWidgets.QPushButton(self.centralwidget)
        self.remove_pushbutton.setGeometry(QtCore.QRect(410, 300, 91, 81))

        font = QtGui.QFont()
        font.setFamily("Eras Demi ITC")
        font.setPointSize(8)

        self.remove_pushbutton.setFont(font)
        self.remove_pushbutton.setStyleSheet("QPushButton{background-color: transparent;\n"
"background-image: url(:/arr_left/Arrow_left.PNG);}")
        self.remove_pushbutton.setObjectName("remove_pushbutton")

        self.submit_pushbutton = QtWidgets.QPushButton(self.centralwidget)
        self.submit_pushbutton.setGeometry(QtCore.QRect(720, 70, 101, 41))

        font = QtGui.QFont()
        font.setFamily("Big Space")
        font.setPointSize(20)

        self.submit_pushbutton.setFont(font)
        self.submit_pushbutton.setStyleSheet("QPushButton {background-color: rgb(255, 38, 38);\n"
"                        color:rgb(255,255,255);                    \n"
"}\n"
"QPushButton:hover {background-color: rgb(218, 167, 0);\n"
"}")
        self.submit_pushbutton.setObjectName("submit_pushbutton")

        self.logout_pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.logout_pushButton.setGeometry(QtCore.QRect(10, 10, 101, 31))

        font = QtGui.QFont()
        font.setFamily("Fixedsys")

        self.logout_pushButton.setFont(font)
        self.logout_pushButton.setStyleSheet("QPushButton {background-color: rgb(255, 38, 38);\n"
"                        color:rgb(255,255,255);                                \n"
"}\n"
"QPushButton:hover {background-color: rgb(218, 167, 0);\n"
"}")
        self.logout_pushButton.setObjectName("logout_pushButton")

        self.inventory_pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.inventory_pushButton.setGeometry(QtCore.QRect(10, 50, 101, 31))
    

        font = QtGui.QFont()
        font.setFamily("Fixedsys")

        self.inventory_pushButton.setFont(font)
        self.inventory_pushButton.setStyleSheet("QPushButton {background-color: rgb(255, 38, 38);\n"
"                        color:rgb(255,255,255);                                \n"
"}\n"
"QPushButton:hover {background-color: rgb(218, 167, 0);\n"
"}")
        self.inventory_pushButton.setObjectName("inventory_pushButton")
        self.inventory_pushButton.clicked.connect(self.toInventory)
        
        transactionWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(transactionWindow)
        QtCore.QMetaObject.connectSlotsByName(transactionWindow)

    def retranslateUi(self, transactionWindow):
        _translate = QtCore.QCoreApplication.translate
        transactionWindow.setWindowTitle(_translate("transactionWindow", "MainWindow"))
        self.label.setText(_translate("transactionWindow", "<html><head/><body><p><img src=\":/trans_src/mainwindow2.jpg\"/></p></body></html>"))
        self.beef_pushbutton.setText(_translate("transactionWindow", "BEEF"))
        self.chicken_pushbutton.setText(_translate("transactionWindow", "CHICKEN"))
        self.pork_pushbutton.setText(_translate("transactionWindow", "PORK"))
        item = self.products_table.horizontalHeaderItem(0)
        item.setText(_translate("transactionWindow", "Name"))
        item = self.products_table.horizontalHeaderItem(1)
        item.setText(_translate("transactionWindow", "Price"))
        item = self.products_table.horizontalHeaderItem(2)
        item.setText(_translate("transactionWindow", "Stock"))
        item = self.orders_table.horizontalHeaderItem(0)
        item.setText(_translate("transactionWindow", "Name"))
        item = self.orders_table.horizontalHeaderItem(1)
        item.setText(_translate("transactionWindow", "Price"))
        item = self.orders_table.horizontalHeaderItem(2)
        item.setText(_translate("transactionWindow", "Stock"))
        self.add_pushbutton.setText(_translate("transactionWindow", "     ADD"))
        self.remove_pushbutton.setText(_translate("transactionWindow", "REMOVE"))
        self.submit_pushbutton.setText(_translate("transactionWindow", "SUBMIT"))
        self.logout_pushButton.setText(_translate("transactionWindow", "Log Out"))
        self.inventory_pushButton.setText(_translate("transactionWindow", "Inventory"))


import arrow_left
import arrow_right
import transaction_source

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    transactionWindow = QtWidgets.QMainWindow()
    ui = Ui_transactionWindow()
    ui.setupUi(transactionWindow)
    transactionWindow.show()
    sys.exit(app.exec_())

