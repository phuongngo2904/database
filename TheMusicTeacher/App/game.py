from PyQt5 import QtCore, QtGui, QtWidgets
from access_to_db import *

logger=record()
mydb =db()
mycursor = mydb.cursor()
class Ui_Game(object):
    def __init__(self,lib_id,user_id):
        logger.info('displayed game window')
        self.lib_id=lib_id
        self.user_id=user_id
    def display_game(self):
        with open('../SQL/game_window.sql') as f:
            commands = f.read().split(';')
        for command in commands:
            if command.find('select g.g_id, g.name from game g, uses_game ug') != -1:
                command = command.replace('@libid', '%s')
                mycursor.execute(command, (self.lib_id,))
                result = mycursor.fetchall()
                row = 0
                column = 0
                if len(result) == 0:
                    pass
                elif len(result) != 0:
                    self.tableWidget.setRowCount(len(result))
                    for x in result:
                        self.tableWidget.setItem(row, column, QtWidgets.QTableWidgetItem(str(x[0])))
                        self.tableWidget.setItem(row, column + 1, QtWidgets.QTableWidgetItem(str(x[1])))
                        row += 1
        # display game currently playing
            elif command.find('select g.name, pg.save_state from plays_game pg, game g') != -1:
                command = command.replace('@user_id', '%s')
                mycursor.execute(command, (self.user_id,))
                result1 = mycursor.fetchall()
                row = 0
                column = 0
                if len(result1) == 0:
                    pass
                elif len(result1) != 0:
                    self.tableWidget_2.setRowCount(len(result1))
                    for x in result1:
                        self.tableWidget_2.setItem(row, column, QtWidgets.QTableWidgetItem(str(x[0])))
                        self.tableWidget_2.setItem(row, column + 1, QtWidgets.QTableWidgetItem(str(x[1])))
                        row += 1


    def setupUi(self, Game):
        Game.setObjectName("Game")
        Game.resize(750, 696)
        Game.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.label = QtWidgets.QLabel(Game)
        self.label.setGeometry(QtCore.QRect(0, 20, 241, 191))
        self.label.setText("")
        self.label.setPixmap(QtGui.QPixmap("Images/12.jpg"))
        self.label.setScaledContents(True)
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(Game)
        self.label_2.setGeometry(QtCore.QRect(480, 480, 241, 191))
        self.label_2.setText("")
        self.label_2.setPixmap(QtGui.QPixmap("Images/12.jpg"))
        self.label_2.setScaledContents(True)
        self.label_2.setObjectName("label_2")
        self.title = QtWidgets.QLabel(Game)
        self.title.setGeometry(QtCore.QRect(250, 80, 61, 21))
        self.title.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"font: 10pt \"Lemon\";\n"
"color: rgb(134, 15, 0);")
        self.title.setObjectName("title")
        self.tableWidget = QtWidgets.QTableWidget(Game)
        self.tableWidget.setGeometry(QtCore.QRect(230, 110, 321, 181))
        self.tableWidget.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"font: 8pt \"Lemon\";\n"
"color: rgb(134, 15, 0);")
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(2)
        self.tableWidget.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(1, item)
        self.title_2 = QtWidgets.QLabel(Game)
        self.title_2.setGeometry(QtCore.QRect(230, 320, 271, 21))
        self.title_2.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"font: 10pt \"Lemon\";\n"
"color: rgb(134, 15, 0);")
        self.title_2.setObjectName("title_2")
        self.tableWidget_2 = QtWidgets.QTableWidget(Game)
        self.tableWidget_2.setGeometry(QtCore.QRect(230, 350, 321, 191))
        self.tableWidget_2.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"font: 8pt \"Lemon\";\n"
"color: rgb(134, 15, 0);")
        self.tableWidget_2.setObjectName("tableWidget_2")
        self.tableWidget_2.setColumnCount(2)
        self.tableWidget_2.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_2.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_2.setHorizontalHeaderItem(1, item)
        self.display_game()
        self.retranslateUi(Game)
        QtCore.QMetaObject.connectSlotsByName(Game)

    def retranslateUi(self, Game):
        _translate = QtCore.QCoreApplication.translate
        Game.setWindowTitle(_translate("Game", "Game"))
        self.title.setText(_translate("Game", "Game"))
        item = self.tableWidget.horizontalHeaderItem(0)
        item.setText(_translate("Game", "Game ID"))
        item = self.tableWidget.horizontalHeaderItem(1)
        item.setText(_translate("Game", "Name"))
        self.title_2.setText(_translate("Game", "Games -- Currently playing"))
        item = self.tableWidget_2.horizontalHeaderItem(0)
        item.setText(_translate("Game", "Name"))
        item = self.tableWidget_2.horizontalHeaderItem(1)
        item.setText(_translate("Game", "Save State"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Game = QtWidgets.QWidget()
    ui = Ui_Game()
    ui.setupUi(Game)
    Game.show()
    sys.exit(app.exec_())
