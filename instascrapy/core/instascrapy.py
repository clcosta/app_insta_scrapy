# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '.\ui\instascrapy.ui'
#
# Created by: PyQt5 UI code generator 5.15.5
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets
from .colors import POPUP_ERROR
from . import VERSION

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(684, 805)
        MainWindow.setMinimumSize(QtCore.QSize(500, 700))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/icone/icon.ico"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        MainWindow.setWindowIcon(icon)
        MainWindow.setStyleSheet("background-color: rgb(10, 10, 10);")
        MainWindow.setToolButtonStyle(QtCore.Qt.ToolButtonIconOnly)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.topbar = QtWidgets.QFrame(self.centralwidget)
        self.topbar.setMaximumSize(QtCore.QSize(16777215, 35))
        self.topbar.setStyleSheet("")
        self.topbar.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.topbar.setFrameShadow(QtWidgets.QFrame.Raised)
        self.topbar.setObjectName("topbar")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.topbar)
        self.horizontalLayout_2.setContentsMargins(0, 5, 0, 0)
        self.horizontalLayout_2.setSpacing(0)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.frame_error = QtWidgets.QFrame(self.topbar)
        self.frame_error.setMaximumSize(QtCore.QSize(450, 35))
        self.frame_error.setStyleSheet(POPUP_ERROR)
        self.frame_error.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_error.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_error.setObjectName("frame_error")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout(self.frame_error)
        self.horizontalLayout_3.setContentsMargins(10, 3, 10, 3)
        self.horizontalLayout_3.setSpacing(3)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.lb_error = QtWidgets.QLabel(self.frame_error)
        self.lb_error.setAlignment(QtCore.Qt.AlignCenter)
        self.lb_error.setObjectName("lb_error")
        self.horizontalLayout_3.addWidget(self.lb_error)
        self.btn_error = QtWidgets.QPushButton(self.frame_error)
        self.btn_error.setMaximumSize(QtCore.QSize(20, 20))
        self.btn_error.setStyleSheet("QPushButton {\n"
"    border-radius: 5px;\n"
"    background-position: center;\n"
"    background-image: url(:/close_image/cil-x.png);\n"
"    \n"
"    background-color: rgb(10,10,10);\n"
"}\n"
"QPushButton:hover{\n"
"    background-color: rgb(55,55,55);\n"
"    color: rgb(200, 200, 200);\n"
"}\n"
"QPushButton:pressed{\n"
"    background-color: rgb(100,100,100);\n"
"    color: rgb(200, 200, 200);\n"
"}")
        self.btn_error.setText("")
        self.btn_error.setObjectName("btn_error")
        self.horizontalLayout_3.addWidget(self.btn_error)
        self.horizontalLayout_2.addWidget(self.frame_error)
        self.verticalLayout.addWidget(self.topbar)
        self.body = QtWidgets.QFrame(self.centralwidget)
        self.body.setStyleSheet("")
        self.body.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.body.setFrameShadow(QtWidgets.QFrame.Raised)
        self.body.setObjectName("body")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.body)
        self.horizontalLayout.setContentsMargins(0, 30, 0, 30)
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.content = QtWidgets.QFrame(self.body)
        self.content.setMaximumSize(QtCore.QSize(450, 550))
        self.content.setStyleSheet("QFrame{\n"
"    background-color: rgb(30,30,30);\n"
"    border-radius: 10px;\n"
"}")
        self.content.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.content.setFrameShadow(QtWidgets.QFrame.Raised)
        self.content.setObjectName("content")
        self.logo = QtWidgets.QFrame(self.content)
        self.logo.setGeometry(QtCore.QRect(83, 45, 283, 89))
        self.logo.setMinimumSize(QtCore.QSize(283, 89))
        self.logo.setMaximumSize(QtCore.QSize(283, 89))
        self.logo.setStyleSheet("background-image: url(:/logo/logo.png);\n"
"backroung-repeat: no-repeat;\n"
"background-position: center;\n"
"border-radius: 6px;")
        self.logo.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.logo.setFrameShadow(QtWidgets.QFrame.Raised)
        self.logo.setObjectName("logo")
        self.btn_configuracoes = QtWidgets.QPushButton(self.content)
        self.btn_configuracoes.setGeometry(QtCore.QRect(155, 500, 130, 50))
        self.btn_configuracoes.setMaximumSize(QtCore.QSize(280, 50))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(9)
        font.setBold(False)
        font.setWeight(50)
        self.btn_configuracoes.setFont(font)
        self.btn_configuracoes.setStyleSheet("QPushButton{\n"
"    background-color: rgb(30,30,30);\n"
"    border: 1px solid rgb(30,30,30);\n"
"    color: rgb(255,255,255);\n"
"}\n"
"QPushButton:hover{\n"
"    color: rgb(210,210,210);\n"
"}\n"
"QPushButton:pressed{\n"
"    color: rgb(27, 107, 106);\n"
"}")
        self.btn_configuracoes.setObjectName("btn_configuracoes")
        self.btn_cancelar = QtWidgets.QPushButton(self.content)
        self.btn_cancelar.setGeometry(QtCore.QRect(80, 430, 135, 50))
        self.btn_cancelar.setMinimumSize(QtCore.QSize(135, 0))
        self.btn_cancelar.setMaximumSize(QtCore.QSize(135, 50))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(9)
        font.setBold(False)
        font.setWeight(50)
        self.btn_cancelar.setFont(font)
        self.btn_cancelar.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.btn_cancelar.setStyleSheet("QPushButton{\n"
"    background-color:  rgb(75,75,75);\n"
"    border: 2px solid rgb(70,70,70);\n"
"    border-radius: 5px;\n"
"    color: rgb(255,255,255);\n"
"}\n"
"QPushButton:hover{\n"
"    border: 2px solid rgb(140,140,140);\n"
"}\n"
"QPushButton:pressed{\n"
"    background-color: rgb(27, 107, 106);\n"
"    border: 2px solid rgb(0, 255, 252);\n"
"}")
        self.btn_cancelar.setObjectName("btn_cancelar")
        self.lb_ajustes = QtWidgets.QLabel(self.content)
        self.lb_ajustes.setGeometry(QtCore.QRect(80, 490, 280, 20))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(10)
        font.setItalic(False)
        self.lb_ajustes.setFont(font)
        self.lb_ajustes.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.lb_ajustes.setStyleSheet("color :rgb(120,120,120)")
        self.lb_ajustes.setAlignment(QtCore.Qt.AlignCenter)
        self.lb_ajustes.setObjectName("lb_ajustes")
        self.btn_como_utilizar = QtWidgets.QPushButton(self.content)
        self.btn_como_utilizar.setGeometry(QtCore.QRect(235, 395, 131, 23))
        self.btn_como_utilizar.setStyleSheet("QPushButton{\n"
"    color: rgb(0, 170, 255);\n"
"    background-color: rgb(30,30,30,);\n"
"    border: 1px solid  rgb(30,30,30);\n"
"}\n"
"QPushButton:hover{\n"
"    color: rgb(0, 149, 200);\n"
"}\n"
"QPushButton:pressed{\n"
"    color: rgb(0, 149, 152);\n"
"}")
        self.btn_como_utilizar.setObjectName("btn_como_utilizar")
        self.lb_title = QtWidgets.QLabel(self.content)
        self.lb_title.setGeometry(QtCore.QRect(75, 150, 300, 50))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(26)
        font.setBold(True)
        font.setWeight(75)
        self.lb_title.setFont(font)
        self.lb_title.setStyleSheet("color: rgb(255, 255, 255);")
        self.lb_title.setObjectName("lb_title")
        self.input_users = QtWidgets.QTextEdit(self.content)
        self.input_users.setGeometry(QtCore.QRect(80, 220, 290, 130))
        self.input_users.setMaximumSize(QtCore.QSize(290, 130))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(12)
        font.setBold(False)
        font.setWeight(50)
        self.input_users.setFont(font)
        self.input_users.viewport().setProperty("cursor", QtGui.QCursor(QtCore.Qt.IBeamCursor))
        self.input_users.setStyleSheet("background-color: rgb(121, 121, 121);")
        self.input_users.setObjectName("input_users")
        self.btn_raspar_dados = QtWidgets.QPushButton(self.content)
        self.btn_raspar_dados.setGeometry(QtCore.QRect(235, 430, 135, 50))
        self.btn_raspar_dados.setMinimumSize(QtCore.QSize(135, 0))
        self.btn_raspar_dados.setMaximumSize(QtCore.QSize(135, 50))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(9)
        font.setBold(False)
        font.setWeight(50)
        self.btn_raspar_dados.setFont(font)
        self.btn_raspar_dados.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.btn_raspar_dados.setStyleSheet("QPushButton{\n"
"    background-color:  rgb(80,80,80);\n"
"    border: 2px solid rgb(70,70,70);\n"
"    border-radius: 5px;\n"
"    color: rgb(255,255,255);\n"
"}\n"
"QPushButton:hover{\n"
"    border: 2px solid rgb(140,140,140);\n"
"}\n"
"QPushButton:pressed{\n"
"    background-color: rgb(27, 107, 106);\n"
"    border: 2px solid rgb(0, 255, 252);\n"
"}")
        self.btn_raspar_dados.setObjectName("btn_raspar_dados")
        self.lb_limitador = QtWidgets.QLabel(self.content)
        self.lb_limitador.setGeometry(QtCore.QRect(85, 350, 140, 50))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(22)
        font.setBold(True)
        font.setWeight(75)
        self.lb_limitador.setFont(font)
        self.lb_limitador.setStyleSheet("color: rgb(255, 255, 255);")
        self.lb_limitador.setObjectName("lb_limitador")
        self.input_limitador = QtWidgets.QLineEdit(self.content)
        self.input_limitador.setGeometry(QtCore.QRect(235, 368, 138, 21))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.input_limitador.setFont(font)
        self.input_limitador.setStyleSheet("background-color: rgb(121, 121, 121);\n"
"border: 2px solid rgb(70,70,70);\n"
"border-radius: 5px;")
        self.input_limitador.setInputMask("")
        self.input_limitador.setText("")
        self.input_limitador.setAlignment(QtCore.Qt.AlignCenter)
        self.input_limitador.setObjectName("input_limitador")
        self.horizontalLayout.addWidget(self.content)
        self.verticalLayout.addWidget(self.body)
        self.footer = QtWidgets.QFrame(self.centralwidget)
        self.footer.setMaximumSize(QtCore.QSize(16777215, 35))
        self.footer.setStyleSheet("background-color: rgb(15,15,15);")
        self.footer.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.footer.setFrameShadow(QtWidgets.QFrame.Raised)
        self.footer.setObjectName("footer")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.footer)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.lb_credits = QtWidgets.QLabel(self.footer)
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(8)
        self.lb_credits.setFont(font)
        self.lb_credits.setLayoutDirection(QtCore.Qt.RightToLeft)
        self.lb_credits.setStyleSheet("color :rgb(120,120,120)")
        self.lb_credits.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.lb_credits.setObjectName("lb_credits")
        self.verticalLayout_2.addWidget(self.lb_credits)
        self.verticalLayout.addWidget(self.footer)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "InstaScrapy"))
        self.lb_error.setText(_translate("MainWindow", "ERROR"))
        self.btn_configuracoes.setText(_translate("MainWindow", "CONFIGURA????ES"))
        self.btn_cancelar.setText(_translate("MainWindow", "FECHAR"))
        self.lb_ajustes.setText(_translate("MainWindow", "Clique aqui para ajustar as Configura????es"))
        self.btn_como_utilizar.setText(_translate("MainWindow", "N??o sabe como utliziar?"))
        self.lb_title.setText(_translate("MainWindow", "Digite os usuarios"))
        self.input_users.setPlaceholderText(_translate("MainWindow", "Cada usuario em uma linha."))
        self.btn_raspar_dados.setText(_translate("MainWindow", "RASPAR DADOS"))
        self.lb_limitador.setText(_translate("MainWindow", "Limitador"))
        self.input_limitador.setPlaceholderText(_translate("MainWindow", "0 (sem limitador)"))
        self.lb_credits.setText(_translate("MainWindow", f"{VERSION}"))
import file_rc_rc


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
