import os
import sys
import webbrowser

from PyQt5 import QtCore, QtWidgets
from PyQt5.QtWidgets import QApplication, QMainWindow

from .core import Ui_ConfiguracoesWindow, Ui_MainWindow, Autenticacao
from .core.colors import *

from .instascraping import InstaScraping

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
        self.initial.btn_cancelar.clicked.connect(self.cancelar_thread)

        ## Botão "não sabe utilizar" -> redirecionamento para o site
        self.initial.btn_como_utilizar.clicked.connect(self.abrir_how_to_use)

        ## Botão "Raspar dados" -> InstaScraping
        self.initial.btn_raspar_dados.clicked.connect(self.scraping)

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

    def cancelar_thread(self):
        os.system("taskkill /f /im  python.exe")

    def scraping(self):

        instascraping = InstaScraping()
        ## Mostar erro
        def showMessage(message, message_color=POPUP_ERROR):
            self.initial.frame_error.show()
            self.initial.frame_error.setStyleSheet(message_color)
            self.initial.lb_error.setText(message)

        ## Checar o campo de input_users
        def check_fields():
            if self.initial.input_users.toPlainText() == "":
                showMessage(" Preencha corretamente o campo de usuarios! ")
            else:
                showMessage(
                    " Iniciando Scraping! ", message_color=POPUP_NEUTRO
                )
                return True

        def scraping_geral():
            try:
                geral_data = instascraping.get_users_follows_infos(
                    users=lista_de_perfils, sleep_time=10
                )
                instascraping.transformar_dict_em_sheets(
                    data=geral_data, range_name="Geral"
                )
            except Exception as error:
                showMessage(f'Erro durante geral -> {error}')
        def scraping_posts():
            try:
                data = instascraping.get_posts(lista_de_perfils, sleep_time=10)
                if data != None:
                    instascraping.transformar_posts_dict_em_sheets(
                        data, lista_de_perfils
                    )
                showMessage(" Raspagem realizada com Sucesso! ", POPUP_OK)
            except Exception as error:
                showMessage(f'Erro durante posts -> {error}')


        check = check_fields()
        ## Está verificação de segurança não é necessário
        if not check:
            return 
        
        texto = self.initial.input_users.toPlainText()
        users = texto.split("\n")
        lista_de_perfils = [user for user in users if user not in ("",'\n')]
        scraping_geral()
        scraping_posts()
        return 

class TelaConfiguracoes(QMainWindow):

    auth = Autenticacao()

    def __init__(self):
        QMainWindow.__init__(self)
        self.settings = Ui_ConfiguracoesWindow()
        self.settings.setupUi(self)

        ## remover titulo da jánela
        self.setWindowFlag(QtCore.Qt.FramelessWindowHint)
        self.setAttribute(QtCore.Qt.WA_TranslucentBackground)

        ## Definir pré textos
        self.pre_textos()

        ## Abrir jnalea inicial
        self.settings.btn_cancelar.clicked.connect(self.abrir_initial)

        ## Atualizar informações
        self.settings.btn_atualizar.clicked.connect(self.update_settings)

        ## Mostrar tela
        self.show()

    def abrir_initial(self):
        initial = TelaInicial()
        self.hide()
        self.ui = initial

    def pre_textos(self):
        self.settings.input_user.setText(self.auth.username)
        self.settings.input_password.setText(self.auth.password)
        self.settings.input_sessionid.setText(self.auth.session_id)
        self.settings.input_sheetid.setText(self.auth.sheet_id)
        self.settings.input_aba_sheets.setText(self.auth.connection_range)

    def update_settings(self):

        ## Mostar erro
        def showMessage(message, message_color=LABEL_ERROR):
            self.settings.lb_configs.setStyleSheet(message_color)
            self.settings.lb_configs.setText(message)

        ## Checar se os campos estão preenchidos
        def check_fields():
            lista_inputs = [
                self.settings.input_user,
                self.settings.input_password,
                self.settings.input_sessionid,
                self.settings.input_sheetid,
                self.settings.input_aba_sheets,
            ]

            check = True
            for i, inputs in enumerate(lista_inputs):
                if inputs.text() == "":
                    check = False
                    inputs.setStyleSheet(INPUT_ERROR)
                    showMessage(" Update Error ")

                elif inputs.text() != "":
                    inputs.setStyleSheet(INPUT_OK)

            if check:
                showMessage("  Atualizado! ", message_color=LABEL_VERDE)
                return True
            else:
                return False

        check = check_fields()

        if check:
            ## Atualizar informações de settings nos arquivos do instascraping
            data = {
                "USERNAME": self.settings.input_user.text(),
                "PASSWORD": self.settings.input_password.text(),
                "SESSION_ID": self.settings.input_sessionid.text(),
                "SHEET_ID": self.settings.input_sheetid.text(),
                "CONNECTION_RANGE": self.settings.input_aba_sheets.text(),
            }
            self.auth.update_auth(data=data)
