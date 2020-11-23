from PyQt5 import QtCore, QtGui, QtWidgets
from access_to_db import *

logger=record()
mydb= db()

class Ui_mygrade(object):
    def __init__(self,id):
        logger.info('display user grade')
        self.id=id
    def display_grade(self):
        mycursor = mydb.cursor()
        query="select c.c_name, gi.sec_id, gi.gi_name, gi.grade, gi.score from graded_item gi,course c where c.c_id=gi.c_id and gi.s_id =%s"
        mycursor.execute(query,(self.id,))
        result = mycursor.fetchall()
        row=0
        column=0
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
    def setupUi(self, mygrade):
        mygrade.setObjectName("mygrade")
        mygrade.resize(975, 932)
        mygrade.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.label1 = QtWidgets.QLabel(mygrade)
        self.label1.setGeometry(QtCore.QRect(80, 30, 151, 31))
        self.label1.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"font: 16pt \"Lemon\";\n"
"color: rgb(134, 15, 0);")
        self.label1.setObjectName("label1")
        self.label = QtWidgets.QLabel(mygrade)
        self.label.setGeometry(QtCore.QRect(20, 260, 1021, 931))
        self.label.setText("")
        self.label.setPixmap(QtGui.QPixmap("Images/grade_student.jpg"))
        self.label.setObjectName("label")
        self.mygrade_2 = QtWidgets.QTableWidget(mygrade)
        self.mygrade_2.setGeometry(QtCore.QRect(340, 30, 631, 751))
        self.mygrade_2.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"font: 8pt \"Lemon\";\n"
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
        self.label.raise_()
        self.label1.raise_()
        self.mygrade_2.raise_()

        self.display_grade()
        self.retranslateUi(mygrade)
        QtCore.QMetaObject.connectSlotsByName(mygrade)

    def retranslateUi(self, mygrade):
        _translate = QtCore.QCoreApplication.translate
        mygrade.setWindowTitle(_translate("mygrade", "View My Grade"))
        self.label1.setText(_translate("mygrade", "My Grade"))
        item = self.mygrade_2.horizontalHeaderItem(0)
        item.setText(_translate("mygrade", "Course"))
        item = self.mygrade_2.horizontalHeaderItem(1)
        item.setText(_translate("mygrade", "Section"))
        item = self.mygrade_2.horizontalHeaderItem(2)
        item.setText(_translate("mygrade", "Assignment"))
        item = self.mygrade_2.horizontalHeaderItem(3)
        item.setText(_translate("mygrade", "Grade"))
        item = self.mygrade_2.horizontalHeaderItem(4)
        item.setText(_translate("mygrade", "Score"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    mygrade = QtWidgets.QWidget()
    ui = Ui_mygrade()
    ui.setupUi(mygrade)
    mygrade.show()
    sys.exit(app.exec_())
