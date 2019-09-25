from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QMessageBox
import pymysql, Signup

class Ui_Dialog:

    def login(self):
        username = self.usernameInput.text()
        password = self.passwordInput.text()
        conn = pymysql.connect("localhost", "root", "", "meatshopdb")
        cursor = conn.cursor()
        query = "SELECT Username, Password FROM admin"
        cursor.execute(query)
        result = cursor.fetchall()
        accounts = {}

        for account in result:
            accounts[account[0]] = account[1]

        if username in accounts:
            for account in accounts:
                if username == account:
                    if password == accounts[account]:
                        QMessageBox.about(self.Dialog, "Login", "Successfully logged in!")
                    else:
                        QMessageBox.about(self.Dialog, "Login", "Invalid password!")
        else:
            QMessageBox.about(self.Dialog, "Login", "Account does not exist in the database!")
            
    def signUp(self):
        self.ui = QtWidgets.QMainWindow()
        self.signup = Signup.Ui_Dialog(self.Dialog)
        self.signup.setupUi(self.ui)
        self.ui.show()
        self.Dialog.hide()

    def pressEvent(self, event):
        if event.key() == QtCore.Qt.Key_Escape:
            self.Dialog.close()
    
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
        self.background = QtWidgets.QLabel(Dialog)
        self.background.setGeometry(QtCore.QRect(0, 0, 720, 500))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.background.sizePolicy().hasHeightForWidth())
        self.background.setSizePolicy(sizePolicy)
        self.background.setMinimumSize(QtCore.QSize(720, 500))
        self.background.setMaximumSize(QtCore.QSize(720, 500))
        self.background.setObjectName("background")
        self.usernameInput = QtWidgets.QLineEdit(Dialog)
        self.usernameInput.setGeometry(QtCore.QRect(50, 230, 361, 41))
        self.usernameInput.setStyleSheet("")
        self.usernameInput.setAlignment(QtCore.Qt.AlignCenter)
        self.usernameInput.setObjectName("usernameInput")
        self.passwordInput = QtWidgets.QLineEdit(Dialog)
        self.passwordInput.setEchoMode(QtWidgets.QLineEdit.Password)
        self.passwordInput.setGeometry(QtCore.QRect(50, 310, 361, 41))
        self.passwordInput.setAlignment(QtCore.Qt.AlignCenter)
        self.passwordInput.setObjectName("passwordInput")
        self.usernameLabel = QtWidgets.QLabel(Dialog)
        self.usernameLabel.setGeometry(QtCore.QRect(520, 240, 121, 31))
        font = QtGui.QFont()
        font.setFamily("Big Space")
        font.setPointSize(12)
        self.usernameLabel.setFont(font)
        self.usernameLabel.setObjectName("usernameLabel")
        self.passwordLabel = QtWidgets.QLabel(Dialog)
        self.passwordLabel.setGeometry(QtCore.QRect(520, 320, 121, 31))
        font = QtGui.QFont()
        font.setFamily("Big Space")
        font.setPointSize(12)
        self.passwordLabel.setFont(font)
        self.passwordLabel.setObjectName("passwordLabel")
        self.loginButton = QtWidgets.QPushButton(Dialog, clicked=self.login)
        self.loginButton.setGeometry(QtCore.QRect(520, 380, 101, 31))
        font = QtGui.QFont()
        font.setFamily("Fixedsys")
        font.setPointSize(12)
        self.loginButton.setFont(font)
        self.loginButton.setStyleSheet("QPushButton {background-color: rgb(255, 38, 38);\n"
"                        color:rgb(255,255,255);                    \n"
"}\n"
"QPushButton:hover {background-color: rgb(218, 167, 0);\n"
"}")
        self.loginButton.setObjectName("loginButton")
        self.signUpButton = QtWidgets.QPushButton(Dialog, clicked=self.signUp)
        self.signUpButton.setGeometry(QtCore.QRect(520, 420, 101, 31))
        font = QtGui.QFont()
        font.setFamily("Fixedsys")
        font.setPointSize(12)
        self.signUpButton.setFont(font)
        self.signUpButton.setStyleSheet("QPushButton {background-color: rgb(255, 38, 38);\n"
"                        color:rgb(255,255,255);                    \n"
"}\n"
"QPushButton:hover {background-color: rgb(218, 167, 0);\n"
"}")
        self.signUpButton.setObjectName("signUpButton")

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.background.setText(_translate("Dialog", "<html><head/><body><p><img src=\":/login prefix/login.jpg\"/></p></body></html>"))
        self.usernameInput.setPlaceholderText(_translate("Dialog", "Insert Username"))
        self.passwordInput.setPlaceholderText(_translate("Dialog", "Inser Password"))
        self.usernameLabel.setText(_translate("Dialog", "<html><head/><body><p align=\"center\"><span style=\" font-size:18pt; color:#ff2020;\">USERNAME</span></p></body></html>"))
        self.passwordLabel.setText(_translate("Dialog", "<html><head/><body><p align=\"center\"><span style=\" font-size:18pt; color:#ff2020;\">PASSWORD</span></p></body></html>"))
        self.loginButton.setText(_translate("Dialog", "Log In"))
        self.signUpButton.setText(_translate("Dialog", "Sign Up"))
import login_source_rc


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = Ui_Dialog()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())
