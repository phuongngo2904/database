from PyQt5 import QtCore, QtGui, QtWidgets
from access_to_db import *

logger=record()
mydb= db()

class Ui_Assignment_Page(object):
    def __init__(self,array):
        logger.info('displayed assignments which has been created')
        self.array=array
    def display_assignment(self):
        mycursor = mydb.cursor()
        row = 0
        column = 0
        for x in self.array:
            query = "select c_name,sec_id,category,gi_name,date_start,date_due,published from course c,gradebook g where c.c_id=g.c_id and g.c_id =%s"
            mycursor.execute(query, (x,))
            result = mycursor.fetchall()
            if len(result)==0:
                pass
            elif len(result)!=0:
                self.assignment_table.setRowCount(len(result))
                for x in result:
                    self.assignment_table.setItem(row, column, QtWidgets.QTableWidgetItem(str(x[0])))
                    self.assignment_table.setItem(row, column+1, QtWidgets.QTableWidgetItem(str(x[1])))
                    self.assignment_table.setItem(row, column+2, QtWidgets.QTableWidgetItem(str(x[2])))
                    self.assignment_table.setItem(row, column+3, QtWidgets.QTableWidgetItem(str(x[3])))
                    self.assignment_table.setItem(row, column+4, QtWidgets.QTableWidgetItem(str(x[4])))
                    self.assignment_table.setItem(row, column+5, QtWidgets.QTableWidgetItem(str(x[5])))
                    if x[6]==1:
                        self.assignment_table.setItem(row, column +6, QtWidgets.QTableWidgetItem("Yes"))
                    else:
                        self.assignment_table.setItem(row, column + 6, QtWidgets.QTableWidgetItem("No"))
                    row += 1
    def setupUi(self, Assignment_Page):
        Assignment_Page.setObjectName("Assignment_Page")
        Assignment_Page.resize(921, 790)
        Assignment_Page.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.label = QtWidgets.QLabel(Assignment_Page)
        self.label.setGeometry(QtCore.QRect(320, 40, 271, 241))
        self.label.setText("")
        self.label.setPixmap(QtGui.QPixmap("Images/images.png"))
        self.label.setObjectName("label")
        self.assignment_table = QtWidgets.QTableWidget(Assignment_Page)
        self.assignment_table.setGeometry(QtCore.QRect(30, 290, 881, 491))
        self.assignment_table.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.assignment_table.setObjectName("assignment_table")
        self.assignment_table.setColumnCount(7)
        self.assignment_table.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.assignment_table.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.assignment_table.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.assignment_table.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.assignment_table.setHorizontalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.assignment_table.setHorizontalHeaderItem(4, item)
        item = QtWidgets.QTableWidgetItem()
        self.assignment_table.setHorizontalHeaderItem(5, item)
        item = QtWidgets.QTableWidgetItem()
        self.assignment_table.setHorizontalHeaderItem(6, item)
        self.firstname = QtWidgets.QLabel(Assignment_Page)
        self.firstname.setGeometry(QtCore.QRect(40, 240, 201, 31))
        self.firstname.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"font: 10pt \"Lemon\";\n"
"color: rgb(134, 15, 0);")
        self.firstname.setObjectName("firstname")
        self.display_assignment()
        self.retranslateUi(Assignment_Page)
        QtCore.QMetaObject.connectSlotsByName(Assignment_Page)

    def retranslateUi(self, Assignment_Page):
        _translate = QtCore.QCoreApplication.translate
        Assignment_Page.setWindowTitle(_translate("Assignment_Page", "Assignment Page"))
        item = self.assignment_table.horizontalHeaderItem(0)
        item.setText(_translate("Assignment_Page", "Course"))
        item = self.assignment_table.horizontalHeaderItem(1)
        item.setText(_translate("Assignment_Page", "Section"))
        item = self.assignment_table.horizontalHeaderItem(2)
        item.setText(_translate("Assignment_Page", "Category"))
        item = self.assignment_table.horizontalHeaderItem(3)
        item.setText(_translate("Assignment_Page", "Name"))
        item = self.assignment_table.horizontalHeaderItem(4)
        item.setText(_translate("Assignment_Page", "Date_Start"))
        item = self.assignment_table.horizontalHeaderItem(5)
        item.setText(_translate("Assignment_Page", "Date_Due"))
        item = self.assignment_table.horizontalHeaderItem(6)
        item.setText(_translate("Assignment_Page", "Publish"))
        self.firstname.setText(_translate("Assignment_Page", "Assignment Created"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Assignment_Page = QtWidgets.QWidget()
    ui = Ui_Assignment_Page()
    ui.setupUi(Assignment_Page)
    Assignment_Page.show()
    sys.exit(app.exec_())
