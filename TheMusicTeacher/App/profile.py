from PyQt5 import QtCore, QtGui, QtWidgets
from access_to_db import *

logger=record()
mydb= db()

class Ui_profile(object):

    def __init__(self,id):
        logger.info('displayed user profile')
        self.id=id
        self.display_info()
    def display_info(self):
        mycursor = mydb.cursor()
        with open('../SQL/profile.sql') as f:
            commands = f.read().split(';')
        for command in commands:
            if command.find('Select username,fname,minit,lname,dob,gender') != -1:
               command = command.replace('@id', '%s')
               mycursor.execute(command, (self.id,))
               result = mycursor.fetchall()
               for x in result:
                   self.uid = x[0]
                   self.first = x[1]
                   self.minit = x[2]
                   self.last = x[3]
                   self.dateob = str(x[4])
                   self.u_gender = x[5]
                   self.cellphone = x[6]
                   self.lastlog = str(x[7])
    def setupUi(self, profile):
        profile.setObjectName("profile")
        profile.resize(677, 885)
        profile.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.userid_2 = QtWidgets.QLabel(profile)
        self.userid_2.setGeometry(QtCore.QRect(110, 270, 71, 31))
        self.userid_2.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"font: 10pt \"Lemon\";\n"
"color: rgb(134, 15, 0);")
        self.userid_2.setObjectName("userid_2")
        self.fname = QtWidgets.QLabel(profile)
        self.fname.setGeometry(QtCore.QRect(70, 320, 111, 31))
        self.fname.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"font: 10pt \"Lemon\";\n"
"color: rgb(134, 15, 0);")
        self.fname.setObjectName("fname")
        self.lname = QtWidgets.QLabel(profile)
        self.lname.setGeometry(QtCore.QRect(70, 370, 111, 31))
        self.lname.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"font: 10pt \"Lemon\";\n"
"color: rgb(134, 15, 0);")
        self.lname.setObjectName("lname")
        self.mname = QtWidgets.QLabel(profile)
        self.mname.setGeometry(QtCore.QRect(30, 420, 151, 31))
        self.mname.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"font: 10pt \"Lemon\";\n"
"color: rgb(134, 15, 0);")
        self.mname.setObjectName("mname")
        self.dateofbirth = QtWidgets.QLabel(profile)
        self.dateofbirth.setGeometry(QtCore.QRect(50, 520, 131, 31))
        self.dateofbirth.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"font: 10pt \"Lemon\";\n"
"color: rgb(134, 15, 0);")
        self.dateofbirth.setObjectName("dateofbirth")
        self.phone = QtWidgets.QLabel(profile)
        self.phone.setGeometry(QtCore.QRect(120, 570, 61, 31))
        self.phone.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"font: 10pt \"Lemon\";\n"
"color: rgb(134, 15, 0);")
        self.phone.setObjectName("phone")
        self.gender = QtWidgets.QLabel(profile)
        self.gender.setGeometry(QtCore.QRect(110, 470, 71, 31))
        self.gender.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"font: 10pt \"Lemon\";\n"
"color: rgb(134, 15, 0);")
        self.gender.setObjectName("gender")
        self.id = QtWidgets.QLabel(profile)
        self.id.setGeometry(QtCore.QRect(190, 270, 281, 31))
        self.id.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"font: 10pt \"Lemon\";\n"
"color: rgb(134, 15, 0);")
        self.id.setText(self.uid)
        self.id.setObjectName("id")
        self.first_name = QtWidgets.QLabel(profile)
        self.first_name.setGeometry(QtCore.QRect(190, 320, 221, 31))
        self.first_name.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"font: 10pt \"Lemon\";\n"
"color: rgb(134, 15, 0);")
        self.first_name.setText(self.first)
        self.first_name.setObjectName("first_name")
        self.last_name = QtWidgets.QLabel(profile)
        self.last_name.setGeometry(QtCore.QRect(190, 370, 221, 31))
        self.last_name.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"font: 10pt \"Lemon\";\n"
"color: rgb(134, 15, 0);")
        self.last_name.setText(self.last)
        self.last_name.setObjectName("last_name")
        self.mid_name = QtWidgets.QLabel(profile)
        self.mid_name.setGeometry(QtCore.QRect(190, 420, 221, 31))
        self.mid_name.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"font: 10pt \"Lemon\";\n"
"color: rgb(134, 15, 0);")
        self.mid_name.setText(self.minit)
        self.mid_name.setObjectName("mid_name")
        self.user_gender = QtWidgets.QLabel(profile)
        self.user_gender.setGeometry(QtCore.QRect(190, 470, 221, 31))
        self.user_gender.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"font: 10pt \"Lemon\";\n"
"color: rgb(134, 15, 0);")
        self.user_gender.setText(self.u_gender)
        self.user_gender.setObjectName("user_gender")
        self.dob = QtWidgets.QLabel(profile)
        self.dob.setGeometry(QtCore.QRect(190, 520, 221, 31))
        self.dob.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"font: 10pt \"Lemon\";\n"
"color: rgb(134, 15, 0);")
        self.dob.setText(self.dateob)
        self.dob.setObjectName("dob")
        self.phone_number = QtWidgets.QLabel(profile)
        self.phone_number.setGeometry(QtCore.QRect(190, 570, 221, 31))
        self.phone_number.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"font: 10pt \"Lemon\";\n"
"color: rgb(134, 15, 0);")
        self.phone_number.setText(self.cellphone)
        self.phone_number.setObjectName("phone_number")
        self.lastlogin = QtWidgets.QLabel(profile)
        self.lastlogin.setGeometry(QtCore.QRect(80, 620, 101, 31))
        self.lastlogin.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"font: 10pt \"Lemon\";\n"
"color: rgb(134, 15, 0);")
        self.lastlogin.setObjectName("lastlogin")
        self.last_log_in = QtWidgets.QLabel(profile)
        self.last_log_in.setGeometry(QtCore.QRect(190, 620, 241, 31))
        self.last_log_in.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"font: 10pt \"Lemon\";\n"
"color: rgb(134, 15, 0);")
        self.last_log_in.setText(self.lastlog)
        self.last_log_in.setObjectName("last_log_in")
        self.label = QtWidgets.QLabel(profile)
        self.label.setGeometry(QtCore.QRect(-100, 0, 851, 261))
        self.label.setText("")
        self.label.setPixmap(QtGui.QPixmap("Images/top.jpg"))
        self.label.setScaledContents(True)
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(profile)
        self.label_2.setGeometry(QtCore.QRect(10, 640, 651, 231))
        self.label_2.setText("")
        self.label_2.setPixmap(QtGui.QPixmap("Images/bottom.jpg"))
        self.label_2.setScaledContents(True)
        self.label_2.setObjectName("label_2")
        self.label_2.raise_()
        self.userid_2.raise_()
        self.fname.raise_()
        self.lname.raise_()
        self.mname.raise_()
        self.dateofbirth.raise_()
        self.phone.raise_()
        self.gender.raise_()
        self.id.raise_()
        self.first_name.raise_()
        self.last_name.raise_()
        self.mid_name.raise_()
        self.user_gender.raise_()
        self.dob.raise_()
        self.phone_number.raise_()
        self.lastlogin.raise_()
        self.last_log_in.raise_()
        self.label.raise_()

        self.retranslateUi(profile)
        QtCore.QMetaObject.connectSlotsByName(profile)

    def retranslateUi(self, profile):
        _translate = QtCore.QCoreApplication.translate
        profile.setWindowTitle(_translate("profile", "Profile"))
        self.userid_2.setText(_translate("profile", "UserId"))
        self.fname.setText(_translate("profile", "First name"))
        self.lname.setText(_translate("profile", "Last name"))
        self.mname.setText(_translate("profile", "Middile Initial"))
        self.dateofbirth.setText(_translate("profile", "Date of birth"))
        self.phone.setText(_translate("profile", "Phone"))
        self.gender.setText(_translate("profile", "Gender"))
        self.lastlogin.setText(_translate("profile", "Last Login"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    profile = QtWidgets.QWidget()
    ui = Ui_profile()
    ui.setupUi(profile)
    profile.show()
    sys.exit(app.exec_())
