from access_to_db import *
from PyQt5 import QtCore, QtGui, QtWidgets

logger=record()
mydb=db()
mycursor = mydb.cursor()

class Ui_material(object):
    def __init__(self,lib_id):
        logger.info('displayed material window')
        self.lib_id=lib_id
    def display_material(self):
        with open('../SQL/material_window.sql') as f:
            commands = f.read().split(';')
        for command in commands:
            if command.find('select m_name, date_created, last_modified,type') !=-1:
                command = command.replace('@libid', '%s')
                mycursor.execute(command, (self.lib_id,))
                result = mycursor.fetchall()
                row = 0
                column = 0
                if len(result) == 0:
                    pass
                elif len(result) != 0:
                    self.tableWidget_2.setRowCount(len(result))
                    for x in result:
                        self.tableWidget_2.setItem(row, column, QtWidgets.QTableWidgetItem(str(x[0])))
                        self.tableWidget_2.setItem(row, column + 1, QtWidgets.QTableWidgetItem(str(x[1])))
                        self.tableWidget_2.setItem(row, column + 2, QtWidgets.QTableWidgetItem(str(x[2])))
                        self.tableWidget_2.setItem(row, column + 3, QtWidgets.QTableWidgetItem(str(x[3])))
                        row += 1
    def setupUi(self, material):
        material.setObjectName("material")
        material.resize(910, 774)
        material.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.label = QtWidgets.QLabel(material)
        self.label.setGeometry(QtCore.QRect(0, 20, 241, 191))
        self.label.setText("")
        self.label.setPixmap(QtGui.QPixmap("Images/12.jpg"))
        self.label.setScaledContents(True)
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(material)
        self.label_2.setGeometry(QtCore.QRect(670, 570, 241, 191))
        self.label_2.setText("")
        self.label_2.setPixmap(QtGui.QPixmap("Images/12.jpg"))
        self.label_2.setScaledContents(True)
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(material)
        self.label_3.setGeometry(QtCore.QRect(250, 120, 91, 21))
        self.label_3.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"font: 10pt \"Lemon\";\n"
"color: rgb(134, 15, 0);")
        self.label_3.setObjectName("label_3")
        self.tableWidget_2 = QtWidgets.QTableWidget(material)
        self.tableWidget_2.setGeometry(QtCore.QRect(240, 150, 511, 471))
        self.tableWidget_2.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"font: 8pt \"Lemon\";\n"
"color: rgb(134, 15, 0);")
        self.tableWidget_2.setObjectName("tableWidget_2")
        self.tableWidget_2.setColumnCount(4)
        self.tableWidget_2.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_2.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_2.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_2.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_2.setHorizontalHeaderItem(3, item)

        self.display_material()
        self.retranslateUi(material)
        QtCore.QMetaObject.connectSlotsByName(material)

    def retranslateUi(self, material):
        _translate = QtCore.QCoreApplication.translate
        material.setWindowTitle(_translate("material", "Material"))
        self.label_3.setText(_translate("material", "Material"))
        item = self.tableWidget_2.horizontalHeaderItem(0)
        item.setText(_translate("material", "Name"))
        item = self.tableWidget_2.horizontalHeaderItem(1)
        item.setText(_translate("material", "Date Created"))
        item = self.tableWidget_2.horizontalHeaderItem(2)
        item.setText(_translate("material", "Last Modified"))
        item = self.tableWidget_2.horizontalHeaderItem(3)
        item.setText(_translate("material", "Type"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    material = QtWidgets.QWidget()
    ui = Ui_material()
    ui.setupUi(material)
    material.show()
    sys.exit(app.exec_())
