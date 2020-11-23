from PyQt5 import QtCore, QtGui, QtWidgets
from profile import Ui_profile
from message_win import Ui_msg
from teacher_view import Ui_Teacher
from acctess_to_a_lib import Ui_lib
from student import Ui_Student_view
from inbox import Ui_inbox
import datetime
from access_to_db import *

logger=record()
mydb= db()
mycursor = mydb.cursor()

class Ui_student_dashboard(object):
    def __init__(self,id):
        logger.info('display user dashboard')
        self.id=id
        self.update_last_login()
    def library_button_clicked(self):
        self.lib = QtWidgets.QWidget()
        self.ui = Ui_lib(self.id)
        self.ui.setupUi(self.lib)
        self.lib.show()
        logger.info('open library window')
    def course_button_clicked(self):
        with open('../SQL/user_dashboard.sql') as f:
            commands = f.read().split(';')
        for command in commands:
            if command.find('SELECT i_id from course') != -1:
               command = command.replace('@user_id', '%s')
               mycursor.execute(command,(self.id,))
               result= mycursor.fetchall()
               if(len(result))==0:
                    logger.info('display courses which student is taking')
                    self.Student_view = QtWidgets.QWidget()
                    self.ui = Ui_Student_view(self.id)
                    self.ui.setupUi(self.Student_view)
                    self.Student_view.show()
               elif len(result)!=0:
                     logger.info('display courses which teachers created')
                     self.Teacher = QtWidgets.QWidget()
                     self.ui = Ui_Teacher(self.id)
                     self.ui.setupUi(self.Teacher)
                     self.Teacher.show()
            else: pass
    def update_last_login(self):
        now = datetime.datetime.now()
        self.last_login = now.strftime('%Y-%m-%d %H:%M:%S')
        with open('../SQL/user_dashboard.sql') as f:
            commands = f.read().split(';')
        for command in commands:
            if command.find('UPDATE user SET') != -1:
               command = command.replace('@id', '%s')
               mycursor.execute(command, (self.last_login,self.id))
               mydb.commit()
               logger.info('last_login time has been updated')
            else: pass
    def inbox_button_clicked(self):
        logger.info('open inbox window')
        self.inbox = QtWidgets.QWidget()
        self.ui = Ui_inbox(self.id)
        self.ui.setupUi(self.inbox)
        self.inbox.show()

    def message_button_clicked(self):
        logger.info('open message window')
        self.msg = QtWidgets.QWidget()
        self.ui = Ui_msg(self.id)
        self.ui.setupUi(self.msg)
        self.msg.show()

    def profile_button_clicked(self):
        logger.info('display user profile')
        self.profile = QtWidgets.QWidget()
        self.ui = Ui_profile(self.id)
        self.ui.setupUi(self.profile)
        self.profile.show()

    def setupUi(self, student_dashboard):
        student_dashboard.setObjectName("student_dashboard")
        student_dashboard.resize(671, 694)
        student_dashboard.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.label = QtWidgets.QLabel(student_dashboard)
        self.label.setGeometry(QtCore.QRect(30, 10, 641, 401))
        self.label.setText("")
        self.label.setPixmap(QtGui.QPixmap("Images/user_login.jpg"))
        self.label.setScaledContents(True)
        self.label.setObjectName("label")
        self.DB = QtWidgets.QGroupBox(student_dashboard)
        self.DB.setGeometry(QtCore.QRect(10, 410, 201, 241))
        self.DB.setStyleSheet("font: 10pt \"Lemon\";\n"
"color: rgb(134, 15, 0);\n"
"background-color: rgb(157, 159, 255);")
        self.DB.setObjectName("DB")
        self.profile_button = QtWidgets.QPushButton(self.DB)
        self.profile_button.setGeometry(QtCore.QRect(10, 40, 171, 31))
        font = QtGui.QFont()
        font.setFamily("Russo One")
        font.setPointSize(14)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.profile_button.setFont(font)
        self.profile_button.setStyleSheet("font: 14pt \"Russo One\";\n"
"color: rgb(255, 247, 128);\n"
"background-color: rgb(153, 0, 28);")
        self.profile_button.setObjectName("profile_button")
        self.library_button = QtWidgets.QPushButton(self.DB)
        self.library_button.setGeometry(QtCore.QRect(10, 80, 171, 31))
        font = QtGui.QFont()
        font.setFamily("Russo One")
        font.setPointSize(14)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.library_button.setFont(font)
        self.library_button.setStyleSheet("font: 14pt \"Russo One\";\n"
"color: rgb(255, 247, 128);\n"
"background-color: rgb(153, 0, 28);")
        self.library_button.setObjectName("library_button")
        self.message_button = QtWidgets.QPushButton(self.DB)
        self.message_button.setGeometry(QtCore.QRect(10, 120, 171, 31))
        font = QtGui.QFont()
        font.setFamily("Russo One")
        font.setPointSize(13)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.message_button.setFont(font)
        self.message_button.setStyleSheet("font: 13pt \"Russo One\";\n"
"color: rgb(255, 247, 128);\n"
"background-color: rgb(153, 0, 28);")
        self.message_button.setObjectName("message_button")
        self.course_button = QtWidgets.QPushButton(self.DB)
        self.course_button.setGeometry(QtCore.QRect(10, 200, 171, 31))
        font = QtGui.QFont()
        font.setFamily("Russo One")
        font.setPointSize(12)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.course_button.setFont(font)
        self.course_button.setStyleSheet("font: 12pt \"Russo One\";\n"
"color: rgb(255, 247, 128);\n"
"background-color: rgb(153, 0, 28);")
        self.course_button.setObjectName("course_button")
        self.inbox_button = QtWidgets.QPushButton(self.DB)
        self.inbox_button.setGeometry(QtCore.QRect(10, 160, 171, 31))
        font = QtGui.QFont()
        font.setFamily("Russo One")
        font.setPointSize(13)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.inbox_button.setFont(font)
        self.inbox_button.setStyleSheet("font: 13pt \"Russo One\";\n"
"color: rgb(255, 247, 128);\n"
"background-color: rgb(153, 0, 28);")
        self.inbox_button.setObjectName("inbox_button")
        self.calendar = QtWidgets.QCalendarWidget(student_dashboard)
        self.calendar.setGeometry(QtCore.QRect(250, 400, 392, 236))
        self.calendar.setFirstDayOfWeek(QtCore.Qt.Monday)
        self.calendar.setGridVisible(True)
        self.calendar.setSelectionMode(QtWidgets.QCalendarWidget.SingleSelection)
        self.calendar.setHorizontalHeaderFormat(QtWidgets.QCalendarWidget.ShortDayNames)
        self.calendar.setVerticalHeaderFormat(QtWidgets.QCalendarWidget.NoVerticalHeader)
        self.calendar.setNavigationBarVisible(True)
        self.calendar.setDateEditEnabled(True)
        self.calendar.setObjectName("calendar")

        self.library_button.clicked.connect(self.library_button_clicked)
        self.profile_button.clicked.connect(self.profile_button_clicked)
        self.message_button.clicked.connect(self.message_button_clicked)
        self.inbox_button.clicked.connect(self.inbox_button_clicked)
        self.course_button.clicked.connect(self.course_button_clicked)
        self.retranslateUi(student_dashboard)
        QtCore.QMetaObject.connectSlotsByName(student_dashboard)

    def retranslateUi(self, student_dashboard):
        _translate = QtCore.QCoreApplication.translate
        student_dashboard.setWindowTitle(_translate("student_dashboard", "DashBoard"))
        self.DB.setTitle(_translate("student_dashboard", "Dashboard"))
        self.profile_button.setText(_translate("student_dashboard", "Profile"))
        self.library_button.setText(_translate("student_dashboard", "Library"))
        self.message_button.setText(_translate("student_dashboard", "Message"))
        self.course_button.setText(_translate("student_dashboard", "Courses"))
        self.inbox_button.setText(_translate("student_dashboard", "Inbox"))

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    student_dashboard = QtWidgets.QWidget()
    ui = Ui_student_dashboard()
    ui.setupUi(student_dashboard)
    student_dashboard.show()
    sys.exit(app.exec_())
