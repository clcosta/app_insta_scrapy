import json
import os

existe = False

BASE_DIR = os.path.dirname(os.path.dirname(__file__))
auth_txt_path = os.path.join(BASE_DIR,'instascraping','auth.txt')

if os.path.exists(auth_txt_path):
    existe = True
    with open(auth_txt_path, 'r') as file:
        string_dict = file.read()
        json_data = string_dict.replace("'", "\"")
        data = json.loads(json_data)
""" Instagram User infos """

if not existe:
    USERNAME = 'claudiopython2'
    PASSWORD = 'pythonbot123123'  
    SESSION_ID = '49723805832%3Ar8LptxxkRBu8E2%3A20'

    """ Google Sheets infos """

    SHEET_ID = '1dGSu6PVtC2eY5hXGFzoh5vl_lYt70yIpPBlP2-Mywpk'
    CONNECTION_RANGE = 'Connection!A1' ## Página oculta
else:
    USERNAME = data['USERNAME']
    PASSWORD = data['PASSWORD']
    SESSION_ID = data['SESSION_ID']

    ### Sheets infos

    SHEET_ID = data['SHEET_ID']
    CONNECTION_RANGE = data['CONNECTION_RANGE']
