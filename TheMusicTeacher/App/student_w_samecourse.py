from PyQt5 import QtCore, QtGui, QtWidgets
from access_to_db import *

logger=record()
mydb= db()

class Ui_people_samecourse(object):
    def __init__(self,id):
        logger.info('displayed users classmate')
        self.id=id
    def display_people_take_samecourse(self):
        mycursor = mydb.cursor()
        query = "select c.c_name,s.sec_id,u.fname,u.lname,u.email from course c, section s, user u, enrolled e " \
                "where c.c_id=s.c_id and e.sec_id=s.sec_id and e.c_id=c.c_id and e.s_id = u.u_id and e.s_id<>%s and " \
                "e.c_id in(select e1.c_id from enrolled e1 where e1.s_id=%s)"
        mycursor.execute(query, (self.id,self.id))
        result = mycursor.fetchall()
        row = 0
        column = 0
        if len(result) == 0:
            pass
        elif len(result) != 0:
            self.mygrade_2.setRowCount(len(result))
            for x in result:
                self.mygrade_2.setItem(row, column, QtWidgets.QTableWidgetItem(str(x[0])))
                self.mygrade_2.setItem(row, column+1, QtWidgets.QTableWidgetItem(str(x[1])))
                self.mygrade_2.setItem(row, column+2, QtWidgets.QTableWidgetItem(str(x[2])))
                self.mygrade_2.setItem(row, column+3, QtWidgets.QTableWidgetItem(str(x[3])))
                self.mygrade_2.setItem(row, column+4, QtWidgets.QTableWidgetItem(str(x[4])))
                row+=1
    def setupUi(self, people_samecourse):
        people_samecourse.setObjectName("people_samecourse")
        people_samecourse.resize(818, 860)
        people_samecourse.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.label1 = QtWidgets.QLabel(people_samecourse)
        self.label1.setGeometry(QtCore.QRect(10, 20, 111, 31))
        self.label1.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"font: 16pt \"Lemon\";\n"
"color: rgb(134, 15, 0);")
        self.label1.setObjectName("label1")
        self.label = QtWidgets.QLabel(people_samecourse)
        self.label.setGeometry(QtCore.QRect(-130, 150, 1021, 931))
        self.label.setText("")
        self.label.setPixmap(QtGui.QPixmap("Images/grade_student.jpg"))
        self.label.setObjectName("label")
        self.mygrade_2 = QtWidgets.QTableWidget(people_samecourse)
        self.mygrade_2.setGeometry(QtCore.QRect(170, 40, 641, 641))
        self.mygrade_2.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"font: 10pt \"Lemon\";\n"
"color: rgb(134, 15, 0);")
        self.mygrade_2.setObjectName("mygrade_2")
        self.mygrade_2.setColumnCount(5)
        self.mygrade_2.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.mygrade_2.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.mygrade_2.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.mygrade_2.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.mygrade_2.setHorizontalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.mygrade_2.setHorizontalHeaderItem(4, item)

        self.display_people_take_samecourse()
        self.retranslateUi(people_samecourse)
        QtCore.QMetaObject.connectSlotsByName(people_samecourse)

    def retranslateUi(self, people_samecourse):
        _translate = QtCore.QCoreApplication.translate
        people_samecourse.setWindowTitle(_translate("people_samecourse", "People Page"))
        self.label1.setText(_translate("people_samecourse", "People"))
        item = self.mygrade_2.horizontalHeaderItem(0)
        item.setText(_translate("people_samecourse", "Course"))
        item = self.mygrade_2.horizontalHeaderItem(1)
        item.setText(_translate("people_samecourse", "Section"))
        item = self.mygrade_2.horizontalHeaderItem(2)
        item.setText(_translate("people_samecourse", "First Name"))
        item = self.mygrade_2.horizontalHeaderItem(3)
        item.setText(_translate("people_samecourse", "Last Name"))
        item = self.mygrade_2.horizontalHeaderItem(4)
        item.setText(_translate("people_samecourse", "Email"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    people_samecourse = QtWidgets.QWidget()
    ui = Ui_people_samecourse()
    ui.setupUi(people_samecourse)
    people_samecourse.show()
    sys.exit(app.exec_())
