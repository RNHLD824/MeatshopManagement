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
        self.label.setMinimumSize(QtCore.QSize(720, 500))
        self.label.setMaximumSize(QtCore.QSize(720, 500))
        self.label.setObjectName("label")

        self.itemName_edit = QtWidgets.QLineEdit(self.centralwidget)
        self.itemName_edit.setGeometry(QtCore.QRect(270, 140, 201, 61))

        font = QtGui.QFont()
        font.setFamily("Century Gothic")
        font.setPointSize(12)

        self.itemName_edit.setFont(font)
        self.itemName_edit.setAlignment(QtCore.Qt.AlignCenter)
        self.itemName_edit.setObjectName("itemName_edit")

        self.price_doublespinbox = QtWidgets.QDoubleSpinBox(self.centralwidget)
        self.price_doublespinbox.setGeometry(QtCore.QRect(270, 230, 201, 61))

        font = QtGui.QFont()
        font.setFamily("Century Gothic")
        font.setPointSize(12)

        self.price_doublespinbox.setFont(font)
        self.price_doublespinbox.setAlignment(QtCore.Qt.AlignCenter)
        self.price_doublespinbox.setObjectName("price_doublespinbox")

        self.stock_spinbox = QtWidgets.QSpinBox(self.centralwidget)
        self.stock_spinbox.setGeometry(QtCore.QRect(270, 320, 201, 61))

        font = QtGui.QFont()
        font.setFamily("Century Gothic")
        font.setPointSize(12)

        self.stock_spinbox.setFont(font)
        self.stock_spinbox.setAlignment(QtCore.Qt.AlignCenter)
        self.stock_spinbox.setObjectName("stock_spinbox")

        self.add_label = QtWidgets.QLabel(self.centralwidget)
        self.add_label.setGeometry(QtCore.QRect(-20, 0, 151, 61))

        font = QtGui.QFont()
        font.setFamily("Big Space")
        font.setPointSize(24)

        self.add_label.setFont(font)
        self.add_label.setObjectName("add_label")
        self.submit_pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.submit_pushButton.setGeometry(QtCore.QRect(320, 400, 101, 31))

        font = QtGui.QFont()
        font.setFamily("Fixedsys")
        font.setPointSize(12)

        self.submit_pushButton.setFont(font)
        self.submit_pushButton.setStyleSheet("QPushButton {background-color: rgb(255, 38, 38);\n"
"                        color:rgb(255,255,255);                        \n"
"}\n"
"\n"
"QPushButton:hover {background-color: rgb(218, 167, 0);\n"
"}")
        self.submit_pushButton.setObjectName("submit_pushButton")

        self.cancel_pushbutton = QtWidgets.QPushButton(self.centralwidget)
        self.cancel_pushbutton.setGeometry(QtCore.QRect(320, 440, 101, 31))

        font = QtGui.QFont()
        font.setFamily("Fixedsys")
        font.setPointSize(12)

        self.cancel_pushbutton.setFont(font)
        self.cancel_pushbutton.setStyleSheet("QPushButton {background-color: rgb(255, 38, 38);\n"
"                        color:rgb(255,255,255);                    \n"
"}\n"
"QPushButton:hover {background-color: rgb(218, 167, 0);\n"
"}")
        self.cancel_pushbutton.setObjectName("cancel_pushbutton")

        self.price_label = QtWidgets.QLabel(self.centralwidget)
        self.price_label.setGeometry(QtCore.QRect(470, 240, 121, 31))

        font = QtGui.QFont()
        font.setFamily("Big Space")
        font.setPointSize(12)

        self.price_label.setFont(font)
        self.price_label.setObjectName("price_label")

        self.stocks_label = QtWidgets.QLabel(self.centralwidget)
        self.stocks_label.setGeometry(QtCore.QRect(480, 330, 121, 31))

        font = QtGui.QFont()
        font.setFamily("Big Space")
        font.setPointSize(12)

        self.stocks_label.setFont(font)
        self.stocks_label.setObjectName("stocks_label")

        self.itemName_label = QtWidgets.QLabel(self.centralwidget)
        self.itemName_label.setGeometry(QtCore.QRect(490, 150, 121, 31))

        font = QtGui.QFont()
        font.setFamily("Big Space")
        font.setPointSize(12)

        self.itemName_label.setFont(font)
        self.itemName_label.setObjectName("itemName_label")

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label.setText(_translate("MainWindow", "<html><head/><body><p><img src=\":/inv_src/mainwindow.jpg\"/></p></body></html>"))
        self.itemName_edit.setPlaceholderText(_translate("MainWindow", "Name"))
        self.add_label.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\"><span style=\" font-size:36pt; color:#ff2020;\">ADD</span></p></body></html>"))
        self.submit_pushButton.setText(_translate("MainWindow", "Submit"))
        self.cancel_pushbutton.setText(_translate("MainWindow", "Cancel"))
        self.price_label.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\"><span style=\" font-size:18pt; color:#ff2020;\">PRICE</span></p></body></html>"))
        self.stocks_label.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\"><span style=\" font-size:18pt; color:#ff2020;\">STOCKS</span></p></body></html>"))
        self.itemName_label.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\"><span style=\" font-size:18pt; color:#ff2020;\">ITEM NAME</span></p></body></html>"))

import inventory_source

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

