from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Dialog(object):

    def __init__(self, Login):
        self.login = Login
        
    def goBack(self):
        self.Dialog.hide()
        self.login.show()
    
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
        self.signup_bg = QtWidgets.QLabel(Dialog)
        self.signup_bg.setGeometry(QtCore.QRect(0, 0, 720, 500))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.signup_bg.sizePolicy().hasHeightForWidth())
        self.signup_bg.setSizePolicy(sizePolicy)
        self.signup_bg.setMinimumSize(QtCore.QSize(720, 500))
        self.signup_bg.setMaximumSize(QtCore.QSize(720, 500))
        self.signup_bg.setObjectName("signup_bg")
        self.username_input = QtWidgets.QLineEdit(Dialog)
        self.username_input.setGeometry(QtCore.QRect(280, 170, 361, 41))
        self.username_input.setStyleSheet("")
        self.username_input.setAlignment(QtCore.Qt.AlignCenter)
        self.username_input.setObjectName("username_input")
        self.password_input = QtWidgets.QLineEdit(Dialog)
        self.password_input.setGeometry(QtCore.QRect(280, 250, 361, 41))
        self.password_input.setStyleSheet("")
        self.password_input.setAlignment(QtCore.Qt.AlignCenter)
        self.password_input.setObjectName("password_input")
        self.contact_input = QtWidgets.QLineEdit(Dialog)
        self.contact_input.setGeometry(QtCore.QRect(280, 330, 361, 41))
        self.contact_input.setStyleSheet("")
        self.contact_input.setAlignment(QtCore.Qt.AlignCenter)
        self.contact_input.setObjectName("contact_input")
        self.username_label = QtWidgets.QLabel(Dialog)
        self.username_label.setGeometry(QtCore.QRect(30, 170, 121, 31))
        font = QtGui.QFont()
        font.setFamily("Big Space")
        font.setPointSize(12)
        self.username_label.setFont(font)
        self.username_label.setObjectName("username_label")
        self.password_label = QtWidgets.QLabel(Dialog)
        self.password_label.setGeometry(QtCore.QRect(30, 260, 121, 31))
        font = QtGui.QFont()
        font.setFamily("Big Space")
        font.setPointSize(12)
        self.password_label.setFont(font)
        self.password_label.setObjectName("password_label")
        self.contact_label = QtWidgets.QLabel(Dialog)
        self.contact_label.setGeometry(QtCore.QRect(30, 340, 121, 31))
        font = QtGui.QFont()
        font.setFamily("Big Space")
        font.setPointSize(12)
        self.contact_label.setFont(font)
        self.contact_label.setObjectName("contact_label")
        self.submit_pushButton = QtWidgets.QPushButton(Dialog)
        self.submit_pushButton.setGeometry(QtCore.QRect(310, 390, 101, 31))
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
        self.back_pushButton = QtWidgets.QPushButton(Dialog, clicked=self.goBack)
        self.back_pushButton.setGeometry(QtCore.QRect(310, 430, 101, 31))
        font = QtGui.QFont()
        font.setFamily("Fixedsys")
        self.back_pushButton.setFont(font)
        self.back_pushButton.setStyleSheet("QPushButton {background-color: rgb(255, 38, 38);\n"
"                        color:rgb(255,255,255);                                \n"
"}\n"
"QPushButton:hover {background-color: rgb(218, 167, 0);\n"
"}")
        self.back_pushButton.setObjectName("back_pushButton")

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.signup_bg.setText(_translate("Dialog", "<html><head/><body><p><img src=\":/signup prefix/signup.jpg\"/></p></body></html>"))
        self.username_input.setPlaceholderText(_translate("Dialog", "Insert Username"))
        self.password_input.setPlaceholderText(_translate("Dialog", "Insert Password"))
        self.contact_input.setPlaceholderText(_translate("Dialog", "Insert Contact Number"))
        self.username_label.setText(_translate("Dialog", "<html><head/><body><p align=\"center\"><span style=\" font-size:16pt; color:#ff2020;\">USERNAME</span></p></body></html>"))
        self.password_label.setText(_translate("Dialog", "<html><head/><body><p align=\"center\"><span style=\" font-size:16pt; color:#ff2020;\">PASSWORD</span></p></body></html>"))
        self.contact_label.setText(_translate("Dialog", "<html><head/><body><p align=\"center\"><span style=\" font-size:16pt; color:#ff2020;\">CONTACT</span></p></body></html>"))
        self.submit_pushButton.setText(_translate("Dialog", "Submit"))
        self.back_pushButton.setText(_translate("Dialog", "Back"))
import signup_source_rc


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = Ui_Dialog()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())
