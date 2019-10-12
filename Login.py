from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_loginWindow(object):
    def setupUi(self, loginWindow):

        loginWindow.setObjectName("loginWindow")
        loginWindow.resize(720, 500)

        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(loginWindow.sizePolicy().hasHeightForWidth())

        loginWindow.setSizePolicy(sizePolicy)
        loginWindow.setMinimumSize(QtCore.QSize(720, 500))
        loginWindow.setMaximumSize(QtCore.QSize(720, 500))

        self.centralwidget = QtWidgets.QWidget(loginWindow)
        self.centralwidget.setObjectName("centralwidget")

        self.login_bg = QtWidgets.QLabel(self.centralwidget)
        self.login_bg.setGeometry(QtCore.QRect(0, 0, 720, 500))

        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.login_bg.sizePolicy().hasHeightForWidth())

        self.login_bg.setSizePolicy(sizePolicy)
        self.login_bg.setMinimumSize(QtCore.QSize(720, 500))
        self.login_bg.setMaximumSize(QtCore.QSize(720, 500))
        self.login_bg.setObjectName("login_bg")

        self.usernameInput = QtWidgets.QLineEdit(self.centralwidget)
        self.usernameInput.setGeometry(QtCore.QRect(50, 230, 361, 41))
        self.usernameInput.setStyleSheet("")
        self.usernameInput.setAlignment(QtCore.Qt.AlignCenter)
        self.usernameInput.setObjectName("usernameInput")

        self.passwordInput = QtWidgets.QLineEdit(self.centralwidget)
        self.passwordInput.setGeometry(QtCore.QRect(50, 320, 361, 41))
        self.passwordInput.setAlignment(QtCore.Qt.AlignCenter)
        self.passwordInput.setObjectName("passwordInput")

        self.usernameLabel = QtWidgets.QLabel(self.centralwidget)
        self.usernameLabel.setGeometry(QtCore.QRect(510, 240, 121, 31))

        font = QtGui.QFont()
        font.setFamily("Big Space")
        font.setPointSize(12)

        self.usernameLabel.setFont(font)
        self.usernameLabel.setObjectName("usernameLabel")
        self.passwordLabel = QtWidgets.QLabel(self.centralwidget)
        self.passwordLabel.setGeometry(QtCore.QRect(510, 330, 121, 31))

        font = QtGui.QFont()
        font.setFamily("Big Space")
        font.setPointSize(12)

        self.passwordLabel.setFont(font)
        self.passwordLabel.setObjectName("passwordLabel")

        self.loginButton = QtWidgets.QPushButton(self.centralwidget)
        self.loginButton.setGeometry(QtCore.QRect(480, 380, 101, 31))

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

        self.signUpButton = QtWidgets.QPushButton(self.centralwidget)
        self.signUpButton.setGeometry(QtCore.QRect(480, 420, 101, 31))

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

        loginWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(loginWindow)
        QtCore.QMetaObject.connectSlotsByName(loginWindow)

    def retranslateUi(self, loginWindow):
        _translate = QtCore.QCoreApplication.translate
        loginWindow.setWindowTitle(_translate("loginWindow", "MainWindow"))
        self.login_bg.setText(_translate("loginWindow", "<html><head/><body><p><img src=\":/login prefix/login.jpg\"/></p></body></html>"))
        self.usernameInput.setPlaceholderText(_translate("loginWindow", "Insert Username"))
        self.passwordInput.setPlaceholderText(_translate("loginWindow", "Inser Password"))
        self.usernameLabel.setText(_translate("loginWindow", "<html><head/><body><p align=\"center\"><span style=\" font-size:18pt; color:#ff2020;\">USERNAME</span></p></body></html>"))
        self.passwordLabel.setText(_translate("loginWindow", "<html><head/><body><p align=\"center\"><span style=\" font-size:18pt; color:#ff2020;\">PASSWORD</span></p></body></html>"))
        self.loginButton.setText(_translate("loginWindow", "Log In"))
        self.signUpButton.setText(_translate("loginWindow", "Sign Up"))

import login_source_rc

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    loginWindow = QtWidgets.QMainWindow()
    ui = Ui_loginWindow()
    ui.setupUi(loginWindow)
    loginWindow.show()
    sys.exit(app.exec_())

