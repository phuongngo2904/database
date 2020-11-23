from PyQt5.QtWidgets import QMessageBox
from PyQt5 import QtCore, QtGui, QtWidgets
from access_to_db import *

logger=record()
mydb= db()


class Ui_create(object):
    def __init__(self,id):
        logger.info('displayed create course window')
        self.id=id
    def submit_button_clicked(self):
        mycursor = mydb.cursor()
        query_for_c_id = "Select max(c_id) from course"
        mycursor.execute(query_for_c_id)
        result1 = mycursor.fetchall()
        x = list(result1[0])
        self.c_id = x[0] + 1
        if self.active.isChecked():
            self.stt=1
        elif self.non_active.isChecked():
            self.stt=0
        query="INSERT INTO course values (%s,%s,%s,%s)"
        query1="INSERT INTO section values (%s,%s)"
        mycursor.execute(query,(self.c_id,self.name_lineedit.text(), self.id,self.stt))
        mycursor.execute(query1, (self.section_lineedit.text(),self.c_id))
        mydb.commit()
        logger.info('successfully inserted a value into table course')
        logger.info('successfully inserted a value into table section')
        message = QMessageBox()
        message.setWindowTitle("Success")
        message.setText("Successfully created a course.")
        message.exec()
    def setupUi(self, create):
        create.setObjectName("create")
        create.resize(892, 470)
        create.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.name = QtWidgets.QLabel(create)
        self.name.setGeometry(QtCore.QRect(20, 180, 141, 31))
        self.name.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"font: 10pt \"Lemon\";\n"
"color: rgb(134, 15, 0);")
        self.name.setObjectName("name")
        self.status = QtWidgets.QLabel(create)
        self.status.setGeometry(QtCore.QRect(20, 270, 141, 31))
        self.status.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"font: 10pt \"Lemon\";\n"
"color: rgb(134, 15, 0);")
        self.status.setObjectName("status")
        self.section = QtWidgets.QLabel(create)
        self.section.setGeometry(QtCore.QRect(70, 220, 81, 31))
        self.section.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"font: 10pt \"Lemon\";\n"
"color: rgb(134, 15, 0);")
        self.section.setObjectName("section")
        self.name_lineedit = QtWidgets.QLineEdit(create)
        self.name_lineedit.setGeometry(QtCore.QRect(170, 180, 361, 31))
        self.name_lineedit.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"font: 10pt \"Lemon\";\n"
"color: rgb(134, 15, 0);")
        self.name_lineedit.setObjectName("name_lineedit")
        self.section_lineedit = QtWidgets.QLineEdit(create)
        self.section_lineedit.setGeometry(QtCore.QRect(170, 220, 361, 31))
        self.section_lineedit.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"font: 10pt \"Lemon\";\n"
"color: rgb(134, 15, 0);")
        self.section_lineedit.setObjectName("section_lineedit")
        self.active = QtWidgets.QRadioButton(create)
        self.active.setGeometry(QtCore.QRect(190, 280, 91, 20))
        self.active.setStyleSheet("font: 10pt \"Lemon\";\n"
"color: rgb(134, 15, 0);")
        self.active.setObjectName("active")
        self.non_active = QtWidgets.QRadioButton(create)
        self.non_active.setGeometry(QtCore.QRect(320, 280, 141, 20))
        self.non_active.setStyleSheet("font: 10pt \"Lemon\";\n"
"color: rgb(134, 15, 0);")
        self.non_active.setObjectName("non_active")
        self.submit_button = QtWidgets.QPushButton(create)
        self.submit_button.setGeometry(QtCore.QRect(140, 360, 101, 31))
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
        self.exit_button = QtWidgets.QPushButton(create)
        self.exit_button.setGeometry(QtCore.QRect(360, 360, 101, 31))
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
        self.label = QtWidgets.QLabel(create)
        self.label.setGeometry(QtCore.QRect(490, 40, 381, 401))
        self.label.setText("")
        self.label.setPixmap(QtGui.QPixmap("Images/create_course.jpg"))
        self.label.setScaledContents(True)
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(create)
        self.label_2.setGeometry(QtCore.QRect(180, -40, 331, 291))
        self.label_2.setText("")
        self.label_2.setPixmap(QtGui.QPixmap("Images/music_icon.jpg"))
        self.label_2.setScaledContents(True)
        self.label_2.setObjectName("label_2")
        self.label_2.raise_()
        self.label.raise_()
        self.name.raise_()
        self.status.raise_()
        self.section.raise_()
        self.name_lineedit.raise_()
        self.section_lineedit.raise_()
        self.active.raise_()
        self.non_active.raise_()
        self.submit_button.raise_()
        self.exit_button.raise_()

        self.exit_button.clicked.connect(create.close)
        self.submit_button.clicked.connect(self.submit_button_clicked)
        self.retranslateUi(create)
        QtCore.QMetaObject.connectSlotsByName(create)

    def retranslateUi(self, create):
        _translate = QtCore.QCoreApplication.translate
        create.setWindowTitle(_translate("create", "Create a Course"))
        self.name.setText(_translate("create", "Courses Name"))
        self.status.setText(_translate("create", "Course Status"))
        self.section.setText(_translate("create", "Section"))
        self.active.setText(_translate("create", "Active"))
        self.non_active.setText(_translate("create", "Non-Active"))
        self.submit_button.setText(_translate("create", "Submit"))
        self.exit_button.setText(_translate("create", "Exit"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    create = QtWidgets.QWidget()
    ui = Ui_create(2)
    ui.setupUi(create)
    create.show()
    sys.exit(app.exec_())
