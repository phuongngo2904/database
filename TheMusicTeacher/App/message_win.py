from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QMessageBox
from access_to_db import *
import datetime

logger=record()
mydb= db()
mycursor=mydb.cursor()

class Ui_msg(object):
    def __init__(self,id):
        logger.info('displayed Message window')
        self.id=id
    def check_button_clicked(self):
        with open('../SQL/message_window.sql') as f:
            commands = f.read().split(';')
        for command in commands:
            if command.find('Select u_id from user where email') != -1:
               command = command.replace('@user_email', '%s')
               mycursor.execute(command, (self.receiver_lineedit.text(),))
               result = mycursor.fetchall()
               for x in result:
                   self.receiver_id = x[0]
               if len(result) == 0:
                   message = QMessageBox()
                   message.setWindowTitle("FAIL !")
                   message.setText("User not found.")
                   message.exec()
                   logger.info('User not found')
               else:
                   message = QMessageBox()
                   message.setWindowTitle("Success!")
                   message.setText("Valid User.")
                   message.exec()
                   logger.info('User found')
            else: pass
    def send_button_clicked(self):
        with open('../SQL/message_window.sql') as f:
            commands = f.read().split(';')
        for command in commands:
            if command.find('Select max(msg_id) from') !=-1:
                mycursor.execute(command)
                result = mycursor.fetchall()
                if len(result)==1:
                     x = list(result[0])
                     if x[0]==None:
                           self.msg_id=1
                     else: self.msg_id = x[0] + 1

            elif command.find('INSERT INTO message values') != -1:
                command= command.replace('@msgid', '%s')
                command= command.replace('@sub', '%s')
                mycursor.execute(command, (self.msg_id, self.subject_lineedit.text()))
                mydb.commit()
                logger.info('Successfully inserted values into table message')

            elif command.find('Select max(submsg_id) from') != -1:
                mycursor.execute(command)
                result1 = mycursor.fetchall()
                if len(result1) == 1:
                    x = list(result1[0])
                if x[0] == None:
                    self.submsg_id = 1
                else:
                    self.submsg_id = x[0] + 1

            elif command.find('INSERT INTO message_chain values') != -1:
                command=command.replace('@subid', '%s')
                command=command.replace('@mid', '%s')
                command=command.replace('@senderid', '%s')
                command=command.replace('@receiverid', '%s')
                command=command.replace('@content', '%s')
                command=command.replace('@time_sent', '%s')
                command=command.replace('@time_read', '%s')
                now = datetime.datetime.now()
                self.time_sent = now.strftime('%Y-%m-%d %H:%M:%S')
                mycursor.execute(command, (
                    self.submsg_id, self.msg_id, self.id, self.receiver_id,
                    self.content_textedit.toPlainText(),
                    self.time_sent, None))
                mydb.commit()
                logger.info('Successfully inserted values into table message_chain')
                message = QMessageBox()
                message.setWindowTitle("Success")
                message.setText("Message sent")
                message.exec()
                logger.info('message sent')
    def setupUi(self, msg):
        msg.setObjectName("msg")
        msg.resize(752, 465)
        msg.setStyleSheet("background-color: qlineargradient(spread:pad, x1:0.0199005, y1:0.028, x2:1, y2:0.79, stop:0 rgba(21, 255, 243, 255), stop:1 rgba(234, 8, 8, 255));")
        self.subjec_label = QtWidgets.QLabel(msg)
        self.subjec_label.setGeometry(QtCore.QRect(60, 150, 81, 31))
        self.subjec_label.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"font: 10pt \"Lemon\";\n"
"color: rgb(134, 15, 0);")
        self.subjec_label.setObjectName("subjec_label")
        self.subject_lineedit = QtWidgets.QLineEdit(msg)
        self.subject_lineedit.setGeometry(QtCore.QRect(160, 150, 401, 31))
        self.subject_lineedit.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"font: 10pt \"Lemon\";\n"
"color: rgb(134, 15, 0);")
        self.subject_lineedit.setObjectName("subject_lineedit")
        self.to_label = QtWidgets.QLabel(msg)
        self.to_label.setGeometry(QtCore.QRect(100, 100, 41, 31))
        self.to_label.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"font: 10pt \"Lemon\";\n"
"color: rgb(134, 15, 0);")
        self.to_label.setObjectName("to_label")
        self.receiver_lineedit = QtWidgets.QLineEdit(msg)
        self.receiver_lineedit.setGeometry(QtCore.QRect(160, 100, 401, 31))
        self.receiver_lineedit.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"font: 10pt \"Lemon\";\n"
"color: rgb(134, 15, 0);")
        self.receiver_lineedit.setObjectName("receiver_lineedit")
        self.send_button = QtWidgets.QPushButton(msg)
        self.send_button.setGeometry(QtCore.QRect(200, 410, 101, 31))
        font = QtGui.QFont()
        font.setFamily("Russo One")
        font.setPointSize(14)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.send_button.setFont(font)
        self.send_button.setStyleSheet("font: 14pt \"Russo One\";\n"
"color: rgb(255, 247, 128);\n"
"background-color: rgb(153, 0, 28);")
        self.send_button.setObjectName("send_button")
        self.cancel_button = QtWidgets.QPushButton(msg)
        self.cancel_button.setGeometry(QtCore.QRect(430, 410, 101, 31))
        font = QtGui.QFont()
        font.setFamily("Russo One")
        font.setPointSize(14)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.cancel_button.setFont(font)
        self.cancel_button.setStyleSheet("font: 14pt \"Russo One\";\n"
"color: rgb(255, 247, 128);\n"
"background-color: rgb(153, 0, 28);")
        self.cancel_button.setObjectName("cancel_button")
        self.check_button = QtWidgets.QPushButton(msg)
        self.check_button.setGeometry(QtCore.QRect(580, 100, 101, 31))
        font = QtGui.QFont()
        font.setFamily("Russo One")
        font.setPointSize(14)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.check_button.setFont(font)
        self.check_button.setStyleSheet("font: 14pt \"Russo One\";\n"
"color: rgb(255, 247, 128);\n"
"background-color: rgb(153, 0, 28);")
        self.check_button.setObjectName("check_button")
        self.content_textedit = QtWidgets.QTextEdit(msg)
        self.content_textedit.setGeometry(QtCore.QRect(160, 200, 401, 171))
        self.content_textedit.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"font: 10pt \"Lemon\";\n"
"color: rgb(134, 15, 0);")
        self.content_textedit.setObjectName("content_textedit")
        self.content_label = QtWidgets.QLabel(msg)
        self.content_label.setGeometry(QtCore.QRect(60, 200, 91, 31))
        self.content_label.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"font: 10pt \"Lemon\";\n"
"color: rgb(134, 15, 0);")
        self.content_label.setObjectName("content_label")
        self.cancel_button.clicked.connect(msg.close)
        self.send_button.clicked.connect(self.send_button_clicked)
        self.check_button.clicked.connect(self.check_button_clicked)
        self.retranslateUi(msg)
        QtCore.QMetaObject.connectSlotsByName(msg)

    def retranslateUi(self, msg):
        _translate = QtCore.QCoreApplication.translate
        msg.setWindowTitle(_translate("msg", "Message"))
        self.subjec_label.setText(_translate("msg", "Subject:"))
        self.to_label.setText(_translate("msg", "To:"))
        self.send_button.setText(_translate("msg", "Send"))
        self.cancel_button.setText(_translate("msg", "Cancel"))
        self.check_button.setText(_translate("msg", "Check"))
        self.content_label.setText(_translate("msg", "Content:"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    msg = QtWidgets.QWidget()
    ui = Ui_msg()
    ui.setupUi(msg)
    msg.show()
    sys.exit(app.exec_())
s