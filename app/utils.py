import requests

from requests.auth import HTTPBasicAuth

def get_token():
    URL = "http://77.220.204.134:54321/api/licences"
    response = requests.get(URL, auth=HTTPBasicAuth("admin", "admin"))
    if response.status_code == 200:
        data = response.json()
        message = {"status":True, "message":"Ok", "data":data}
    else:
        message = {"status":False, "message":"Recconnect, please check access connection", "data":None}
    return message

