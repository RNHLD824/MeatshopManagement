from PyQt5 import QtCore, QtGui, QtWidgets
import Signup

class Ui_Dialog(object):
    def login(self):
        username = self.username_input.text()
        password = self.password_input.text()
        
        print (username, password)
    
    def signUp(self):
        self.ui = QtWidgets.QMainWindow()
        self.signup = Signup.Ui_Dialog(self.Dialog)
        self.signup.setupUi(self.ui)
        self.ui.show()
        self.Dialog.hide()
    
    def setupUi(self, Dialog):
        self.Dialog = Dialog
        Dialog.setObjectName("Dialog")
        Dialog.resize(720, 500)

        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(Dialog.sizePolicy().hasHeightForWidth())

        Dialog.setSizePolicy(sizePolicy)
        Dialog.setMinimumSize(QtCore.QSize(720, 500))
        Dialog.setMaximumSize(QtCore.QSize(720, 500))

        self.login_bg = QtWidgets.QLabel(Dialog)
        self.login_bg.setGeometry(QtCore.QRect(0, 0, 720, 500))

        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.login_bg.sizePolicy().hasHeightForWidth())

        self.login_bg.setSizePolicy(sizePolicy)
        self.login_bg.setMinimumSize(QtCore.QSize(720, 500))
        self.login_bg.setMaximumSize(QtCore.QSize(720, 500))
        self.login_bg.setObjectName("login_bg")

        self.username_input = QtWidgets.QLineEdit(Dialog)
        self.username_input.setGeometry(QtCore.QRect(50, 230, 361, 41))
        self.username_input.setStyleSheet("")
        self.username_input.setAlignment(QtCore.Qt.AlignCenter)
        self.username_input.setObjectName("username_input")

        self.password_input = QtWidgets.QLineEdit(Dialog)
        self.password_input.setEchoMode(QtWidgets.QLineEdit.Password)
        self.password_input.setGeometry(QtCore.QRect(50, 310, 361, 41))
        self.password_input.setAlignment(QtCore.Qt.AlignCenter)
        self.password_input.setObjectName("password_input")
        self.username_label = QtWidgets.QLabel(Dialog)
        self.username_label.setGeometry(QtCore.QRect(520, 240, 121, 31))

        font = QtGui.QFont()
        font.setFamily("Big Space")
        font.setPointSize(12)

        self.username_label.setFont(font)
        self.username_label.setObjectName("username_label")
        self.password_label = QtWidgets.QLabel(Dialog)
        self.password_label.setGeometry(QtCore.QRect(520, 320, 121, 31))

        font = QtGui.QFont()
        font.setFamily("Big Space")
        font.setPointSize(12)

        self.password_label.setFont(font)
        self.password_label.setObjectName("password_label")
        self.signup_pushButton = QtWidgets.QPushButton(Dialog, clicked=self.signUp)
        self.signup_pushButton.setGeometry(QtCore.QRect(520, 420, 101, 31))

        font = QtGui.QFont()
        font.setFamily("Fixedsys")
        font.setPointSize(12)

        self.signup_pushButton.setFont(font)
        self.signup_pushButton.setStyleSheet("QPushButton {background-color: rgb(255, 38, 38);\n"
"                        color:rgb(255,255,255);                    \n"
"}\n"
"QPushButton:hover {background-color: rgb(218, 167, 0);\n"
"}")
        self.signup_pushButton.setObjectName("signup_pushButton")
        self.login_pushButton = QtWidgets.QPushButton(Dialog, clicked = self.login)
        self.login_pushButton.setGeometry(QtCore.QRect(520, 380, 101, 31))

        font = QtGui.QFont()
        font.setFamily("Fixedsys")
        font.setPointSize(12)

        self.login_pushButton.setFont(font)
        self.login_pushButton.setStyleSheet("QPushButton {background-color: rgb(255, 38, 38);\n"
"                        color:rgb(255,255,255);                    \n"
"}\n"
"QPushButton:hover {background-color: rgb(218, 167, 0);\n"
"}")
        self.login_pushButton.setObjectName("login_pushButton")

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.login_bg.setText(_translate("Dialog", "<html><head/><body><p><img src=\":/login prefix/login.jpg\"/></p></body></html>"))
        self.username_input.setPlaceholderText(_translate("Dialog", "Insert Username"))
        self.password_input.setPlaceholderText(_translate("Dialog", "Inser Password"))
        self.username_label.setText(_translate("Dialog", "<html><head/><body><p align=\"center\"><span style=\" font-size:18pt; color:#ff2020;\">USERNAME</span></p></body></html>"))
        self.password_label.setText(_translate("Dialog", "<html><head/><body><p align=\"center\"><span style=\" font-size:18pt; color:#ff2020;\">PASSWORD</span></p></body></html>"))
        self.signup_pushButton.setText(_translate("Dialog", "Signup"))
        self.login_pushButton.setText(_translate("Dialog", "Login"))

import login_source_rc

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = Ui_Dialog()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())

