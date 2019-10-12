from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QMessageBox, QApplication, QMainWindow, QPushButton
import pymysql, Signup
from Transaction import Ui_transactionWindow

class Ui_MainWindow(QMainWindow):

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
                        QMessageBox.about(self.MainWindow, "Login", "Successfully logged in!")
                        self.transact()  
                    else:
                        QMessageBox.about(self.MainWindow, "Login", "Invalid password!")
        else:
            QMessageBox.about(self.MainWindow, "Login", "Account does not exist in the database!")
            
    def signUp(self):
        self.ui = QtWidgets.QMainWindow()
        self.signup = Signup.Ui_signupWindow(self.MainWindow)
        self.signup.setupUi(self.ui)
        self.ui.show()
        self.MainWindow.hide()

    def transact(self):
        self.ui2 = QtWidgets.QMainWindow()
        self.transaction = Ui_transactionWindow(self)
        self.transaction.setupUi(self.ui2)
        self.ui2.show()
        self.MainWindow.hide()

    def keyPressEvent(self, event):
        if event.key() == QtCore.Qt.Key_Escape:
            self.MainWindow.close()
        elif event.key() == QtCore.Qt.Key_Return:
            self.login()
    
    def setupUi(self, MainWindow):
        self.MainWindow = MainWindow
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(720, 500)

        self.this_window = MainWindow

        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MainWindow.sizePolicy().hasHeightForWidth())

        MainWindow.setSizePolicy(sizePolicy)
        MainWindow.setMinimumSize(QtCore.QSize(720, 500))
        MainWindow.setMaximumSize(QtCore.QSize(720, 500))

        self.background = QtWidgets.QLabel(MainWindow)
        self.background.setGeometry(QtCore.QRect(0, 0, 720, 500))

        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.background.sizePolicy().hasHeightForWidth())

        self.background.setSizePolicy(sizePolicy)
        self.background.setMinimumSize(QtCore.QSize(720, 500))
        self.background.setMaximumSize(QtCore.QSize(720, 500))
        self.background.setObjectName("background")

        self.usernameInput = QtWidgets.QLineEdit(MainWindow)
        self.usernameInput.setGeometry(QtCore.QRect(50, 230, 361, 41))
        self.usernameInput.setStyleSheet("")
        self.usernameInput.setAlignment(QtCore.Qt.AlignCenter)
        self.usernameInput.setObjectName("usernameInput")

        self.passwordInput = QtWidgets.QLineEdit(MainWindow)
        self.passwordInput.setEchoMode(QtWidgets.QLineEdit.Password)
        self.passwordInput.setGeometry(QtCore.QRect(50, 310, 361, 41))
        self.passwordInput.setAlignment(QtCore.Qt.AlignCenter)
        self.passwordInput.setObjectName("passwordInput")

        self.usernameLabel = QtWidgets.QLabel(MainWindow)
        self.usernameLabel.setGeometry(QtCore.QRect(520, 240, 121, 31))

        font = QtGui.QFont()
        font.setFamily("Big Space")
        font.setPointSize(12)

        self.usernameLabel.setFont(font)
        self.usernameLabel.setObjectName("usernameLabel")
        self.passwordLabel = QtWidgets.QLabel(MainWindow)
        self.passwordLabel.setGeometry(QtCore.QRect(520, 320, 121, 31))

        font = QtGui.QFont()
        font.setFamily("Big Space")
        font.setPointSize(12)

        self.passwordLabel.setFont(font)
        self.passwordLabel.setObjectName("passwordLabel")
        self.loginButton = QtWidgets.QPushButton(MainWindow, clicked=self.login)
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

        self.signUpButton = QtWidgets.QPushButton(MainWindow, clicked=self.signUp)
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

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

        MainWindow.keyPressEvent = self.keyPressEvent

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("Dialog", "Dialog"))
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
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
