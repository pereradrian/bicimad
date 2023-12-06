import requests
import json

BASE_URL = "https://openapi.emtmadrid.es/v1/"
# methods of the api
HELLO_METHOD = "hello"
LOGIN_METHOD = "mobilitylabs/user/login/"
LOGOUT_METHOD = "mobilitylabs/user/logout/"

class BiciMAD:
    def __init__(self, authentication_file_path:str = "./keys.json") -> None:
        with open(authentication_file_path) as authentication_file:
                authentication_data =  json.load(authentication_file)
        self.x_client_id = authentication_data['x_client_id']
        self.pass_key = authentication_data['pass_key']

    def get_request(self, url: str, headers:dict = None):
        response = requests.get(url, headers=headers)
        if response.status_code == 200:
            return response.json()
        else:
            return None

    def parse_url(self, method_name):
        return f'{BASE_URL}{method_name}'

    def hello(self):
        url = self.parse_url(HELLO_METHOD)
        return self.get_request(url)
    
    def login(self):
        headers = {
            'X-ClientId' : self.x_client_id,
            'passKey' : self.pass_key,
        }
        url = self.parse_url(LOGIN_METHOD)
        return self.get_request(url, headers=headers)
    
    def logout(self):
        headers = { 
            'accessToken' : self.pass_key,
        }
        url = self.parse_url(LOGOUT_METHOD)
        return self.get_request(url, headers=headers)
    
# https://openapi.emtmadrid.es/v1/mobilitylabs/user/login/