from access_to_db import *
from PyQt5 import QtCore, QtGui, QtWidgets

logger=record()
mydb=db()
mycursor = mydb.cursor()

class Ui_smv(object):
    def __init__(self,lib_id):
        logger.info('displayed smv window')
        self.lib_id = lib_id
    def display_file(self):
        with open('../SQL/smv_window.sql') as f:
            commands = f.read().split(';')
        for command in commands:
            if command.find('select s.name, s.instrument,sf.smv_f, sf.date_created') !=-1:
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
                        self.tableWidget_2.setItem(row, column + 4, QtWidgets.QTableWidgetItem(str(x[4])))
                        row += 1
            else: pass
    def setupUi(self, smv):
        smv.setObjectName("smv")
        smv.resize(957, 652)
        smv.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.label = QtWidgets.QLabel(smv)
        self.label.setGeometry(QtCore.QRect(0, 20, 241, 191))
        self.label.setText("")
        self.label.setPixmap(QtGui.QPixmap("Images/12.jpg"))
        self.label.setScaledContents(True)
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(smv)
        self.label_2.setGeometry(QtCore.QRect(710, 450, 241, 191))
        self.label_2.setText("")
        self.label_2.setPixmap(QtGui.QPixmap("Images/12.jpg"))
        self.label_2.setScaledContents(True)
        self.label_2.setObjectName("label_2")
        self.title_2 = QtWidgets.QLabel(smv)
        self.title_2.setGeometry(QtCore.QRect(250, 120, 281, 21))
        self.title_2.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"font: 10pt \"Lemon\";\n"
"color: rgb(134, 15, 0);")
        self.title_2.setObjectName("title_2")
        self.tableWidget_2 = QtWidgets.QTableWidget(smv)
        self.tableWidget_2.setGeometry(QtCore.QRect(240, 150, 661, 291))
        self.tableWidget_2.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"font: 8pt \"Lemon\";\n"
"color: rgb(134, 15, 0);")
        self.tableWidget_2.setObjectName("tableWidget_2")
        self.tableWidget_2.setColumnCount(5)
        self.tableWidget_2.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_2.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_2.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_2.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_2.setHorizontalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_2.setHorizontalHeaderItem(4, item)
        self.display_file()
        self.retranslateUi(smv)
        QtCore.QMetaObject.connectSlotsByName(smv)

    def retranslateUi(self, smv):
        _translate = QtCore.QCoreApplication.translate
        smv.setWindowTitle(_translate("smv", "Sheet Music Visualizer"))
        self.title_2.setText(_translate("smv", "Sheet Music Visualizer Files"))
        item = self.tableWidget_2.horizontalHeaderItem(0)
        item.setText(_translate("smv", "Name"))
        item = self.tableWidget_2.horizontalHeaderItem(1)
        item.setText(_translate("smv", "Instrument"))
        item = self.tableWidget_2.horizontalHeaderItem(2)
        item.setText(_translate("smv", "File Name"))
        item = self.tableWidget_2.horizontalHeaderItem(3)
        item.setText(_translate("smv", "Date Created"))
        item = self.tableWidget_2.horizontalHeaderItem(4)
        item.setText(_translate("smv", "Last Modified"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    smv = QtWidgets.QWidget()
    ui = Ui_smv()
    ui.setupUi(smv)
    smv.show()
    sys.exit(app.exec_())
