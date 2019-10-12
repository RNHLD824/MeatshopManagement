from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QMessageBox, QApplication, QMainWindow, QPushButton
import pymysql

class Ui_signupWindow:

    def __init__(self, Login):
        self.login = Login
        
    def goBack(self):
        self.signupWindow.hide()
        self.login.this_window.show()

    def checkAccount(self, username):
        conn = pymysql.connect("localhost", "root", "", "meatshopdb")
        with conn:
            cursor = conn.cursor()
            query = "SELECT Username, Password FROM admin"
            cursor.execute(query)
            result = cursor.fetchall()
            accounts = {}
            for account in result:
                accounts[account[0]] = account[1]
            if username in accounts:
                return 1
            else:
                return 0
        return 0
        
    def submitAccount(self):
        username = self.username_input.text()
        password = self.password_input.text()
        contact = self.contact_input.text()
        conn = pymysql.connect("localhost", "root", "", "meatshopdb")
        try:
            with conn:
                cursor = conn.cursor()
                if username != "" and password != "" and contact != "":
                    if self.checkAccount(username):
                        QMessageBox.about(self.signupWindow, "Sign Up", "Username already exists!")
                        return None
                    else:
                        QMessageBox.about(self.signupWindow, "Sign Up", "Account created successfully!")
                        query = "INSERT INTO admin VALUES ('{0}', '{1}', '{2}')".format(username, password, contact)
                        self.goBack()
                    cursor.execute(query)
                    conn.commit()
                    cursor.close()
                else:
                    QMessageBox.about(self.signupWindow, "Sign Up", "Please fill all the blank!")
        except:
            print("Error!")
            return None
        return None

    def setupUi(self, signupWindow):

        self.signupWindow = signupWindow
        
        signupWindow.setObjectName("signupWindow")
        signupWindow.resize(720, 500)

        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(signupWindow.sizePolicy().hasHeightForWidth())

        signupWindow.setSizePolicy(sizePolicy)
        signupWindow.setMinimumSize(QtCore.QSize(720, 500))
        signupWindow.setMaximumSize(QtCore.QSize(720, 500))

        self.centralwidget = QtWidgets.QWidget(signupWindow)
        self.centralwidget.setObjectName("centralwidget")

        self.signup_bg = QtWidgets.QLabel(self.centralwidget)
        self.signup_bg.setGeometry(QtCore.QRect(0, 0, 720, 500))

        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.signup_bg.sizePolicy().hasHeightForWidth())

        self.signup_bg.setSizePolicy(sizePolicy)
        self.signup_bg.setMinimumSize(QtCore.QSize(720, 500))
        self.signup_bg.setMaximumSize(QtCore.QSize(720, 500))
        self.signup_bg.setObjectName("signup_bg")

        self.username_label = QtWidgets.QLabel(self.centralwidget)
        self.username_label.setGeometry(QtCore.QRect(60, 170, 121, 31))

        font = QtGui.QFont()
        font.setFamily("Big Space")
        font.setPointSize(12)

        self.username_label.setFont(font)
        self.username_label.setObjectName("username_label")
        self.password_label = QtWidgets.QLabel(self.centralwidget)
        self.password_label.setGeometry(QtCore.QRect(60, 250, 121, 31))

        font = QtGui.QFont()
        font.setFamily("Big Space")
        font.setPointSize(12)

        self.password_label.setFont(font)
        self.password_label.setObjectName("password_label")
        self.contact_label = QtWidgets.QLabel(self.centralwidget)
        self.contact_label.setGeometry(QtCore.QRect(60, 340, 121, 31))

        font = QtGui.QFont()
        font.setFamily("Big Space")
        font.setPointSize(12)

        self.contact_label.setFont(font)
        self.contact_label.setObjectName("contact_label")

        self.username_input = QtWidgets.QLineEdit(self.centralwidget)
        self.username_input.setGeometry(QtCore.QRect(290, 170, 361, 41))
        self.username_input.setStyleSheet("")
        self.username_input.setAlignment(QtCore.Qt.AlignCenter)
        self.username_input.setObjectName("username_input")

        self.password_input = QtWidgets.QLineEdit(self.centralwidget)
        self.password_input.setEchoMode(QtWidgets.QLineEdit.Password)    
        self.password_input.setGeometry(QtCore.QRect(290, 250, 361, 41))
        self.password_input.setStyleSheet("")
        self.password_input.setAlignment(QtCore.Qt.AlignCenter)
        self.password_input.setObjectName("password_input")

        self.contact_input = QtWidgets.QLineEdit(self.centralwidget)
        self.contact_input.setGeometry(QtCore.QRect(290, 340, 361, 41))
        self.contact_input.setStyleSheet("")
        self.contact_input.setAlignment(QtCore.Qt.AlignCenter)
        self.contact_input.setObjectName("contact_input")

        self.submit_pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.submit_pushButton.setGeometry(QtCore.QRect(310, 400, 101, 31))

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
        self.submit_pushButton.clicked.connect(self.submitAccount)

        self.back_pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.back_pushButton.setGeometry(QtCore.QRect(310, 440, 101, 31))

        font = QtGui.QFont()
        font.setFamily("Fixedsys")

        self.back_pushButton.setFont(font)
        self.back_pushButton.setStyleSheet("QPushButton {background-color: rgb(255, 38, 38);\n"
"                        color:rgb(255,255,255);                                \n"
"}\n"
"QPushButton:hover {background-color: rgb(218, 167, 0);\n"
"}")
        self.back_pushButton.setObjectName("back_pushButton")
        self.back_pushButton.clicked.connect(self.goBack)

        signupWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(signupWindow)
        QtCore.QMetaObject.connectSlotsByName(signupWindow)

    def retranslateUi(self, signupWindow):
        _translate = QtCore.QCoreApplication.translate
        signupWindow.setWindowTitle(_translate("signupWindow", "MainWindow"))
        self.signup_bg.setText(_translate("signupWindow", "<html><head/><body><p><img src=\":/signup prefix/signup.jpg\"/></p></body></html>"))
        self.username_label.setText(_translate("signupWindow", "<html><head/><body><p align=\"center\"><span style=\" font-size:16pt; color:#ff2020;\">USERNAME</span></p></body></html>"))
        self.password_label.setText(_translate("signupWindow", "<html><head/><body><p align=\"center\"><span style=\" font-size:16pt; color:#ff2020;\">PASSWORD</span></p></body></html>"))
        self.contact_label.setText(_translate("signupWindow", "<html><head/><body><p align=\"center\"><span style=\" font-size:16pt; color:#ff2020;\">CONTACT</span></p></body></html>"))
        self.username_input.setPlaceholderText(_translate("signupWindow", "Insert Username"))
        self.password_input.setPlaceholderText(_translate("signupWindow", "Insert Password"))
        self.contact_input.setPlaceholderText(_translate("signupWindow", "Insert Contact Number"))
        self.submit_pushButton.setText(_translate("signupWindow", "Submit"))
        self.back_pushButton.setText(_translate("signupWindow", "Back"))

import signup_source_rc

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    signupWindow = QtWidgets.QMainWindow()
    ui = Ui_signupWindow()
    ui.setupUi(signupWindow)
    signupWindow.show()
    sys.exit(app.exec_())

