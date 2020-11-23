from create_assignment import Ui_create_assign
from assignment_view import Ui_Assignment_Page
from create_course import Ui_create
from grade_teacher import Ui_ppgrade
from student import Ui_Student_view
from PyQt5 import QtCore, QtGui, QtWidgets
from access_to_db import *

logger=record()

class Ui_Teacher(object):
    def __init__(self,id):
        self.id=id
        logger.info('display teacher view')
    def refresh_button_clicked(self):
        self.display_course()
    def switch_button_clicked(self):
        logger.info('switch to student view')
        self.Student_view = QtWidgets.QWidget()
        self.ui = Ui_Student_view(self.id)
        self.ui.setupUi(self.Student_view)
        self.Student_view.show()
    def people_button_clicked(self):
        logger.info('open all students grade window')
        self.ppgrade = QtWidgets.QWidget()
        self.ui = Ui_ppgrade(self.array_not_dup)
        self.ui.setupUi(self.ppgrade)
        self.ppgrade.show()
    def create_assignment_clicked(self):
        logger.info('open create assignment window')
        self.create_assign = QtWidgets.QWidget()
        self.ui = Ui_create_assign(self.array_not_dup)
        self.ui.setupUi(self.create_assign)
        self.create_assign.show()
    def create_course_button_clicked(self):
        logger.info('open create course window')
        self.create = QtWidgets.QWidget()
        self.ui = Ui_create(self.id)
        self.ui.setupUi(self.create)
        self.create.show()

    def assignment_button_clicked(self):
        logger.info('open all assignments which has been created')
        self.Assignment_Page = QtWidgets.QWidget()
        self.ui = Ui_Assignment_Page(self.array_not_dup)
        self.ui.setupUi(self.Assignment_Page)
        self.Assignment_Page.show()
    def display_course(self):
        mydb = db()
        mycursor = mydb.cursor()
        query = "select c.c_id,c.c_name,s.sec_id,c.active from course c, section s where c.c_id = s.c_id and c.i_id=%s"
        mycursor.execute(query, (self.id,))
        result = mycursor.fetchall()
        row=0
        column=0
        index=1
        self.array_c_id=[]
        self.array_section=[]
        self.tableWidget.setRowCount(len(result))
        for x in result:
            self.array_c_id.append(x[0])
            self.tableWidget.setItem(row,column,QtWidgets.QTableWidgetItem(str(x[index])))
            self.tableWidget.setItem(row, column+1, QtWidgets.QTableWidgetItem(str(x[index+1])))
            self.array_section.append(x[index+1])
            if x[index+2]==1:
                self.tableWidget.setItem(row, column+2, QtWidgets.QTableWidgetItem("Active"))
            else:
                self.tableWidget.setItem(row, column + 2, QtWidgets.QTableWidgetItem("Non-Active"))
            row +=1

        self.array_not_dup=[]
        for i in self.array_c_id:
            if i not in self.array_not_dup:
                self.array_not_dup.append(i)
    def setupUi(self, Teacher):
        Teacher.setObjectName("Teacher")
        Teacher.resize(706, 799)
        Teacher.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.tableWidget = QtWidgets.QTableWidget(Teacher)
        self.tableWidget.setGeometry(QtCore.QRect(290, 300, 381, 491))
        self.tableWidget.setStyleSheet("background-color: rgb(255, 255, 255);\n"
                                     "font: 8pt \"Lemon\";\n"
                                     "color: rgb(134, 15, 0);")
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(3)
        self.tableWidget.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(2, item)
        self.groupBox = QtWidgets.QGroupBox(Teacher)
        self.groupBox.setGeometry(QtCore.QRect(50, 290, 201, 241))
        self.groupBox.setStyleSheet("font: 14pt \"Russo One\";\n"
"color: rgb(153, 0, 28);\n"
"background-color: rgb(255, 255, 255);")
        self.groupBox.setObjectName("groupBox")
        self.create_course_button = QtWidgets.QPushButton(self.groupBox)
        self.create_course_button.setGeometry(QtCore.QRect(10, 40, 181, 31))
        font = QtGui.QFont()
        font.setFamily("Russo One")
        font.setPointSize(14)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.create_course_button.setFont(font)
        self.create_course_button.setStyleSheet("font: 14pt \"Russo One\";\n"
"color: rgb(255, 247, 128);\n"
"background-color: rgb(153, 0, 28);")
        self.create_course_button.setObjectName("create_course_button")
        self.create_assignment = QtWidgets.QPushButton(self.groupBox)
        self.create_assignment.setGeometry(QtCore.QRect(10, 120, 181, 31))
        font = QtGui.QFont()
        font.setFamily("Russo One")
        font.setPointSize(10)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.create_assignment.setFont(font)
        self.create_assignment.setStyleSheet("font: 10pt \"Russo One\";\n"
"color: rgb(255, 247, 128);\n"
"background-color: rgb(153, 0, 28);")
        self.create_assignment.setObjectName("create_assignment")
        self.people_button = QtWidgets.QPushButton(self.groupBox)
        self.people_button.setGeometry(QtCore.QRect(10, 160, 181, 31))
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
        self.switch_button = QtWidgets.QPushButton(self.groupBox)
        self.switch_button.setGeometry(QtCore.QRect(10, 200, 181, 31))
        font = QtGui.QFont()
        font.setFamily("Russo One")
        font.setPointSize(14)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.switch_button.setFont(font)
        self.switch_button.setStyleSheet("font: 14pt \"Russo One\";\n"
"color: rgb(255, 247, 128);\n"
"background-color: rgb(153, 0, 28);")
        self.switch_button.setObjectName("switch_button")
        self.firstname = QtWidgets.QLabel(Teacher)
        self.firstname.setGeometry(QtCore.QRect(280, 260, 161, 31))
        self.firstname.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"font: 10pt \"Lemon\";\n"
"color: rgb(134, 15, 0);")
        self.firstname.setObjectName("firstname")
        self.label = QtWidgets.QLabel(Teacher)
        self.label.setGeometry(QtCore.QRect(-50, 0, 741, 311))
        self.label.setText("")
        self.label.setPixmap(QtGui.QPixmap("Images/teacher_view.jpg"))
        self.label.setScaledContents(True)
        self.label.setObjectName("label")

        self.f5_button = QtWidgets.QPushButton(Teacher)
        self.f5_button.setGeometry(QtCore.QRect(60, 550, 181, 31))
        font = QtGui.QFont()
        font.setFamily("Russo One")
        font.setPointSize(14)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.f5_button.setFont(font)
        self.f5_button.setStyleSheet("font: 14pt \"Russo One\";\n"
                                     "color: rgb(255, 247, 128);\n"
                                     "background-color: rgb(153, 0, 28);")
        self.f5_button.setObjectName("f5_button")

        self.label.raise_()
        self.tableWidget.raise_()
        self.groupBox.raise_()
        self.firstname.raise_()
        self.f5_button.raise_()

        self.display_course()
        self.f5_button.clicked.connect(self.refresh_button_clicked)
        self.create_course_button.clicked.connect(self.create_course_button_clicked)
        self.assignment_button.clicked.connect(self.assignment_button_clicked)
        self.create_assignment.clicked.connect(self.create_assignment_clicked)
        self.people_button.clicked.connect(self.people_button_clicked)
        self.switch_button.clicked.connect(self.switch_button_clicked)
        self.retranslateUi(Teacher)
        QtCore.QMetaObject.connectSlotsByName(Teacher)

    def retranslateUi(self, Teacher):
        _translate = QtCore.QCoreApplication.translate
        Teacher.setWindowTitle(_translate("Teacher", "Course"))
        item = self.tableWidget.horizontalHeaderItem(0)
        item.setText(_translate("Teacher", "Course"))
        item = self.tableWidget.horizontalHeaderItem(1)
        item.setText(_translate("Teacher", "Section"))
        item = self.tableWidget.horizontalHeaderItem(2)
        item.setText(_translate("Teacher", "Status"))
        self.groupBox.setTitle(_translate("Teacher", "Option"))
        self.create_course_button.setText(_translate("Teacher", "Create Course"))
        self.create_assignment.setText(_translate("Teacher", "Create Assignment"))
        self.people_button.setText(_translate("Teacher", "People"))
        self.assignment_button.setText(_translate("Teacher", "Assignment"))
        self.switch_button.setText(_translate("Teacher", "Switch View"))
        self.firstname.setText(_translate("Teacher", "Courses Created"))
        self.f5_button.setText(_translate("Teacher", "Refresh"))

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Teacher = QtWidgets.QWidget()
    ui = Ui_Teacher()
    ui.setupUi(Teacher)
    Teacher.show()
    sys.exit(app.exec_())
