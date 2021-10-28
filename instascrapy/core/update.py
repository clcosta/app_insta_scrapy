import json
import os

from ..instascraping.auth import (
    CONNECTION_RANGE,
    PASSWORD,
    SESSION_ID,
    SHEET_ID,
    USERNAME,
)

class Autenticacao:

    __BASE_DIR = os.path.dirname(os.path.dirname(__file__))
    connection_range = CONNECTION_RANGE
    password = PASSWORD
    session_id = SESSION_ID
    sheet_id = SHEET_ID
    username = USERNAME
    data = None

    def __init__(self):
        data = self.__verificar_arquivo()
        if data:
            self.data = data
            self.username = data["USERNAME"]
            self.password = data["PASSWORD"]
            self.session_id = data["SESSION_ID"]
            self.sheet_id = data["SHEET_ID"]
            self.connection_range = data["CONNECTION_RANGE"]
        # insta_scrapy\core\instascraping\auth.txt

    def __verificar_arquivo(self):
        self.__auth_txt_path = os.path.join(
            self.__BASE_DIR,"instascraping", "auth.txt"
        )
        if os.path.exists(self.__auth_txt_path):
            existe = True
            with open(self.__auth_txt_path, "r") as file:
                json_data = file.readlines()[0].replace("'", '"')
                data = json.loads(json_data)

        else:
            existe = False

        if existe:
            return data
        else:
            return None

    def update_auth(self, data: dict):
        with open(self.__auth_txt_path, "w") as file:
            file.write(str(data))
            self.data = data
            self.username = data["USERNAME"]
            self.password = data["PASSWORD"]
            self.session_id = data["SESSION_ID"]
            self.sheet_id = data["SHEET_ID"]
            self.connection_range = data["CONNECTION_RANGE"]
