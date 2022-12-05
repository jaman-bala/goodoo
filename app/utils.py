import requests

from requests.auth import HTTPBasicAuth

def get_token():
    URL = "http://10.12.20.65:9099/api/licences"
    response = requests.get(URL, auth=HTTPBasicAuth("admin", "admin"))
    if response.status_code == 200:
        data = response.json()
        message = {"status":True, "message":"Ok", "data":data}
    else:
        message = {"status":False, "message":"Recconnect, please check access connection", "data":None}
    return message

