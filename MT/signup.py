from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QMainWindow, QMessageBox
import pymysql


class Ui_Dialog(QMainWindow):

    def anyNameFunction(self):
        conn = pymysql.connect("localhost", "root", "", "meat_prices")
        cursor = conn.cursor()
        
        self.username = self.uname_lineEdit.text()
        self.password = self.uname_lineEdit_3.text()
        self.email_id = self.uname_lineEdit_2.text()

        if (self.username != "" and self.password != "" and self.email_id != ""):
            query = "INSERT INTO admin (username, password, email_id) VALUES (\"%s\", \"%s\", \"%s\")" %(self.username, self.password, self.email_id)
            cursor.execute(query)
            QMessageBox.about(self, "Sign Up", "You have created an account!")
            conn.commit()
            cursor.close()
            self.Dialog.close()
        else:
            QMessageBox.about(self, "Sign Up", "Invalid input!")

    def setupUi(self, Dialog):
        self.Dialog = Dialog
        Dialog.setObjectName("Dialog")
        Dialog.resize(720, 500)
        Dialog.setMinimumSize(QtCore.QSize(720, 500))
        Dialog.setMaximumSize(QtCore.QSize(720, 500))
        font = QtGui.QFont()
        font.setFamily("Papyrus")
        Dialog.setFont(font)
        Dialog.setStyleSheet("background-color: rgb(255, 97, 66);")
        self.label = QtWidgets.QLabel(Dialog)
        self.label.setGeometry(QtCore.QRect(130, 170, 81, 31))
        font = QtGui.QFont()
        font.setFamily("Tahoma")
        font.setPointSize(10)
        self.label.setFont(font)
        self.label.setStyleSheet("background-color: rgb(255, 193, 46);")
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(Dialog)
        self.label_2.setGeometry(QtCore.QRect(130, 230, 81, 31))
        font = QtGui.QFont()
        font.setFamily("Tahoma")
        font.setPointSize(10)
        self.label_2.setFont(font)
        self.label_2.setStyleSheet("background-color: rgb(255, 193, 46);")
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(Dialog)
        self.label_3.setGeometry(QtCore.QRect(130, 290, 81, 31))
        font = QtGui.QFont()
        font.setFamily("Tahoma")
        font.setPointSize(10)
        self.label_3.setFont(font)
        self.label_3.setStyleSheet("background-color: rgb(255, 193, 46);")
        self.label_3.setObjectName("label_3")
        self.uname_lineEdit = QtWidgets.QLineEdit(Dialog)
        self.uname_lineEdit.setGeometry(QtCore.QRect(300, 170, 311, 31))
        self.uname_lineEdit.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.uname_lineEdit.setObjectName("uname_lineEdit")

        
        self.signup_btn = QtWidgets.QPushButton(Dialog)

        self.signup_btn.clicked.connect(self.anyNameFunction)
        
        self.signup_btn.setGeometry(QtCore.QRect(300, 370, 111, 41))
        font = QtGui.QFont()
        font.setFamily("Tahoma")
        font.setPointSize(10)
        self.signup_btn.setFont(font)
        self.signup_btn.setStyleSheet("background-color: rgb(255, 193, 46);")
        self.signup_btn.setObjectName("signup_btn")
        self.label_4 = QtWidgets.QLabel(Dialog)
        self.label_4.setGeometry(QtCore.QRect(0, 0, 721, 91))
        font = QtGui.QFont()
        font.setFamily("Papyrus")
        font.setPointSize(35)
        font.setBold(False)
        font.setUnderline(True)
        font.setWeight(50)
        self.label_4.setFont(font)
        self.label_4.setStyleSheet("background-color: rgb(255, 193, 46);")
        self.label_4.setAlignment(QtCore.Qt.AlignCenter)
        self.label_4.setObjectName("label_4")
        self.uname_lineEdit_2 = QtWidgets.QLineEdit(Dialog)
        self.uname_lineEdit_2.setGeometry(QtCore.QRect(300, 290, 311, 31))
        self.uname_lineEdit_2.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.uname_lineEdit_2.setObjectName("uname_lineEdit_2")
        self.uname_lineEdit_3 = QtWidgets.QLineEdit(Dialog)
        self.uname_lineEdit_3.setGeometry(QtCore.QRect(300, 230, 311, 31))
        self.uname_lineEdit_3.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.uname_lineEdit_3.setObjectName("uname_lineEdit_3")
        self.uname_lineEdit_3.setEchoMode(QtWidgets.QLineEdit.Password)

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.label.setText(_translate("Dialog", "  USERNAME"))
        self.label_2.setText(_translate("Dialog", " PASSWORD"))
        self.label_3.setText(_translate("Dialog", "  EMAIL ID"))
        self.signup_btn.setText(_translate("Dialog", "Sign Up"))
        self.label_4.setText(_translate("Dialog", "Create Account"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = Ui_Dialog()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())
