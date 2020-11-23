from PyQt5 import QtCore, QtGui, QtWidgets
from access_to_db import *
from game import Ui_Game
from smvfile import Ui_smv
from material import Ui_material

logger=record()
mydb = db()


class Ui_openlib(object):
    def __init__(self,user_id,id, title):
        logger.info('displayed Library window')
        self.user_id = user_id
        self.id=id
        self.title_win=title
    def game_button_clicked(self):
        logger.info('access to game window')
        self.Game = QtWidgets.QWidget()
        self.ui = Ui_Game(self.id,self.user_id)
        self.ui.setupUi(self.Game)
        self.Game.show()

    def smv_button_clicked(self):
        logger.info('access to smv window')
        self.smv = QtWidgets.QWidget()
        self.ui = Ui_smv(self.id)
        self.ui.setupUi(self.smv)
        self.smv.show()

    def material_button_clicked(self):
        logger.info('access to material window')
        self.material = QtWidgets.QWidget()
        self.ui = Ui_material(self.id)
        self.ui.setupUi(self.material)
        self.material.show()

    def setupUi(self, openlib):
        openlib.setObjectName("openlib")
        openlib.resize(675, 526)
        openlib.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.title = QtWidgets.QLabel(openlib)
        self.title.setGeometry(QtCore.QRect(210, 10, 251, 21))
        self.title.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"font: 10pt \"Lemon\";\n"
"color: rgb(134, 15, 0);")
        self.title.setText(self.title_win)
        self.title.setObjectName("title")
        self.label = QtWidgets.QLabel(openlib)
        self.label.setGeometry(QtCore.QRect(0, 0, 681, 531))
        self.label.setText("")
        self.label.setPixmap(QtGui.QPixmap("Images/4.jpg"))
        self.label.setScaledContents(True)
        self.label.setObjectName("label")
        self.game_button = QtWidgets.QPushButton(openlib)
        self.game_button.setGeometry(QtCore.QRect(30, 90, 101, 31))
        font = QtGui.QFont()
        font.setFamily("Russo One")
        font.setPointSize(14)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.game_button.setFont(font)
        self.game_button.setStyleSheet("font: 14pt \"Russo One\";\n"
"color: rgb(255, 247, 128);\n"
"background-color: rgb(153, 0, 28);")
        self.game_button.setObjectName("game_button")
        self.smv_button = QtWidgets.QPushButton(openlib)
        self.smv_button.setGeometry(QtCore.QRect(30, 160, 101, 31))
        font = QtGui.QFont()
        font.setFamily("Russo One")
        font.setPointSize(12)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.smv_button.setFont(font)
        self.smv_button.setStyleSheet("font: 12pt \"Russo One\";\n"
"color: rgb(255, 247, 128);\n"
"background-color: rgb(153, 0, 28);")
        self.smv_button.setObjectName("smv_button")
        self.material_button = QtWidgets.QPushButton(openlib)
        self.material_button.setGeometry(QtCore.QRect(30, 230, 101, 31))
        font = QtGui.QFont()
        font.setFamily("Russo One")
        font.setPointSize(14)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.material_button.setFont(font)
        self.material_button.setStyleSheet("font: 14pt \"Russo One\";\n"
"color: rgb(255, 247, 128);\n"
"background-color: rgb(153, 0, 28);")
        self.material_button.setObjectName("material_button")
        self.exit_button = QtWidgets.QPushButton(openlib)
        self.exit_button.setGeometry(QtCore.QRect(30, 300, 101, 31))
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
        self.title.raise_()
        self.game_button.raise_()
        self.smv_button.raise_()
        self.material_button.raise_()
        self.exit_button.raise_()

        self.game_button.clicked.connect(self.game_button_clicked)
        self.smv_button.clicked.connect(self.smv_button_clicked)
        self.material_button.clicked.connect(self.material_button_clicked)
        self.exit_button.clicked.connect(openlib.close)
        self.retranslateUi(openlib)
        QtCore.QMetaObject.connectSlotsByName(openlib)

    def retranslateUi(self, openlib):
        _translate = QtCore.QCoreApplication.translate
        openlib.setWindowTitle(_translate("openlib", "Library"))
        self.game_button.setText(_translate("openlib", "Game"))
        self.smv_button.setText(_translate("openlib", "SMV File"))
        self.material_button.setText(_translate("openlib", "Material"))
        self.exit_button.setText(_translate("openlib", "Exit"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    openlib = QtWidgets.QWidget()
    ui = Ui_openlib()
    ui.setupUi(openlib)
    openlib.show()
    sys.exit(app.exec_())
