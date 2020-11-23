from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QMessageBox
from access_to_db import *

logger=record()
mydb= db()

class Ui_create_assign(object):
    def __init__(self,a):
        self.array_cid=a
    def submit_button_clicked(self):
        for x in range(len(self.course)):
            if self.course.currentIndex()==x:
                mycursor = mydb.cursor()
                query = "INSERT INTO gradebook values (%s,%s,%s,%s,%s,%s,%s)"
                if self.yes.isChecked():
                    self.publish=1
                elif self.no.isChecked():
                    self.publish=0
                mycursor.execute(query,(self.name_lineedit.text(),self.section_id[x],self.c_id[x],self.category_lineedit.text(),
                                        self.start_lineedit.text(),self.due_lineedit.text(),self.publish))
                mydb.commit()
                logger.info('successfully inserted a value into table gradebook')
                message = QMessageBox()
                message.setWindowTitle("Success")
                message.setText("Successfully created an assignment.")
                message.exec()
            else: pass
    def show_course(self):
        self.c_id=[]
        self.section_id=[]
        mycursor = mydb.cursor()
        for x in self.array_cid:
            query = "select c.c_id,c.c_name,sec_id from course c, section s where c.c_id=s.c_id and c.c_id=%s"
            mycursor.execute(query, (x,))
            result = mycursor.fetchall()
            for y in result:
                self.c_id.append(y[0])
                self.section_id.append(y[2])
                self.course.addItem(f"{y[1]}__section({y[2]})")
    def setupUi(self, create_assign):
        create_assign.setObjectName("create_assign")
        create_assign.resize(705, 562)
        create_assign.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.label2 = QtWidgets.QLabel(create_assign)
        self.label2.setGeometry(QtCore.QRect(10, 190, 181, 31))
        self.label2.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"font: 10pt \"Lemon\";\n"
"color: rgb(134, 15, 0);")
        self.label2.setObjectName("label2")
        self.name_lineedit = QtWidgets.QLineEdit(create_assign)
        self.name_lineedit.setGeometry(QtCore.QRect(200, 190, 361, 31))
        self.name_lineedit.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"font: 10pt \"Lemon\";\n"
"color: rgb(134, 15, 0);")
        self.name_lineedit.setObjectName("name_lineedit")
        self.course = QtWidgets.QComboBox(create_assign)
        self.course.setGeometry(QtCore.QRect(200, 130, 451, 31))
        self.course.setObjectName("course")
        self.course.setStyleSheet("font: 10pt \"Lemon\";\ncolor: rgb(134, 15, 0);")
        self.label1 = QtWidgets.QLabel(create_assign)
        self.label1.setGeometry(QtCore.QRect(90, 140, 81, 31))
        self.label1.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"font: 10pt \"Lemon\";\n"
"color: rgb(134, 15, 0);")
        self.label1.setObjectName("label1")
        self.label4 = QtWidgets.QLabel(create_assign)
        self.label4.setGeometry(QtCore.QRect(80, 300, 101, 31))
        self.label4.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"font: 10pt \"Lemon\";\n"
"color: rgb(134, 15, 0);")
        self.label4.setObjectName("label4")
        self.label5 = QtWidgets.QLabel(create_assign)
        self.label5.setGeometry(QtCore.QRect(80, 350, 91, 31))
        self.label5.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"font: 10pt \"Lemon\";\n"
"color: rgb(134, 15, 0);")
        self.label5.setObjectName("label5")
        self.start_lineedit = QtWidgets.QLineEdit(create_assign)
        self.start_lineedit.setGeometry(QtCore.QRect(200, 300, 361, 31))
        self.start_lineedit.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"font: 10pt \"Lemon\";\n"
"color: rgb(134, 15, 0);")
        self.start_lineedit.setObjectName("start_lineedit")
        self.due_lineedit = QtWidgets.QLineEdit(create_assign)
        self.due_lineedit.setGeometry(QtCore.QRect(200, 350, 361, 31))
        self.due_lineedit.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"font: 10pt \"Lemon\";\n"
"color: rgb(134, 15, 0);")
        self.due_lineedit.setObjectName("due_lineedit")
        self.label6 = QtWidgets.QLabel(create_assign)
        self.label6.setGeometry(QtCore.QRect(90, 400, 81, 31))
        self.label6.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"font: 10pt \"Lemon\";\n"
"color: rgb(134, 15, 0);")
        self.label6.setObjectName("label6")
        self.yes = QtWidgets.QRadioButton(create_assign)
        self.yes.setGeometry(QtCore.QRect(210, 410, 61, 20))
        self.yes.setStyleSheet("font: 10pt \"Lemon\";\n"
"color: rgb(134, 15, 0);")
        self.yes.setObjectName("yes")
        self.no = QtWidgets.QRadioButton(create_assign)
        self.no.setGeometry(QtCore.QRect(310, 410, 61, 20))
        self.no.setStyleSheet("font: 10pt \"Lemon\";\n"
"color: rgb(134, 15, 0);")
        self.no.setObjectName("no")
        self.submit_button = QtWidgets.QPushButton(create_assign)
        self.submit_button.setGeometry(QtCore.QRect(180, 490, 101, 31))
        font = QtGui.QFont()
        font.setFamily("Russo One")
        font.setPointSize(14)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.submit_button.setFont(font)
        self.submit_button.setStyleSheet("font: 14pt \"Russo One\";\n"
"color: rgb(255, 247, 128);\n"
"background-color: rgb(153, 0, 28);")
        self.submit_button.setObjectName("submit_button")
        self.exit_button = QtWidgets.QPushButton(create_assign)
        self.exit_button.setGeometry(QtCore.QRect(400, 490, 101, 31))
        font = QtGui.QFont()
        font.setFamily("Russo One")
        font.setPointSize(14)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.exit_button.setFont(font)
        self.exit_button.setStyleSheet("font: 14pt \"Russo One\";\n"
"color: rgb(255, 247, 128);\n"
"background-color: rgb(153, 0, 28);")
        self.exit_button.setObjectName("exit_button")
        self.label_2 = QtWidgets.QLabel(create_assign)
        self.label_2.setGeometry(QtCore.QRect(200, -70, 361, 291))
        self.label_2.setText("")
        self.label_2.setPixmap(QtGui.QPixmap("Images/music_icon.jpg"))
        self.label_2.setScaledContents(True)
        self.label_2.setObjectName("label_2")
        self.category = QtWidgets.QLabel(create_assign)
        self.category.setGeometry(QtCore.QRect(90, 250, 101, 31))
        self.category.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"font: 10pt \"Lemon\";\n"
"color: rgb(134, 15, 0);")
        self.category.setObjectName("category")
        self.category_lineedit = QtWidgets.QLineEdit(create_assign)
        self.category_lineedit.setGeometry(QtCore.QRect(200, 250, 361, 31))
        self.category_lineedit.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"font: 10pt \"Lemon\";\n"
"color: rgb(134, 15, 0);")
        self.category_lineedit.setObjectName("category_lineedit")
        self.label_2.raise_()
        self.label2.raise_()
        self.name_lineedit.raise_()
        self.course.raise_()
        self.label1.raise_()
        self.label4.raise_()
        self.label5.raise_()
        self.start_lineedit.raise_()
        self.due_lineedit.raise_()
        self.label6.raise_()
        self.yes.raise_()
        self.no.raise_()
        self.submit_button.raise_()
        self.exit_button.raise_()
        self.category.raise_()
        self.category_lineedit.raise_()

        self.show_course()
        self.exit_button.clicked.connect(create_assign.close)
        self.submit_button.clicked.connect(self.submit_button_clicked)

        self.retranslateUi(create_assign)
        QtCore.QMetaObject.connectSlotsByName(create_assign)

    def retranslateUi(self, create_assign):
        _translate = QtCore.QCoreApplication.translate
        create_assign.setWindowTitle(_translate("create_assign", "Create an Assignment"))
        self.label2.setText(_translate("create_assign", "Assignment Name"))
        self.label1.setText(_translate("create_assign", "Courses"))
        self.label4.setText(_translate("create_assign", "Date Start"))
        self.label5.setText(_translate("create_assign", "Date Due"))
        self.label6.setText(_translate("create_assign", "Publish"))
        self.yes.setText(_translate("create_assign", "Yes"))
        self.no.setText(_translate("create_assign", "No"))
        self.submit_button.setText(_translate("create_assign", "Confirm"))
        self.exit_button.setText(_translate("create_assign", "Exit"))
        self.category.setText(_translate("create_assign", "Category"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    create_assign = QtWidgets.QWidget()
    ui = Ui_create_assign()
    ui.setupUi(create_assign)
    create_assign.show()
    sys.exit(app.exec_())
