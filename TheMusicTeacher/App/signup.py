from PyQt5.QtWidgets import QMessageBox
import hashlib
import datetime
from PyQt5 import QtCore, QtGui, QtWidgets
from access_to_db import *

logger= record()
mydb= db()




class Ui_register_window(object):
    def confirm_button_clicked(self):
        mycursor = mydb.cursor()
        query_for_uid= "Select max(u_id) from user"
        mycursor.execute(query_for_uid)
        result1 = mycursor.fetchall()
        x=list(result1[0])
        self.id=x[0]+1
        self.stt=True
        now = datetime.datetime.now()
        self.date_created = now.strftime('%Y-%m-%d %H:%M:%S')
        self.last_login = now.strftime('%Y-%m-%d %H:%M:%S')
        if self.valid_user ==True:
            if self.sex_m.isChecked() == True:
                self.sex_g = 'M'
            elif self.sex_female.isChecked() == True:
                self.sex_g = 'F'
            self.hash_pw=hashlib.sha1(self.password_lineedit.text().encode("UTF-8")).hexdigest()
            query = "INSERT INTO user values (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"
            mycursor.execute(query, (self.id,self.username_lineedit.text(), self.email_lineedit.text(), self.fname_lineedit.text(),
                                     self.mname_lineedit.text(),self.lname_lineedit.text(),self.dob_lineedit.text(),
                                     self.sex_g,self.phone_lineedit.text(),self.date_created,self.last_login,self.stt,self.hash_pw))
            mydb.commit()
            message = QMessageBox()
            message.setWindowTitle("Success")
            message.setText("Successfully signed up.")
            message.exec()
            logger.info('successfully inserted new user into table user')
    def check_button_clicked(self):
        mycursor = mydb.cursor()
        query = "SELECT username FROM user WHERE username = %s"
        mycursor.execute(query, (self.username_lineedit.text(),))
        result = mycursor.fetchall()
        if len(result)==0 and self.username_lineedit.text() != "":
            self.valid_user =True
            message = QMessageBox()
            message.setWindowTitle("Success!")
            message.setText("Valid user.")
            message.exec()
            logger.info('Valid User Name')
        elif len(result)==0 and self.username_lineedit.text()=="":
            self.valid_user = False
            self.username_lineedit.clear()
            message = QMessageBox()
            message.setWindowTitle("Fail!")
            message.setText("Invalid username.")
            message.exec()
            logger.info('Invalid User Name')
        elif len(result)>0 and self.username_lineedit.text()!="":
            self.valid_user = False
            self.username_lineedit.clear()
            message = QMessageBox()
            message.setWindowTitle("Fail!")
            message.setText("Username is already used.")
            message.exec()
            logger.info('Username is already used')
    def setupUi(self, register_window):
        register_window.setObjectName("register_window")
        register_window.resize(836, 859)
        register_window.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.label = QtWidgets.QLabel(register_window)
        self.label.setGeometry(QtCore.QRect(-20, -10, 691, 861))
        self.label.setText("")
        self.label.setPixmap(QtGui.QPixmap("Images/register.jpg"))
        self.label.setScaledContents(True)
        self.label.setObjectName("label")
        self.firstname = QtWidgets.QLabel(register_window)
        self.firstname.setGeometry(QtCore.QRect(280, 150, 111, 31))
        self.firstname.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"font: 10pt \"Lemon\";\n"
"color: rgb(134, 15, 0);")
        self.firstname.setObjectName("firstname")
        self.fname_lineedit = QtWidgets.QLineEdit(register_window)
        self.fname_lineedit.setGeometry(QtCore.QRect(400, 150, 301, 31))
        self.fname_lineedit.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"font: 10pt \"Lemon\";\n"
"color: rgb(134, 15, 0);")
        self.fname_lineedit.setObjectName("fname_lineedit")
        self.lastname = QtWidgets.QLabel(register_window)
        self.lastname.setGeometry(QtCore.QRect(280, 200, 111, 31))
        self.lastname.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"font: 10pt \"Lemon\";\n"
"color: rgb(134, 15, 0);")
        self.lastname.setObjectName("lastname")
        self.lname_lineedit = QtWidgets.QLineEdit(register_window)
        self.lname_lineedit.setGeometry(QtCore.QRect(400, 200, 301, 31))
        self.lname_lineedit.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"font: 10pt \"Lemon\";\n"
"color: rgb(134, 15, 0);")
        self.lname_lineedit.setObjectName("lname_lineedit")
        self.middlename = QtWidgets.QLabel(register_window)
        self.middlename.setGeometry(QtCore.QRect(260, 250, 131, 31))
        self.middlename.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"font: 10pt \"Lemon\";\n"
"color: rgb(134, 15, 0);")
        self.middlename.setObjectName("middlename")
        self.mname_lineedit = QtWidgets.QLineEdit(register_window)
        self.mname_lineedit.setGeometry(QtCore.QRect(400, 250, 301, 31))
        self.mname_lineedit.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"font: 10pt \"Lemon\";\n"
"color: rgb(134, 15, 0);")
        self.mname_lineedit.setObjectName("mname_lineedit")
        self.dateofbirth = QtWidgets.QLabel(register_window)
        self.dateofbirth.setGeometry(QtCore.QRect(330, 300, 41, 31))
        self.dateofbirth.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"font: 10pt \"Lemon\";\n"
"color: rgb(134, 15, 0);")
        self.dateofbirth.setObjectName("dateofbirth")
        self.dob_lineedit = QtWidgets.QLineEdit(register_window)
        self.dob_lineedit.setGeometry(QtCore.QRect(400, 300, 301, 31))
        self.dob_lineedit.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"font: 10pt \"Lemon\";\n"
"color: rgb(134, 15, 0);")
        self.dob_lineedit.setObjectName("dob_lineedit")
        self.email = QtWidgets.QLabel(register_window)
        self.email.setGeometry(QtCore.QRect(320, 360, 61, 31))
        self.email.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"font: 10pt \"Lemon\";\n"
"color: rgb(134, 15, 0);")
        self.email.setObjectName("email")
        self.email_lineedit = QtWidgets.QLineEdit(register_window)
        self.email_lineedit.setGeometry(QtCore.QRect(400, 360, 301, 31))
        self.email_lineedit.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"font: 10pt \"Lemon\";\n"
"color: rgb(134, 15, 0);")
        self.email_lineedit.setObjectName("email_lineedit")
        self.gender = QtWidgets.QLabel(register_window)
        self.gender.setGeometry(QtCore.QRect(310, 410, 71, 31))
        self.gender.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"font: 10pt \"Lemon\";\n"
"color: rgb(134, 15, 0);")
        self.gender.setObjectName("gender")
        self.sex_m = QtWidgets.QRadioButton(register_window)
        self.sex_m.setGeometry(QtCore.QRect(430, 420, 71, 20))
        self.sex_m.setStyleSheet("font: 10pt \"Lemon\";\n"
"color: rgb(134, 15, 0);")
        self.sex_m.setObjectName("sex_m")
        self.sex_female = QtWidgets.QRadioButton(register_window)
        self.sex_female.setGeometry(QtCore.QRect(550, 420, 101, 20))
        self.sex_female.setStyleSheet("font: 10pt \"Lemon\";\n"
"color: rgb(134, 15, 0);")
        self.sex_female.setObjectName("sex_female")
        self.username = QtWidgets.QLabel(register_window)
        self.username.setGeometry(QtCore.QRect(290, 510, 101, 31))
        self.username.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"font: 10pt \"Lemon\";\n"
"color: rgb(134, 15, 0);")
        self.username.setObjectName("username")
        self.username_lineedit = QtWidgets.QLineEdit(register_window)
        self.username_lineedit.setGeometry(QtCore.QRect(400, 510, 301, 31))
        self.username_lineedit.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"font: 10pt \"Lemon\";\n"
"color: rgb(134, 15, 0);")
        self.username_lineedit.setObjectName("username_lineedit")
        self.check_button = QtWidgets.QPushButton(register_window)
        self.check_button.setGeometry(QtCore.QRect(710, 510, 81, 31))
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
        self.password = QtWidgets.QLabel(register_window)
        self.password.setGeometry(QtCore.QRect(290, 560, 101, 31))
        self.password.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"font: 10pt \"Lemon\";\n"
"color: rgb(134, 15, 0);")
        self.password.setObjectName("password")
        self.password_lineedit = QtWidgets.QLineEdit(register_window)
        self.password_lineedit.setGeometry(QtCore.QRect(400, 560, 301, 31))
        self.password_lineedit.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"font: 10pt \"Lemon\";\n"
"color: rgb(134, 15, 0);")
        self.password_lineedit.setObjectName("password_lineedit")
        self.confirm_button = QtWidgets.QPushButton(register_window)
        self.confirm_button.setGeometry(QtCore.QRect(380, 610, 101, 31))
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
        self.exit_button_2 = QtWidgets.QPushButton(register_window)
        self.exit_button_2.setGeometry(QtCore.QRect(600, 610, 101, 31))
        font = QtGui.QFont()
        font.setFamily("Russo One")
        font.setPointSize(14)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.exit_button_2.setFont(font)
        self.exit_button_2.setStyleSheet("font: 14pt \"Russo One\";\n"
"color: rgb(255, 247, 128);\n"
"background-color: rgb(153, 0, 28);")
        self.exit_button_2.setObjectName("exit_button_2")
        self.phone = QtWidgets.QLabel(register_window)
        self.phone.setGeometry(QtCore.QRect(310, 460, 81, 31))
        self.phone.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"font: 10pt \"Lemon\";\n"
"color: rgb(134, 15, 0);")
        self.phone.setObjectName("phone")
        self.phone_lineedit = QtWidgets.QLineEdit(register_window)
        self.phone_lineedit.setGeometry(QtCore.QRect(400, 460, 301, 31))
        self.phone_lineedit.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"font: 10pt \"Lemon\";\n"
"color: rgb(134, 15, 0);")
        self.phone_lineedit.setObjectName("phone_lineedit")

        self.confirm_button.clicked.connect(self.confirm_button_clicked)
        self.check_button.clicked.connect(self.check_button_clicked)
        self.exit_button_2.clicked.connect(register_window.close)

        self.retranslateUi(register_window)
        QtCore.QMetaObject.connectSlotsByName(register_window)

    def retranslateUi(self, register_window):
        _translate = QtCore.QCoreApplication.translate
        register_window.setWindowTitle(_translate("register_window", "Register"))
        self.firstname.setText(_translate("register_window", "First Name"))
        self.lastname.setText(_translate("register_window", "Last Name"))
        self.middlename.setText(_translate("register_window", "Middle Name"))
        self.dateofbirth.setText(_translate("register_window", "DoB"))
        self.email.setText(_translate("register_window", "Email"))
        self.gender.setText(_translate("register_window", "Gender"))
        self.sex_m.setText(_translate("register_window", "Male"))
        self.sex_female.setText(_translate("register_window", "Female"))
        self.username.setText(_translate("register_window", "Username"))
        self.check_button.setText(_translate("register_window", "Check"))
        self.password.setText(_translate("register_window", "Password"))
        self.confirm_button.setText(_translate("register_window", "Confirm"))
        self.exit_button_2.setText(_translate("register_window", "Exit"))
        self.phone.setText(_translate("register_window", "Phone #"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    register_window = QtWidgets.QWidget()
    ui = Ui_register_window()
    ui.setupUi(register_window)
    register_window.show()
    sys.exit(app.exec_())
