# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'LoginWidget.ui'
#
# Created by: PyQt5 UI code generator 5.15.2
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets
import TicketAir
import HomePage

class Ui_LOGINWidget(object):
    def setupUi(self, LOGINWidget):
        LOGINWidget.setObjectName("LOGINWidget")
        LOGINWidget.resize(609, 700)
        LOGINWidget.setMinimumSize(QtCore.QSize(500, 700))
        self.Login = QtWidgets.QVBoxLayout(LOGINWidget)
        self.Login.setContentsMargins(0, 0, 0, 0)
        self.Login.setSpacing(0)
        self.Login.setObjectName("Login")
        self.top = QtWidgets.QFrame(LOGINWidget)
        self.top.setMaximumSize(QtCore.QSize(16777215, 40))
        self.top.setBaseSize(QtCore.QSize(0, 0))
        self.top.setStyleSheet("background-color: rgb(255, 255, 127);")
        self.top.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.top.setFrameShadow(QtWidgets.QFrame.Raised)
        self.top.setObjectName("top")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.top)
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_2.setSpacing(0)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.ERRORFrame = QtWidgets.QFrame(self.top)
        self.ERRORFrame.setMaximumSize(QtCore.QSize(450, 35))
        self.ERRORFrame.setStyleSheet("background-color: rgb(170, 255, 127);\n"
                                      "border-radius: 5px;")
        self.ERRORFrame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.ERRORFrame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.ERRORFrame.setObjectName("ERRORFrame")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout(self.ERRORFrame)
        self.horizontalLayout_3.setContentsMargins(6, 6, 6, 6)
        self.horizontalLayout_3.setSpacing(4)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.ERRORLabel = QtWidgets.QLabel(self.ERRORFrame)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.ERRORLabel.setFont(font)
        self.ERRORLabel.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.ERRORLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.ERRORLabel.setObjectName("ERRORLabel")
        self.horizontalLayout_3.addWidget(self.ERRORLabel)
        self.ERRORXButton = QtWidgets.QPushButton(self.ERRORFrame)
        self.ERRORXButton.setMaximumSize(QtCore.QSize(15, 15))
        self.ERRORXButton.setStyleSheet("QPushButton {\n"
                                        "    border-raadius: 5px;\n"
                                        "    background-position: centre;\n"
                                        "    border: 2px solid;\n"
                                        "}\n"
                                        "\n"
                                        "QPushButton:hover {\n"
                                        "    background-color: rgb(50, 50, 50);\n"
                                        "    color: rgb(255, 234, 70);\n"
                                        "}\n"
                                        "\n"
                                        "QPushButton:pressed {\n"
                                        "    background-color: rgb(35, 35, 35);\n"
                                        "    color: rgb(255, 234, 70);\n"
                                        "}")
        self.ERRORXButton.setObjectName("ERRORXButton")
        self.horizontalLayout_3.addWidget(self.ERRORXButton)
        self.horizontalLayout_2.addWidget(self.ERRORFrame)
        self.Login.addWidget(self.top)
        self.content = QtWidgets.QFrame(LOGINWidget)
        self.content.setStyleSheet("background-color: rgb(143, 143, 143);")
        self.content.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.content.setFrameShadow(QtWidgets.QFrame.Raised)
        self.content.setObjectName("content")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.content)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.main = QtWidgets.QFrame(self.content)
        self.main.setMaximumSize(QtCore.QSize(450, 550))
        self.main.setStyleSheet("background-color: rgb(57, 57, 57);\n"
                                "border-radius: 10px;")
        self.main.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.main.setFrameShadow(QtWidgets.QFrame.Raised)
        self.main.setObjectName("main")
        self.USERLabel = QtWidgets.QLineEdit(self.main)
        self.USERLabel.setGeometry(QtCore.QRect(120, 330, 220, 45))
        font = QtGui.QFont()
        font.setPointSize(8)
        self.USERLabel.setFont(font)
        self.USERLabel.setStyleSheet("QLineEdit {\n"
                                     "    border: 2px solid rgb(45,45,45);\n"
                                     "    border-radius: 5px;    \n"
                                     "    padding: 15 px;\n"
                                     "    background-color: rgb(30,30,30);\n"
                                     "    color: rgb(200, 200, 200);\n"
                                     "}\n"
                                     "\n"
                                     "QLineEdit:hover {\n"
                                     "    border: 2px solid rgb(55,55,55);\n"
                                     "}\n"
                                     "\n"
                                     "QLineEdit:focus {\n"
                                     "    border: 2px solid rgb(255,255,127);\n"
                                     "    color: rgb(200,200,200)\n"
                                     "}")
        self.USERLabel.setText("")
        self.USERLabel.setMaxLength(100)
        self.USERLabel.setObjectName("USERLabel")
        self.PASSWORDLabel = QtWidgets.QLineEdit(self.main)
        self.PASSWORDLabel.setGeometry(QtCore.QRect(120, 380, 220, 45))
        font = QtGui.QFont()
        font.setPointSize(8)
        self.PASSWORDLabel.setFont(font)
        self.PASSWORDLabel.setStyleSheet("QLineEdit {\n"
                                         "    border: 2px solid rgb(45,45,45);\n"
                                         "    border-radius: 5px;    \n"
                                         "    padding: 15 px;\n"
                                         "    background-color: rgb(30,30,30);\n"
                                         "    color: rgb(200, 200, 200);\n"
                                         "}\n"
                                         "\n"
                                         "QLineEdit:hover {\n"
                                         "    border: 2px solid rgb(55,55,55);\n"
                                         "}\n"
                                         "\n"
                                         "QLineEdit:focus {\n"
                                         "    border: 2px solid rgb(255,255,127);\n"
                                         "    color: rgb(200,200,200)\n"
                                         "}")
        self.PASSWORDLabel.setText("")
        self.PASSWORDLabel.setMaxLength(100)
        self.PASSWORDLabel.setEchoMode(QtWidgets.QLineEdit.Password)
        self.PASSWORDLabel.setObjectName("PASSWORDLabel")
        self.LOGINButton = QtWidgets.QPushButton(self.main)
        self.LOGINButton.setGeometry(QtCore.QRect(120, 490, 201, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.LOGINButton.setFont(font)
        self.LOGINButton.setStyleSheet("QPushButton {\n"
                                       "    background-color: rgb(50, 50, 50);\n"
                                       "    border: 2px solid rgb(60,60,60);\n"
                                       "    border-radius: 5px;\n"
                                       "}\n"
                                       "\n"
                                       "QPushButton:hover {\n"
                                       "    background-color: rgb(60, 60, 60);\n"
                                       "    border: 2px solid rgb(70,70,70);\n"
                                       "    border-radius: 5px;\n"
                                       "}\n"
                                       "\n"
                                       "QPushButton:pressed {\n"
                                       "    background-color: rgb(255, 255, 127);\n"
                                       "    border: 2px solid rgb(0,0,0);\n"
                                       "    border-radius: 5px;\n"
                                       "    \n"
                                       "    color: rgb(35, 35, 35);\n"
                                       "}")
        self.LOGINButton.setObjectName("LOGINButton")
        self.NEWUSERRadioButton = QtWidgets.QRadioButton(self.main)
        self.NEWUSERRadioButton.setGeometry(QtCore.QRect(120, 430, 31, 21))
        self.NEWUSERRadioButton.setStyleSheet("QRadioButton::indicator {\n"
                                              "    border: 3px solid rgb(100,100,100);\n"
                                              "    width: 15px;\n"
                                              "    height: 15px;\n"
                                              "    border-radius: 10px;\n"
                                              "    background-color: rgb(135, 135, 135);\n"
                                              "}\n"
                                              "\n"
                                              "QRadioButton::indicator:checked {\n"
                                              "    border: 3px solid rgb(255,255,0);\n"
                                              "    background-color: rgb(255, 255, 127);\n"
                                              "}")
        self.NEWUSERRadioButton.setText("")
        self.NEWUSERRadioButton.setObjectName("NEWUSERRadioButton")
        self.AVATARFrame = QtWidgets.QFrame(self.main)
        self.AVATARFrame.setGeometry(QtCore.QRect(190, 250, 61, 61))
        self.AVATARFrame.setStyleSheet("QFrame {\n"
                                       "    background-image: url(:/User/img/userv3.png);\n"
                                       "    border: 7px solid;\n"
                                       "}\n"
                                       "")
        self.AVATARFrame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.AVATARFrame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.AVATARFrame.setObjectName("AVATARFrame")
        self.LOGOframe = QtWidgets.QFrame(self.main)
        self.LOGOframe.setGeometry(QtCore.QRect(130, 10, 201, 171))
        self.LOGOframe.setStyleSheet("background-image: url(:/LOGO/img/logo.png);")
        self.LOGOframe.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.LOGOframe.setFrameShadow(QtWidgets.QFrame.Raised)
        self.LOGOframe.setObjectName("LOGOframe")
        self.NEWUSERLabel = QtWidgets.QLabel(self.main)
        self.NEWUSERLabel.setGeometry(QtCore.QRect(150, 430, 71, 21))
        self.NEWUSERLabel.setStyleSheet("color: rgb(200, 200, 200);")
        self.NEWUSERLabel.setObjectName("NEWUSERLabel")
        self.horizontalLayout.addWidget(self.main)
        self.Login.addWidget(self.content)
        self.bottom = QtWidgets.QFrame(LOGINWidget)
        self.bottom.setMaximumSize(QtCore.QSize(16777215, 40))
        self.bottom.setBaseSize(QtCore.QSize(0, 0))
        self.bottom.setStyleSheet("background-color: rgb(255, 255, 127);")
        self.bottom.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.bottom.setFrameShadow(QtWidgets.QFrame.Raised)
        self.bottom.setObjectName("bottom")
        self.Login.addWidget(self.bottom)

        self.retranslateUi(LOGINWidget)
        QtCore.QMetaObject.connectSlotsByName(LOGINWidget)
        self.LOGINButton.clicked.connect(self.login)
        self.ERRORXButton.clicked.connect(self.closePopup)
        self.ERRORFrame.hide()

    def retranslateUi(self, LOGINWidget):
        _translate = QtCore.QCoreApplication.translate
        LOGINWidget.setWindowTitle(_translate("LOGINWidget", "LOGIN"))
        self.ERRORLabel.setText(_translate("LOGINWidget", "ERROR"))
        self.ERRORXButton.setText(_translate("LOGINWidget", "X"))
        self.USERLabel.setPlaceholderText(_translate("LOGINWidget", "USER"))
        self.PASSWORDLabel.setPlaceholderText(_translate("LOGINWidget", "PASSWORD"))
        self.LOGINButton.setText(_translate("LOGINWidget", "LOGIN "))
        self.NEWUSERLabel.setText(_translate("LOGINWidget", "NEW USER"))


    def __init__(self, home):
        self.home = home

    def login(self):
        db = TicketAir.DataBase()
        if self.NEWUSERRadioButton.isChecked():
            if not db.nickTaken(self.USERLabel.text()):
                user = TicketAir.Passenger(self.USERLabel.text(), '', '', self.PASSWORDLabel.text(), self.USERLabel.text())
                db.addUser(user)
                self.home.setUser(user)
            else:
                self.ERRORFrame.show()
                self.ERRORLabel.setText('Username is already taken')
                self.USERLabel.setText('')
                self.PASSWORDLabel.setText('')
        elif db.nickTaken(self.USERLabel.text()):
            user = db.login(self.USERLabel.text(), self.PASSWORDLabel.text())
            if user != None:
                self.home.setUser(user)
            else:
                self.ERRORFrame.show()
                self.ERRORLabel.setText('Wrong password')
                self.PASSWORDLabel.setText('')
        else:
            self.ERRORFrame.show()
            self.ERRORLabel.setText('No user with this nick')
            self.USERLabel.setText('')
            self.PASSWORDLabel.setText('')


    def closePopup(self):
        self.ERRORFrame.hide()


if __name__ == "__main__":
    import sys

    app = QtWidgets.QApplication(sys.argv)
    LOGINWidget = QtWidgets.QWidget()
    ui = Ui_LOGINWidget()
    ui.setupUi(LOGINWidget)
    LOGINWidget.show()
    sys.exit(app.exec_())