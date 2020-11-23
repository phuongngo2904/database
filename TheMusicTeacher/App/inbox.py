from access_to_db import *
from PyQt5 import QtCore, QtGui, QtWidgets

logger=record()
mydb=db()
mycursor = mydb.cursor()

class Ui_inbox(object):
    def __init__(self,id):
        self.id=id
        logger.info('displayed inbox window')
    def display_msg_sent(self):
        with open('../SQL/inbox_window.sql') as f:
            commands = f.read().split(';')
        for command in commands:
            if command.find('select u.fname, m.subject,mc.content, mc.time_sent from user') != -1:
                command = command.replace('@sender', '%s')
                mycursor.execute(command, (self.id,))
                result = mycursor.fetchall()
                row = 0
                column = 0
                if len(result) == 0:
                    pass
                elif len(result) != 0:
                    self.sent.setRowCount(len(result))
                    for x in result:
                        self.sent.setItem(row, column, QtWidgets.QTableWidgetItem(str(x[0])))
                        self.sent.setItem(row, column + 1, QtWidgets.QTableWidgetItem(str(x[1])))
                        self.sent.setItem(row, column + 2, QtWidgets.QTableWidgetItem(str(x[2])))
                        self.sent.setItem(row, column + 3, QtWidgets.QTableWidgetItem(str(x[3])))
                        row += 1
    def display_msg_read(self):
        with open('../SQL/inbox_window.sql') as f:
            commands = f.read().split(';')
        for command in commands:
            if command.find('select u.fname, m.subject,mc.content, mc.time_read') != -1:
                command = command.replace('@receiver', '%s')
                mycursor.execute(command, (self.id,))
                result = mycursor.fetchall()
                row = 0
                column = 0
                if len(result) == 0:
                    pass
                elif len(result) != 0:
                    self.read.setRowCount(len(result))
                    for x in result:
                        self.read.setItem(row, column, QtWidgets.QTableWidgetItem(str(x[0])))
                        self.read.setItem(row, column + 1, QtWidgets.QTableWidgetItem(str(x[1])))
                        self.read.setItem(row, column + 2, QtWidgets.QTableWidgetItem(str(x[2])))
                        self.read.setItem(row, column + 3, QtWidgets.QTableWidgetItem(str(x[3])))
                        row += 1

    def setupUi(self, inbox):
        inbox.setObjectName("inbox")
        inbox.resize(1328, 854)
        inbox.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.label1 = QtWidgets.QLabel(inbox)
        self.label1.setGeometry(QtCore.QRect(10, 10, 231, 31))
        self.label1.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"font: 16pt \"Lemon\";\n"
"color: rgb(134, 15, 0);")
        self.label1.setObjectName("label1")
        self.label = QtWidgets.QLabel(inbox)
        self.label.setGeometry(QtCore.QRect(-10, 370, 1351, 761))
        self.label.setText("")
        self.label.setPixmap(QtGui.QPixmap("Images/3.jpg"))
        self.label.setScaledContents(True)
        self.label.setObjectName("label")
        self.sent = QtWidgets.QTableWidget(inbox)
        self.sent.setGeometry(QtCore.QRect(20, 60, 521, 541))
        self.sent.setObjectName("sent")
        self.sent.setColumnCount(4)
        self.sent.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.sent.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.sent.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.sent.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.sent.setHorizontalHeaderItem(3, item)
        self.read = QtWidgets.QTableWidget(inbox)
        self.read.setGeometry(QtCore.QRect(750, 60, 511, 541))
        self.read.setObjectName("read")
        self.read.setColumnCount(4)
        self.read.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.read.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.read.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.read.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.read.setHorizontalHeaderItem(3, item)
        self.label1_2 = QtWidgets.QLabel(inbox)
        self.label1_2.setGeometry(QtCore.QRect(760, 10, 231, 31))
        self.label1_2.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"font: 16pt \"Lemon\";\n"
"color: rgb(134, 15, 0);")
        self.label1_2.setObjectName("label1_2")

        self.display_msg_read()
        self.display_msg_sent()
        self.retranslateUi(inbox)
        QtCore.QMetaObject.connectSlotsByName(inbox)

    def retranslateUi(self, inbox):
        _translate = QtCore.QCoreApplication.translate
        inbox.setWindowTitle(_translate("inbox", "INBOX"))
        self.label1.setText(_translate("inbox", "Message Sent"))
        item = self.sent.horizontalHeaderItem(0)
        item.setText(_translate("inbox", "To"))
        item = self.sent.horizontalHeaderItem(1)
        item.setText(_translate("inbox", "Subject"))
        item = self.sent.horizontalHeaderItem(2)
        item.setText(_translate("inbox", "Content"))
        item = self.sent.horizontalHeaderItem(3)
        item.setText(_translate("inbox", "Time Sent"))
        item = self.read.horizontalHeaderItem(0)
        item.setText(_translate("inbox", "From"))
        item = self.read.horizontalHeaderItem(1)
        item.setText(_translate("inbox", "Subject"))
        item = self.read.horizontalHeaderItem(2)
        item.setText(_translate("inbox", "Content"))
        item = self.read.horizontalHeaderItem(3)
        item.setText(_translate("inbox", "Time Read"))
        self.label1_2.setText(_translate("inbox", "Message Read"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    inbox = QtWidgets.QWidget()
    ui = Ui_inbox()
    ui.setupUi(inbox)
    inbox.show()
    sys.exit(app.exec_())
