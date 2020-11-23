from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QMessageBox
from user_dashboard import Ui_student_dashboard
from resetpw import Ui_resetpw
from signup import Ui_register_window
import hashlib
from access_to_db import *

logger=record()
mydb= db()
mycursor = mydb.cursor()

class Ui_MainWindow(object):
    def exit_button_clicked(self):
        logger.info('Abort the program')
        MainWindow.close()
    def register_button_clicked(self):
        self.register_window = QtWidgets.QWidget()
        self.ui = Ui_register_window()
        self.ui.setupUi(self.register_window)
        self.register_window.show()
    def resetpw_clicked(self):
        self.resetpw = QtWidgets.QWidget()
        self.ui = Ui_resetpw()
        self.ui.setupUi(self.resetpw)
        self.resetpw.show()
    def login_clicked(self):
        with open('../SQL/login.sql') as f:
            commands = f.read().split(';')
        for command in commands:
            if command.find('SELECT u_id, username, hashed_password FROM user') != -1:
                command = command.replace('@user_username', '%s')
                mycursor.execute(command, (self.id_lineedit.text(),))
                result = mycursor.fetchall()
                if len(result) == 0:
                    self.id_lineedit.clear()
                    self.pw_lineedit.clear()
                    message = QMessageBox()
                    message.setWindowTitle("FAIL !")
                    message.setText("Invalid user.")
                    logger.warning('User not found.')
                    message.exec()
                else:
                    for x in result:
                        id = x[0]
                        username = x[1]
                        pw = x[2]
                    self.hash_pw = hashlib.sha1(self.pw_lineedit.text().encode("UTF-8")).hexdigest()
                    if self.id_lineedit.text() == username and self.hash_pw == pw:  # when user enter id and passw correctly
                        self.id_lineedit.clear()
                        self.pw_lineedit.clear()
                        logger.info('Logged In')
                        self.student_dashboard = QtWidgets.QWidget()
                        self.ui = Ui_student_dashboard(id)
                        self.ui.setupUi(self.student_dashboard)
                        self.student_dashboard.show()
                    elif self.id_lineedit.text() == username and self.hash_pw != pw:  # when user enter username correctly but wrong password
                        message = QMessageBox()
                        message.setWindowTitle("FAIL !")
                        message.setText("Incorrect password.")
                        logger.warning('Incorrect password.')
                        message.exec()
                        self.pw_lineedit.clear()
            else:
                pass

    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(772, 850)
        MainWindow.setStyleSheet("background-color: rgb(244, 244, 244);")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.login_button = QtWidgets.QPushButton(self.centralwidget)
        self.login_button.setGeometry(QtCore.QRect(340, 680, 101, 31))
        font = QtGui.QFont()
        font.setFamily("Russo One")
        font.setPointSize(14)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.login_button.setFont(font)
        self.login_button.setStyleSheet("font: 14pt \"Russo One\";\n"
"color: rgb(255, 247, 128);\n"
"background-color: rgb(153, 0, 28);")
        self.login_button.setObjectName("login_button")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(-20, -60, 871, 751))
        self.label.setText("")
        self.label.setPixmap(QtGui.QPixmap("Images/800px_COLOURBOX4294785.jpg"))
        self.label.setScaledContents(True)
        self.label.setObjectName("label")
        self.userid = QtWidgets.QLabel(self.centralwidget)
        self.userid.setGeometry(QtCore.QRect(270, 570, 71, 31))
        self.userid.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"font: 10pt \"Lemon\";\n"
"color: rgb(134, 15, 0);")
        self.userid.setObjectName("User id")
        self.password = QtWidgets.QLabel(self.centralwidget)
        self.password.setGeometry(QtCore.QRect(260, 610, 101, 31))
        self.password.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"font: 10pt \"Lemon\";\n"
"color: rgb(134, 15, 0);")
        self.password.setObjectName("password")
        self.id_lineedit = QtWidgets.QLineEdit(self.centralwidget)
        self.id_lineedit.setGeometry(QtCore.QRect(370, 570, 361, 31))
        self.id_lineedit.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"font: 10pt \"Lemon\";\n"
"color: rgb(134, 15, 0);")
        self.id_lineedit.setObjectName("id_lineedit")
        self.pw_lineedit = QtWidgets.QLineEdit(self.centralwidget)
        self.pw_lineedit.setGeometry(QtCore.QRect(370, 610, 361, 31))
        self.pw_lineedit.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"font: 10pt \"Lemon\";\n"
"color: rgb(134, 15, 0);")
        self.pw_lineedit.setEchoMode(QtWidgets.QLineEdit.Password)
        self.pw_lineedit.setObjectName("pw_lineedit")
        self.resetpw_button = QtWidgets.QPushButton(self.centralwidget)
        self.resetpw_button.setGeometry(QtCore.QRect(240, 740, 111, 31))
        font = QtGui.QFont()
        font.setFamily("Russo One")
        font.setPointSize(12)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.resetpw_button.setFont(font)
        self.resetpw_button.setStyleSheet("font: 12pt \"Russo One\";\n"
"color: rgb(255, 247, 128);\n"
"background-color: rgb(153, 0, 28);")
        self.resetpw_button.setObjectName("resetpw_button")
        self.register_button = QtWidgets.QPushButton(self.centralwidget)
        self.register_button.setGeometry(QtCore.QRect(360, 740, 111, 31))
        font = QtGui.QFont()
        font.setFamily("Russo One")
        font.setPointSize(14)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.register_button.setFont(font)
        self.register_button.setStyleSheet("font: 14pt \"Russo One\";\n"
"color: rgb(255, 247, 128);\n"
"background-color: rgb(153, 0, 28);")
        self.register_button.setObjectName("register_button")
        self.exit_button = QtWidgets.QPushButton(self.centralwidget)
        self.exit_button.setGeometry(QtCore.QRect(480, 740, 111, 31))
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
        self.login_button.raise_()
        self.userid.raise_()
        self.password.raise_()
        self.id_lineedit.raise_()
        self.pw_lineedit.raise_()
        self.resetpw_button.raise_()
        self.register_button.raise_()
        self.exit_button.raise_()
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 772, 26))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.login_button.clicked.connect(self.login_clicked)
        self.exit_button.clicked.connect(self.exit_button_clicked)
        self.resetpw_button.clicked.connect(self.resetpw_clicked)
        self.register_button.clicked.connect(self.register_button_clicked)
        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Log In"))
        self.login_button.setText(_translate("MainWindow", "LOG IN"))
        self.userid.setText(_translate("MainWindow", "User Id"))
        self.password.setText(_translate("MainWindow", "Password"))
        self.resetpw_button.setText(_translate("MainWindow", "Forgot PW"))
        self.register_button.setText(_translate("MainWindow", "Register"))
        self.exit_button.setText(_translate("MainWindow", "Exit"))



if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
