from PyQt5 import QtCore, QtGui, QtWidgets
from access_to_db import *
from library import Ui_openlib

logger=record()
mydb = db()

class Ui_lib(object):
    def __init__(self,id):
        self.id=id
    def access_button_clicked(self):
        for x in range(len(self.array_lib_id)):
            if self.comboBox.currentIndex()==x:
                logger.info(f'open {self.lib_name[x]} library')
                self.openlib = QtWidgets.QWidget()
                self.ui = Ui_openlib(self.id,self.array_lib_id[x],self.lib_name[x])
                self.ui.setupUi(self.openlib)
                self.openlib.show()

            else: pass
    def display_lib(self):
        mycursor = mydb.cursor()
        self.array_lib_id=[]
        self.lib_name=[]
        with open('../SQL/access_to_a_lib_window.sql') as f:
            commands = f.read().split(';')
        for command in commands:
            if command.find('select l.lib_id, l.lib_name') != -1:
                command = command.replace('@user_id', '%s')
                mycursor.execute(command, (self.id,))
                result = mycursor.fetchall()
                for x in result:
                    self.array_lib_id.append(x[0])
                    self.lib_name.append(x[1])
                    self.comboBox.addItem(x[1])

    def setupUi(self, lib):
        lib.setObjectName("lib")
        lib.resize(675, 478)
        lib.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.label1 = QtWidgets.QLabel(lib)
        self.label1.setGeometry(QtCore.QRect(130, 30, 211, 31))
        self.label1.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"font: 10pt \"Lemon\";\n"
"color: rgb(134, 15, 0);")
        self.label1.setObjectName("label1")
        self.label = QtWidgets.QLabel(lib)
        self.label.setGeometry(QtCore.QRect(0, 0, 681, 481))
        self.label.setText("")
        self.label.setPixmap(QtGui.QPixmap("Images/4.jpg"))
        self.label.setScaledContents(True)
        self.label.setObjectName("label")
        self.comboBox = QtWidgets.QComboBox(lib)
        self.comboBox.setGeometry(QtCore.QRect(10, 90, 371, 31))
        self.comboBox.setStyleSheet("background-color: rgb(255, 255, 255);\n"
                                  "font: 10pt \"Lemon\";\n"
                                  "color: rgb(134, 15, 0);")
        self.comboBox.setObjectName("comboBox")
        self.access_button = QtWidgets.QPushButton(lib)
        self.access_button.setGeometry(QtCore.QRect(50, 190, 101, 31))
        font = QtGui.QFont()
        font.setFamily("Russo One")
        font.setPointSize(14)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.access_button.setFont(font)
        self.access_button.setStyleSheet("font: 14pt \"Russo One\";\n"
"color: rgb(255, 247, 128);\n"
"background-color: rgb(153, 0, 28);")
        self.access_button.setObjectName("access_button")
        self.exit_button = QtWidgets.QPushButton(lib)
        self.exit_button.setGeometry(QtCore.QRect(220, 190, 101, 31))
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
        self.label.raise_()
        self.label1.raise_()
        self.comboBox.raise_()
        self.access_button.raise_()
        self.exit_button.raise_()

        self.access_button.clicked.connect(self.access_button_clicked)
        self.display_lib()
        self.exit_button.clicked.connect(lib.close)
        self.retranslateUi(lib)
        QtCore.QMetaObject.connectSlotsByName(lib)

    def retranslateUi(self, lib):
        _translate = QtCore.QCoreApplication.translate
        lib.setWindowTitle(_translate("lib", "Access to a Library"))
        self.label1.setText(_translate("lib", "Please pick a library"))
        self.access_button.setText(_translate("lib", "Access"))
        self.exit_button.setText(_translate("lib", "Exit"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    lib = QtWidgets.QWidget()
    ui = Ui_lib()
    ui.setupUi(lib)
    lib.show()
    sys.exit(app.exec_())
