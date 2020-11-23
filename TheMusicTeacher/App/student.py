from PyQt5 import QtCore, QtGui, QtWidgets
from signup_newcouse import Ui_signup_newcourse
from student_grade import Ui_mygrade
from student_w_samecourse import Ui_people_samecourse
from access_to_db import *

logger=record()



class Ui_Student_view(object):
    def __init__(self, id):
        logger.info('displayed student view')
        self.id = id
    def refresh_button_clicked(self):
        logger.info('refresh the table')
        self.display_course()
    def people_button_clicked(self):
        logger.info('open students who take the same course window')
        self.people_samecourse = QtWidgets.QWidget()
        self.ui = Ui_people_samecourse(self.id)
        self.ui.setupUi(self.people_samecourse)
        self.people_samecourse.show()
    def view_my_grade_clicked(self):
        logger.info('open student grade window')
        self.mygrade = QtWidgets.QWidget()
        self.ui = Ui_mygrade(self.id)
        self.ui.setupUi(self.mygrade)
        self.mygrade.show()
    def add_button_clicked(self):
        logger.info('open Sign Up New Course window')
        self.signup_newcourse = QtWidgets.QWidget()
        self.ui = Ui_signup_newcourse(self.id)
        self.ui.setupUi(self.signup_newcourse)
        self.signup_newcourse.show()
    def display_course(self):
        mydb = db()
        mycursor = mydb.cursor()
        row = 0
        column = 0
        query="select c.c_name, s.sec_id, u.fname, c.active from course c, section s, user u, enrolled e " \
              "where c.c_id=s.c_id and e.sec_id=s.sec_id and e.c_id=c.c_id and c.i_id = u.u_id and e.s_id=%s"
        mycursor.execute(query, (self.id,))
        result = mycursor.fetchall()
        self.course_taking.setRowCount(len(result))
        for x in result:
            self.course_taking.setItem(row,column,QtWidgets.QTableWidgetItem(x[0]))
            self.course_taking.setItem(row, column+1, QtWidgets.QTableWidgetItem(x[1]))
            self.course_taking.setItem(row, column+2, QtWidgets.QTableWidgetItem(x[2]))
            if x[3]==1:
                self.course_taking.setItem(row, column+3, QtWidgets.QTableWidgetItem("active"))
            elif x[3]==0 or x[3]==None:
                self.course_taking.setItem(row, column+3, QtWidgets.QTableWidgetItem("non-active"))
            row+=1
    def setupUi(self, Student_view):
        Student_view.setObjectName("Student_view")
        Student_view.resize(891, 796)
        Student_view.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.label = QtWidgets.QLabel(Student_view)
        self.label.setGeometry(QtCore.QRect(0, 0, 871, 351))
        self.label.setText("")
        self.label.setPixmap(QtGui.QPixmap("Images/teacher_view.jpg"))
        self.label.setScaledContents(True)
        self.label.setObjectName("label")
        self.groupBox = QtWidgets.QGroupBox(Student_view)
        self.groupBox.setGeometry(QtCore.QRect(80, 320, 201, 161))
        self.groupBox.setStyleSheet("font: 14pt \"Russo One\";\n"
"color: rgb(153, 0, 28);\n"
"background-color: rgb(255, 255, 255);")
        self.groupBox.setObjectName("groupBox")
        self.add_button = QtWidgets.QPushButton(self.groupBox)
        self.add_button.setGeometry(QtCore.QRect(10, 40, 181, 31))
        font = QtGui.QFont()
        font.setFamily("Russo One")
        font.setPointSize(10)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.add_button.setFont(font)
        self.add_button.setStyleSheet("font: 10pt \"Russo One\";\n"
"color: rgb(255, 247, 128);\n"
"background-color: rgb(153, 0, 28);")
        self.add_button.setObjectName("add_button")
        self.people_button = QtWidgets.QPushButton(self.groupBox)
        self.people_button.setGeometry(QtCore.QRect(10, 120, 181, 31))
        font = QtGui.QFont()
        font.setFamily("Russo One")
        font.setPointSize(14)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.people_button.setFont(font)
        self.people_button.setStyleSheet("font: 14pt \"Russo One\";\n"
"color: rgb(255, 247, 128);\n"
"background-color: rgb(153, 0, 28);")
        self.people_button.setObjectName("people_button")
        self.assignment_button = QtWidgets.QPushButton(self.groupBox)
        self.assignment_button.setGeometry(QtCore.QRect(10, 80, 181, 31))
        font = QtGui.QFont()
        font.setFamily("Russo One")
        font.setPointSize(14)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.assignment_button.setFont(font)
        self.assignment_button.setStyleSheet("font: 14pt \"Russo One\";\n"
"color: rgb(255, 247, 128);\n"
"background-color: rgb(153, 0, 28);")
        self.assignment_button.setObjectName("assignment_button")
        self.course_taking = QtWidgets.QTableWidget(Student_view)
        self.course_taking.setGeometry(QtCore.QRect(370, 300, 511, 491))
        self.course_taking.setStyleSheet("background-color: rgb(255, 255, 255);\n"
                                     "font: 8pt \"Lemon\";\n"
                                     "color: rgb(134, 15, 0);")
        self.course_taking.setObjectName("course_taking")
        self.course_taking.setColumnCount(4)
        self.course_taking.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.course_taking.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.course_taking.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.course_taking.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.course_taking.setHorizontalHeaderItem(3, item)
        self.label_2 = QtWidgets.QLabel(Student_view)
        self.label_2.setGeometry(QtCore.QRect(370, 260, 151, 31))
        self.label_2.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"font: 10pt \"Lemon\";\n"
"color: rgb(134, 15, 0);")
        self.label_2.setObjectName("label_2")

        self.refresh_button = QtWidgets.QPushButton(Student_view)
        self.refresh_button.setGeometry(QtCore.QRect(90, 520, 181, 31))
        font = QtGui.QFont()
        font.setFamily("Russo One")
        font.setPointSize(14)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.refresh_button.setFont(font)
        self.refresh_button.setStyleSheet("font: 14pt \"Russo One\";\n"
                                     "color: rgb(255, 247, 128);\n"
                                     "background-color: rgb(153, 0, 28);")
        self.refresh_button.setObjectName("refresh_button")

        self.display_course()
        self.refresh_button.clicked.connect(self.refresh_button_clicked)
        self.add_button.clicked.connect(self.add_button_clicked)
        self.assignment_button.clicked.connect(self.view_my_grade_clicked)
        self.people_button.clicked.connect(self.people_button_clicked)
        self.retranslateUi(Student_view)
        QtCore.QMetaObject.connectSlotsByName(Student_view)

    def retranslateUi(self, Student_view):
        _translate = QtCore.QCoreApplication.translate
        Student_view.setWindowTitle(_translate("Student_view", "Course (Student view)"))
        self.groupBox.setTitle(_translate("Student_view", "Option"))
        self.add_button.setText(_translate("Student_view", "Sign Up new course"))
        self.people_button.setText(_translate("Student_view", "People"))
        self.assignment_button.setText(_translate("Student_view", "View Grade"))
        item = self.course_taking.horizontalHeaderItem(0)
        item.setText(_translate("Student_view", "Course"))
        item = self.course_taking.horizontalHeaderItem(1)
        item.setText(_translate("Student_view", "Section"))
        item = self.course_taking.horizontalHeaderItem(2)
        item.setText(_translate("Student_view", "Instructor"))
        item = self.course_taking.horizontalHeaderItem(3)
        item.setText(_translate("Student_view", "Status"))
        self.label_2.setText(_translate("Student_view", "Courses Taking"))
        self.refresh_button.setText(_translate("Student_view", "Refresh"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Student_view = QtWidgets.QWidget()
    ui = Ui_Student_view()
    ui.setupUi(Student_view)
    Student_view.show()
    sys.exit(app.exec_())
