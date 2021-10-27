from __future__ import print_function

import os

import pandas as pd
from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build
from rich.console import Console

from .auth import CONNECTION_RANGE, SHEET_ID

BASE_DIR = os.path.dirname(os.path.dirname(__file__))
credentials_path = os.path.join(BASE_DIR, "credentials.json")
token_path = os.path.join(BASE_DIR,"token.json")
class GoogleSheets:

    console = Console()

    CONNECTION_RANGE = CONNECTION_RANGE
    SCOPES = ['https://www.googleapis.com/auth/spreadsheets']
    SHEET_ID = SHEET_ID

    def __init__(self, sheets_id=SHEET_ID, connection_range =CONNECTION_RANGE):
        error_message = "Não foi possivel se conectar ao Google Sheets, verifique as credenciais e o ID da planilha"

        self.connection = self.__connection(sheets_id, connection_range)
        if not self.connection: raise ConnectionError(error_message)

    def __connection(self, sheets_id, connection_range):

        creds = None
        if os.path.exists(token_path):
            self.console.log('Token to connection Google Sheets Detected')
            creds = Credentials.from_authorized_user_file(token_path, self.SCOPES)

        if not creds or not creds.valid:
            if creds and creds.expired and creds.refresh_token:
                creds.refresh(Request())
            else:
                flow = InstalledAppFlow.from_client_secrets_file(
                    credentials_path,
                    self.SCOPES
                )
                self.console.log('Credentials accept')
                creds = flow.run_local_server(open_browser=False)

            with open(token_path, 'w') as token:
                token.write(creds.to_json())

        self.service = build('sheets', 'v4', credentials=creds)

        sheet = self.service.spreadsheets()
        result = sheet.values().get(spreadsheetId=sheets_id,
                                    range=connection_range).execute()
        values = result.get('values', [])

        if not values:
            self.console.log('Conexão falha')
            return False
        else:
            self.console.log('Conexão efetuada com sucesso!')
            return True

    def add_lista_de_valores_em_range(self,args: list, range_name: str,sheets_id: str = SHEET_ID, is_formula: bool = False, mode:str = 'append'):
        values = args
        body = {
        'values': values
        }

        nome_das_abas = self.pegar_nomes_das_abas_existentes()
        if range_name[:-3] in nome_das_abas:
            mode = 'update'

        if is_formula: value_input_option = 'USER_ENTERED'
        else: value_input_option = 'RAW'

        if mode == 'append':
            result = self.service.spreadsheets().values().append(
                        spreadsheetId=sheets_id,
                        range=f"{range_name}",
                        valueInputOption=value_input_option, body=body).execute()
            self.console.log(f'Celulas atualizadas: {result.get("updates").get("updatedCells")}')
        if mode == 'update':
            result = self.service.spreadsheets().values().update(
                        spreadsheetId=sheets_id,
                        range=f"{range_name}",
                        valueInputOption=value_input_option, body=body).execute()
            self.console.log(f'Celulas atualizadas: {result.get("updatedCells")}')
        if mode == 'batchUpdate':
            result = self.service.spreadsheets().values().batchUpdate(
                        spreadsheetId=sheets_id,
                        range=f"{range_name}",
                        valueInputOption=value_input_option, body=body).execute()
            self.console.log(f'Celulas atualizadas: {result.get("totalUpdatedCells")}')

    def ler_valores_em_range(self, range_name: str, sheets_id: str= SHEET_ID):
        sheet = self.service.spreadsheets()
        result = sheet.values().get(spreadsheetId=sheets_id,
                                    range=range_name).execute()
        values = result.get('values', [])
        return values

    def transformar_dict_em_sheets(self, data: dict= None, range_name: str= None):
        colunas = [i for i in data]
        df = pd.DataFrame(data, columns=colunas)
        df_list = [df.columns.values.tolist()] + df.values.tolist()
        self.add_lista_de_valores_em_range(df_list, range_name, mode='update')


    def transformar_posts_dict_em_sheets(self,data,lista_de_perfils):
        for user in lista_de_perfils:
            range_name = f'{user}_posts'
            self.__criar_pagina(name_page=range_name)
            colunas = [i for i in data[user]]
            df = pd.DataFrame(data[user], columns=colunas)
            df = df.fillna('')
            df_list = [df.columns.values.tolist()] + df.values.tolist()
            self.add_lista_de_valores_em_range(df_list, range_name=f"{range_name}"+'!A1')

    def __criar_pagina(self,name_page:str, sheets_id:str = SHEET_ID):
        nome_das_abas = self.pegar_nomes_das_abas_existentes()
        if name_page in nome_das_abas: return
        body = {
          "requests": [{
              "addSheet": {
                  "properties": {
                    "title": f"{name_page}",
                  }
              }
          }],
        }

        request = self.service.spreadsheets().batchUpdate(spreadsheetId=sheets_id, body=body)
        response = request.execute()
        self.console.log(f'Aba adicionado [bold]{name_page}[/]')


    def pegar_nomes_das_abas_existentes(self, sheets_id:str = SHEET_ID):
        sheet_metadata = self.service.spreadsheets().get(spreadsheetId=sheets_id).execute()
        sheets = sheet_metadata.get('sheets','')
        nome_das_abas = [i['properties']['title'] for i in sheets]
        return nome_das_abas
