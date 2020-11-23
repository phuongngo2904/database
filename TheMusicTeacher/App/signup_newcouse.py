from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QMessageBox
from access_to_db import *

logger=record()
mydb= db()


class Ui_signup_newcourse(object):
    def __init__(self,id):
        logger.info('displayed courses to sign up')
        self.id=id
    def signup_button_clicked(self):
        for x in range(len(self.course_signup)):
            if self.course_signup.currentIndex()==x:
                mycursor = mydb.cursor()
                query = "INSERT INTO enrolled values (%s,%s,%s)"
                mycursor.execute(query, (self.id,self.s_id[x],self.c_id[x]))
                mydb.commit()
                logger.info('successfully insert a value into table enrolled')
                message = QMessageBox()
                message.setWindowTitle("Success")
                message.setText("Successfully signed up an.")
                message.exec()
                self.course_signup.clear()
                self.show_course()
    def show_course(self):
        self.c_id=[]
        self.s_id=[]
        mycursor = mydb.cursor()
        query = "select c.c_id,c.c_name,s.sec_id, u.fname from course c, section s ,user u " \
                "where c.i_id=u.u_id and c.c_id=s.c_id and c.active =1 and c.c_id NOT IN(" \
                "select c.c_id from course c, section s, user u, enrolled e " \
                "where  c.c_id=s.c_id and e.sec_id=s.sec_id and e.c_id=c.c_id and c.i_id = u.u_id and e.s_id=%s)"
        mycursor.execute(query, (self.id,))
        result = mycursor.fetchall()
        for x in result:
            self.c_id.append(x[0])
            self.s_id.append(x[2])
            self.course_signup.addItem(f"{x[1]}__Section({x[2]})__Professor({x[3]})")
    def setupUi(self, signup_newcourse):
        signup_newcourse.setObjectName("signup_newcourse")
        signup_newcourse.resize(815, 603)
        self.label = QtWidgets.QLabel(signup_newcourse)
        self.label.setGeometry(QtCore.QRect(0, 0, 811, 651))
        self.label.setText("")
        self.label.setPixmap(QtGui.QPixmap("Images/image_signup.jpg"))
        self.label.setScaledContents(True)
        self.label.setObjectName("label")
        self.label1 = QtWidgets.QLabel(signup_newcourse)
        self.label1.setGeometry(QtCore.QRect(20, 250, 81, 31))
        self.label1.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"font: 10pt \"Lemon\";\n"
"color: rgb(134, 15, 0);")
        self.label1.setObjectName("label1")
        self.course_signup = QtWidgets.QComboBox(signup_newcourse)
        self.course_signup.setGeometry(QtCore.QRect(110, 250, 691, 31))
        self.course_signup.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"font: 10pt \"Lemon\";\n"
"color: rgb(134, 15, 0);")
        self.course_signup.setObjectName("course_signup")
        #self.course_signup.addItem("")
        self.course_signup.setItemText(0, "")
        self.signup_button = QtWidgets.QPushButton(signup_newcourse)
        self.signup_button.setGeometry(QtCore.QRect(250, 330, 101, 31))
        font = QtGui.QFont()
        font.setFamily("Russo One")
        font.setPointSize(14)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.signup_button.setFont(font)
        self.signup_button.setStyleSheet("font: 14pt \"Russo One\";\n"
"color: rgb(255, 247, 128);\n"
"background-color: rgb(153, 0, 28);")
        self.signup_button.setObjectName("signup_button")
        self.exit_button = QtWidgets.QPushButton(signup_newcourse)
        self.exit_button.setGeometry(QtCore.QRect(410, 330, 101, 31))
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

        self.show_course()
        self.signup_button.clicked.connect(self.signup_button_clicked)
        self.exit_button.clicked.connect(signup_newcourse.close)

        self.retranslateUi(signup_newcourse)
        QtCore.QMetaObject.connectSlotsByName(signup_newcourse)

    def retranslateUi(self, signup_newcourse):
        _translate = QtCore.QCoreApplication.translate
        signup_newcourse.setWindowTitle(_translate("signup_newcourse", "Sign Up New Course"))
        self.label1.setText(_translate("signup_newcourse", "Courses"))
        self.signup_button.setText(_translate("signup_newcourse", "Sign Up"))
        self.exit_button.setText(_translate("signup_newcourse", "Exit"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    signup_newcourse = QtWidgets.QWidget()
    ui = Ui_signup_newcourse()
    ui.setupUi(signup_newcourse)
    signup_newcourse.show()
    sys.exit(app.exec_())
