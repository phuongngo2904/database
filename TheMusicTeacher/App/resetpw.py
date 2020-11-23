from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QMessageBox
import hashlib
from access_to_db import *

mydb= db()
logger=record()
mycursor = mydb.cursor()

class Ui_resetpw(object):

    def confirm_button_clicked(self):
        if self.newpw_lineedit.text() != self.confirmpw_lineedit.text():
            self.confirmpw_lineedit.clear()
            message = QMessageBox()
            message.setWindowTitle("FAIL")
            message.setText("Ooops! Password don't match.")
            logger.warning('Password dont match')
            message.exec()
        elif self.newpw_lineedit.text() == self.confirmpw_lineedit.text():
            self.hash_pw = hashlib.sha1(self.confirmpw_lineedit.text().encode("UTF-8")).hexdigest()
            with open('../SQL/resetpw.sql') as f:
                commands = f.read().split(';')
            for command in commands:
                if command.find('UPDATE user SET hashed_password') != -1:
                   command = command.replace('@hashed_pw', '%s')
                   command = command.replace('@username','%s')
                   mycursor.execute(command, (self.hash_pw, self.id_lineedit.text()))
                   mydb.commit()
                   message = QMessageBox()
                   message.setWindowTitle("Success")
                   message.setText("Successfully reset password.")
                   logger.info('Password has been reset')
                   message.exec()
                   self.newpw_lineedit.clear()
                   self.confirmpw_lineedit.clear()
    def check_button_clicked(self):
        with open('../SQL/resetpw.sql') as f:
            commands = f.read().split(';')
        for command in commands:
            if command.find('SELECT username FROM') != -1:
               command = command.replace('@usname', '%s')
               mycursor.execute(command, (self.id_lineedit.text(),))
               result = mycursor.fetchall()
               if len(result) == 0:
                   self.id_lineedit.clear()
                   message = QMessageBox()
                   message.setWindowTitle("FAIL !")
                   message.setText("Invalid user.")
                   message.exec()
                   logger.warning('User not found')
               else:
                   message = QMessageBox()
                   message.setWindowTitle("Success")
                   message.setText("Valid User.")
                   message.exec()
                   logger.info('User found')
               self.confirm_button.clicked.connect(self.confirm_button_clicked)

    def setupUi(self, resetpw):
        resetpw.setObjectName("resetpw")
        resetpw.resize(969, 794)
        resetpw.setStyleSheet("background-color: rgb(244, 244, 244);")
        self.userid = QtWidgets.QLabel(resetpw)
        self.userid.setGeometry(QtCore.QRect(240, 320, 131, 31))
        self.userid.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"font: 18pt \"Lemon\";\n"
"color: rgb(134, 15, 0);")
        self.userid.setObjectName("userid")
        self.id_lineedit = QtWidgets.QLineEdit(resetpw)
        self.id_lineedit.setGeometry(QtCore.QRect(380, 320, 341, 31))
        self.id_lineedit.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"font: 10pt \"Lemon\";\n"
"color: rgb(134, 15, 0);")
        self.id_lineedit.setObjectName("id_lineedit")
        self.label = QtWidgets.QLabel(resetpw)
        self.label.setGeometry(QtCore.QRect(-10, 10, 921, 761))
        self.label.setText("")
        self.label.setPixmap(QtGui.QPixmap("Images/resetpw.jpg"))
        self.label.setScaledContents(True)
        self.label.setObjectName("label")
        self.newpw = QtWidgets.QLabel(resetpw)
        self.newpw.setGeometry(QtCore.QRect(180, 380, 201, 31))
        self.newpw.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"font: 14pt \"Lemon\";\n"
"color: rgb(134, 15, 0);")
        self.newpw.setObjectName("newpw")
        self.newpw_lineedit = QtWidgets.QLineEdit(resetpw)
        self.newpw_lineedit.setGeometry(QtCore.QRect(380, 380, 341, 31))
        self.newpw_lineedit.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"font: 10pt \"Lemon\";\n"
"color: rgb(134, 15, 0);")
        self.newpw_lineedit.setObjectName("newpw_lineedit")
        self.confirm_pw = QtWidgets.QLabel(resetpw)
        self.confirm_pw.setGeometry(QtCore.QRect(210, 430, 161, 31))
        self.confirm_pw.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"font: 14pt \"Lemon\";\n"
"color: rgb(134, 15, 0);")
        self.confirm_pw.setObjectName("confirm_pw")
        self.confirmpw_lineedit = QtWidgets.QLineEdit(resetpw)
        self.confirmpw_lineedit.setGeometry(QtCore.QRect(380, 430, 341, 31))
        self.confirmpw_lineedit.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"font: 10pt \"Lemon\";\n"
"color: rgb(134, 15, 0);")
        self.confirmpw_lineedit.setObjectName("confirmpw_lineedit")
        self.confirm_button = QtWidgets.QPushButton(resetpw)
        self.confirm_button.setGeometry(QtCore.QRect(320, 510, 101, 31))
        font = QtGui.QFont()
        font.setFamily("Russo One")
        font.setPointSize(14)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.confirm_button.setFont(font)
        self.confirm_button.setStyleSheet("font: 14pt \"Russo One\";\n"
"color: rgb(255, 247, 128);\n"
"background-color: rgb(153, 0, 28);")
        self.confirm_button.setObjectName("confirm_button")
        self.exit_button = QtWidgets.QPushButton(resetpw)
        self.exit_button.setGeometry(QtCore.QRect(520, 510, 101, 31))
        font = QtGui.QFont()
        font.setFamily("Russo One")
        font.setPointSize(14)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.exit_button.setFont(font)
        self.exit_button.setStyleSheet("font: 14pt \"Russo One\";\n"
"color: rgb(255, 247, 128);\n"
"background-color: rgb(153, 0, 28);")
        self.exit_button.setObjectName("exit_button")
        self.check_button = QtWidgets.QPushButton(resetpw)
        self.check_button.setGeometry(QtCore.QRect(740, 320, 101, 31))
        font = QtGui.QFont()
        font.setFamily("Russo One")
        font.setPointSize(14)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.check_button.setFont(font)
        self.check_button.setStyleSheet("font: 14pt \"Russo One\";\n"
"color: rgb(255, 247, 128);\n"
"background-color: rgb(153, 0, 28);")
        self.check_button.setObjectName("check_button")
        self.label.raise_()
        self.userid.raise_()
        self.id_lineedit.raise_()
        self.newpw.raise_()
        self.newpw_lineedit.raise_()
        self.confirm_pw.raise_()
        self.confirmpw_lineedit.raise_()
        self.confirm_button.raise_()
        self.exit_button.raise_()
        self.check_button.raise_()

        self.exit_button.clicked.connect(resetpw.close)
        self.check_button.clicked.connect(self.check_button_clicked)
        self.retranslateUi(resetpw)
        QtCore.QMetaObject.connectSlotsByName(resetpw)

    def retranslateUi(self, resetpw):
        _translate = QtCore.QCoreApplication.translate
        resetpw.setWindowTitle(_translate("resetpw", "Reset Password"))
        self.userid.setText(_translate("resetpw", "User Id"))
        self.newpw.setText(_translate("resetpw", "New Password"))
        self.confirm_pw.setText(_translate("resetpw", "Confirm PW"))
        self.confirm_button.setText(_translate("resetpw", "Confirm"))
        self.exit_button.setText(_translate("resetpw", "Exit"))
        self.check_button.setText(_translate("resetpw", "Check"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    resetpw = QtWidgets.QWidget()
    ui = Ui_resetpw()
    ui.setupUi(resetpw)
    resetpw.show()
    sys.exit(app.exec_())
