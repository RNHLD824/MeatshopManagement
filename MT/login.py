from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QMainWindow, QMessageBox
import pymysql # < ---- MYSQL
from signup import Ui_Dialog as signUpWindow # <--- ITO UNG ISANG WINDOW NA GAGAMITIN MO PARA MAOPEN SA SIGNUP

class Ui_Dialog(QMainWindow):

    # OPEN SIGN UP WINDOW FUNCTION
    def openSignUpWindow(self):
        self.window = QtWidgets.QMainWindow()
        self.ui = signUpWindow()
        self.ui.setupUi(self.window)
        self.window.show()

    # LOGIN FUNCTION
    def Login(self):
        self.password = self.uname_lineEdit_2.text()
        self.username = self.uname_lineEdit_3.text()

        if (self.username != "" and self.password != ""):
            conn = pymysql.connect("localhost", "root", "", "meat_prices")
            cursor = conn.cursor()
            query = "SELECT * FROM admin"
            cursor.execute(query)
            result = cursor.fetchall()
            accounts = {} # ACCOUNTS CONTAINER DICTIONARY

            # UNG FOR LOOP NA ITO, INOORGANIZE LANG NYA UNG accounts MULA SA result
            for account_number in range(0, len(result)):
                accounts[result[account_number][0]] = result[account_number]

            # DITO MANGYAYARI UNG CONDITIONS KUNG MERON BANG NAGEEXIST SA DB NA ACCOUNT
            if (self.username in accounts):
                if (self.password == accounts[self.username][1]):
                    QMessageBox.about(self, "Login", "Successfuly logged in!")
                else:
                    QMessageBox.about(self, "Login", "Invalid password!")
            else:
                QMessageBox.about(self, "Login", "Login failed!")
        else:
            QMessageBox.about(self, "Login", "Invalid input!")
        
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(720, 500)
        Dialog.setMinimumSize(QtCore.QSize(720, 500))
        Dialog.setMaximumSize(QtCore.QSize(720, 500))
        Dialog.setStyleSheet("background-color: rgb(255, 97, 66);")
        self.u_name_label = QtWidgets.QLabel(Dialog)
        self.u_name_label.setGeometry(QtCore.QRect(150, 200, 111, 31))
        font = QtGui.QFont()
        font.setFamily("MS Shell Dlg 2")
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        self.u_name_label.setFont(font)
        self.u_name_label.setStyleSheet("background-color: rgb(255, 193, 46);")
        self.u_name_label.setAlignment(QtCore.Qt.AlignCenter)
        self.u_name_label.setObjectName("u_name_label")
        self.pass_label = QtWidgets.QLabel(Dialog)
        self.pass_label.setGeometry(QtCore.QRect(150, 260, 111, 31))
        font = QtGui.QFont()
        font.setFamily("MS Shell Dlg 2")
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        self.pass_label.setFont(font)
        self.pass_label.setStyleSheet("background-color: rgb(255, 193, 46);")
        self.pass_label.setAlignment(QtCore.Qt.AlignCenter)
        self.pass_label.setObjectName("pass_label")
        
        self.login_btn = QtWidgets.QPushButton(Dialog) # < -- LOGIN BUTTON
        self.login_btn.clicked.connect(self.Login) # <---- Login button click calls function self.Login()
        
        self.login_btn.setGeometry(QtCore.QRect(240, 340, 81, 31))
        self.login_btn.setStyleSheet("background-color: rgb(255, 193, 46);")
        self.login_btn.setObjectName("login_btn")
        
        self.signup_btn = QtWidgets.QPushButton(Dialog) # < ---- ITO UNG SIGN UP BUTTON
        self.signup_btn.clicked.connect(self.openSignUpWindow) # <---- Open ung isang window na sign up
        
        self.signup_btn.setGeometry(QtCore.QRect(360, 340, 81, 31))
        self.signup_btn.setStyleSheet("background-color: rgb(255, 193, 46);")
        self.signup_btn.setObjectName("signup_btn")
        self.label = QtWidgets.QLabel(Dialog)
        self.label.setGeometry(QtCore.QRect(0, 0, 721, 91))
        font = QtGui.QFont()
        font.setFamily("Papyrus")
        font.setPointSize(35)
        font.setBold(False)
        font.setUnderline(True)
        font.setWeight(50)
        self.label.setFont(font)
        self.label.setStyleSheet("background-color: rgb(255, 193, 46);")
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.uname_lineEdit_2 = QtWidgets.QLineEdit(Dialog)
        self.uname_lineEdit_2.setGeometry(QtCore.QRect(330, 260, 281, 31))
        self.uname_lineEdit_2.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.uname_lineEdit_2.setObjectName("uname_lineEdit_2")
        self.uname_lineEdit_3 = QtWidgets.QLineEdit(Dialog)
        self.uname_lineEdit_3.setGeometry(QtCore.QRect(330, 200, 281, 31))
        self.uname_lineEdit_3.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.uname_lineEdit_3.setObjectName("uname_lineEdit_3")
        self.uname_lineEdit_2.setEchoMode(QtWidgets.QLineEdit.Password)

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.u_name_label.setText(_translate("Dialog", "USERNAME "))
        self.pass_label.setText(_translate("Dialog", "PASSWORD"))
        self.login_btn.setText(_translate("Dialog", "Login"))
        self.signup_btn.setText(_translate("Dialog", "Sign Up"))
        self.label.setText(_translate("Dialog", "Noemi\'s Meatshop"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = Ui_Dialog()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())
