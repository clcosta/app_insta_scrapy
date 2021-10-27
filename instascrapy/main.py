from .core import Ui_MainWindow, Ui_ConfiguracoesWindow
import sys

from PyQt5 import QtCore, QtWidgets
from PyQt5.QtWidgets import QApplication, QMainWindow

from .core.colors import *
import webbrowser

class TelaInicial(QMainWindow):
    
    URL_HTU = "http://insta-scrapy.herokuapp.com/como-utilizar"

    def __init__(self):
        QMainWindow.__init__(self)
        self.initial = Ui_MainWindow()
        self.initial.setupUi(self)
        
        ### Botão fechar PopPup Error
        self.initial.btn_error.clicked.connect(self.close_popup)
        ## Esconder PopPup error 
        self.initial.frame_error.hide()

        ## Botão "não sabe utilizar" -> redirecionamento para o site
        self.initial.btn_como_utilizar.clicked.connect(self.abrir_how_to_use)

        ## Abrir janela de settings
        self.initial.btn_configuracoes.clicked.connect(self.abrir_settings)

        # Mostrar tela
        self.show()
    
    def close_popup(self):
        self.initial.frame_error.hide()

    def abrir_how_to_use(self):
        webbrowser.open_new_tab(self.URL_HTU)

    def abrir_settings(self):
        settings = TelaConfiguracoes()
        self.hide()
        self.ui = settings

class TelaConfiguracoes(QMainWindow):

    def __init__(self):
        QMainWindow.__init__(self)
        self.settings = Ui_ConfiguracoesWindow()
        self.settings.setupUi(self)
        
        ## remover titulo da jánela
        self.setWindowFlag(QtCore.Qt.FramelessWindowHint)
        self.setAttribute(QtCore.Qt.WA_TranslucentBackground)

        ## Abrir jnalea inicial
        self.settings.btn_cancelar.clicked.connect(self.abrir_initial)

        ## Mostrar tela
        self.show()
    
    def abrir_initial(self):
        initial = TelaInicial()
        self.hide()
        self.ui = initial