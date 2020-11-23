from PyQt5 import QtCore, QtGui, QtWidgets
from access_to_db import *

logger=record()
mydb= db()


class Ui_ppgrade(object):
    def __init__(self,array):
        logger.info('displayed all students grades')
        self.array_cid=array
    def display_grade(self):
        mycursor = mydb.cursor()
        row = 0
        column = 0
        for x in self.array_cid:
            query="Select u.fname,u.lname,c.c_name,gi.sec_id,gi.gi_name,gi.grade,gi.score from user u, graded_item gi, course c " \
                  "where u.u_id=gi.s_id and gi.c_id= c.c_id and gi.c_id =%s order by u.fname"
            mycursor.execute(query, (x,))
            result = mycursor.fetchall()
            if len(result) == 0:
                pass
            elif len(result) != 0:
                self.grade_table.setRowCount(len(result))
                for y in result:
                    self.grade_table.setItem(row, column, QtWidgets.QTableWidgetItem(str(y[0])))
                    self.grade_table.setItem(row, column+1, QtWidgets.QTableWidgetItem(str(y[1])))
                    self.grade_table.setItem(row, column+2, QtWidgets.QTableWidgetItem(str(y[2])))
                    self.grade_table.setItem(row, column+3, QtWidgets.QTableWidgetItem(str(y[3])))
                    self.grade_table.setItem(row, column+4, QtWidgets.QTableWidgetItem(str(y[4])))
                    self.grade_table.setItem(row, column+5, QtWidgets.QTableWidgetItem(str(y[5])))
                    self.grade_table.setItem(row, column+6, QtWidgets.QTableWidgetItem(str(y[6])))
                    row += 1

    def setupUi(self, ppgrade):
        ppgrade.setObjectName("ppgrade")
        ppgrade.resize(1401, 825)
        ppgrade.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.grade_table = QtWidgets.QTableWidget(ppgrade)
        self.grade_table.setGeometry(QtCore.QRect(500, 110, 891, 711))
        self.grade_table.setObjectName("grade_table")
        self.grade_table.setColumnCount(7)
        self.grade_table.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.grade_table.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.grade_table.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.grade_table.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.grade_table.setHorizontalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.grade_table.setHorizontalHeaderItem(4, item)
        item = QtWidgets.QTableWidgetItem()
        self.grade_table.setHorizontalHeaderItem(5, item)
        item = QtWidgets.QTableWidgetItem()
        self.grade_table.setHorizontalHeaderItem(6, item)
        self.label = QtWidgets.QLabel(ppgrade)
        self.label.setGeometry(QtCore.QRect(10, 30, 541, 791))
        self.label.setText("")
        self.label.setPixmap(QtGui.QPixmap("Images/people.jpg"))
        self.label.setScaledContents(True)
        self.label.setObjectName("label")
        self.label1 = QtWidgets.QLabel(ppgrade)
        self.label1.setGeometry(QtCore.QRect(500, 70, 91, 31))
        self.label1.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"font: 16pt \"Lemon\";\n"
"color: rgb(134, 15, 0);")
        self.label1.setObjectName("label1")
        self.label.raise_()
        self.grade_table.raise_()
        self.label1.raise_()

        self.display_grade()

        self.retranslateUi(ppgrade)
        QtCore.QMetaObject.connectSlotsByName(ppgrade)

    def retranslateUi(self, ppgrade):
        _translate = QtCore.QCoreApplication.translate
        ppgrade.setWindowTitle(_translate("ppgrade", "Grade"))
        item = self.grade_table.horizontalHeaderItem(0)
        item.setText(_translate("ppgrade", "First Name"))
        item = self.grade_table.horizontalHeaderItem(1)
        item.setText(_translate("ppgrade", "Last Name"))
        item = self.grade_table.horizontalHeaderItem(2)
        item.setText(_translate("ppgrade", "Course"))
        item = self.grade_table.horizontalHeaderItem(3)
        item.setText(_translate("ppgrade", "Section"))
        item = self.grade_table.horizontalHeaderItem(4)
        item.setText(_translate("ppgrade", "Assignment"))
        item = self.grade_table.horizontalHeaderItem(5)
        item.setText(_translate("ppgrade", "Grade"))
        item = self.grade_table.horizontalHeaderItem(6)
        item.setText(_translate("ppgrade", "Score"))
        self.label1.setText(_translate("ppgrade", "Grade"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    ppgrade = QtWidgets.QWidget()
    ui = Ui_ppgrade()
    ui.setupUi(ppgrade)
    ppgrade.show()
    sys.exit(app.exec_())
