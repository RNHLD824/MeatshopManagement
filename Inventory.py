from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(720, 500)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MainWindow.sizePolicy().hasHeightForWidth())
        MainWindow.setSizePolicy(sizePolicy)
        MainWindow.setMinimumSize(QtCore.QSize(720, 500))
        MainWindow.setMaximumSize(QtCore.QSize(720, 500))
        self.centralwidget = QtWidgets.QWidget(MainWindow)
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
        self.beef_pushbutton = QtWidgets.QPushButton(self.centralwidget)
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
        self.chicken_pushbutton = QtWidgets.QPushButton(self.centralwidget)
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
        self.add_pushbutton = QtWidgets.QPushButton(self.centralwidget)
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
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label.setText(_translate("MainWindow", "<html><head/><body><p><img src=\":/inv_src/mainwindow.jpg\"/></p></body></html>"))
        self.beef_pushbutton.setText(_translate("MainWindow", "BEEF"))
        self.chicken_pushbutton.setText(_translate("MainWindow", "CHICKEN"))
        self.pork_pushbutton.setText(_translate("MainWindow", "PORK"))
        item = self.inventory_table.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "Name"))
        item = self.inventory_table.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "Price"))
        item = self.inventory_table.horizontalHeaderItem(2)
        item.setText(_translate("MainWindow", "Stock"))
        self.add_pushbutton.setText(_translate("MainWindow", "ADD"))
        self.update_pushbutton.setText(_translate("MainWindow", "UPDATE"))
        self.delete_pushbutton.setText(_translate("MainWindow", "DELETE"))
        self.back_pushButton.setText(_translate("MainWindow", "Back"))

import inventory_source

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

