import requests
import json

from .bus_stop import BusStop

#############################################################
## List of all methods and documentation in
## https://apidocs.emtmadrid.es/
##
## Also visit to see a list of all methods
## https://openapi.emtmadrid.es/
##
#############################################################

BASE_URL = "https://openapi.emtmadrid.es/v1/"

# API methods
## Block 0: General
HELLO_METHOD = "hello"

## Block 1: User identity
LOGIN_METHOD = "mobilitylabs/user/login/"
LOGOUT_METHOD = "mobilitylabs/user/logout/"
WHOAMI_METHOD = "mobilitylabs/user/whoami/"

## Block 2: Data model
#### OBS: None of them seems to be working
CATEGORIES_METHOD = "mobilitylabs/discover/categories/"
LINKTYPES_METHOD = "mobilitylabs/discover/linktypes/"
DATATYPES_METHOD = "mobilitylabs/discover/datatypes/"
FIELDFORMATS_METHOD = "mobilitylabs/discover/fieldformats/"
RESTACTIONS_METHOD = "mobilitylabs/discover/restactions/"
RESTTYPES_METHOD = "mobilitylabs/discover/resttypes/"
SHARINGTYPES_METHOD = "mobilitylabs/discover/sharingtypes/"

## Block 3: Transport BUSEMTMAD
# TODO: Review
TRANSPORT_BUSEMTMAD_STOPS_DETAIL = "transport/busemtmad/stops/{stopId}/detail/"
TRANSPORT_BUSEMTMAD_STOPS_AROUNDSTOP = "transport/busemtmad/stops/arroundstop/{stopId}/{radius}/"
TRANSPORT_BUSEMTMAD_STOPS_AROUNDXY = "transport/busemtmad/stops/arroundxy/{longitude}/{latitude}/{radius}/"
TRANSPORT_BUSEMTMAD_STOPS_ARRIVES = "transport/busemtmad/stops/{stopId}/arrives/{lineArrive}/"
TRANSPORT_BUSEMTMAD_CALENDAR = "transport/busemtmad/calendar/{startdate}/{enddate}/"
TRANSPORT_BUSEMTMAD_LINES_INCIDENTS = "transport/busemtmad/lines/incidents/{lineid}/"
TRANSPORT_BUSEMTMAD_LINES_INFOLINE_DETAIL = "transport/busemtmad/lines/{lineId}/info/{dateRef}/"
TRANSPORT_BUSEMTMAD_LINES_INFOLINE_GENERAL = "transport/busemtmad/lines/info/{dateRef}/"
TRANSPORT_BUSEMTMAD_STOPS_LIST = "transport/busemtmad/stops/list/"
TRANSPORT_BUSEMTMAD_LINES_STOPS = "transport/busemtmad/lines/{lineId}/stops/{direction}/"
# OBS: rMEthod repeated with another name as "list stops" and "infostops(general)"
#TRANSPORT_BUSEMTMAD_LINES_STOPS = "transport/busemtmad/stops/list/"
TRANSPORT_BUSEMTMAD_LINES_OPERATION_GROUPS = "transport/busemtmad/lines/groups/"
TRANSPORT_BUSEMTMAD_LINES_ROUTE = "transport/busemtmad/lines/{labelId}/route/"
TRANSPORT_BUSEMTMAD_STOPS_AROUNDSTREET = "transport/busemtmad/stops/arroundstreet/{namePlace}/{number_or_zero_street_number}/{radius}/"
TRANSPORT_BUSEMTMAD_LINES_TIMETABLE = "transport/busemtmad/lines/{lineId}/timetable/"
TRANSPORT_BUSEMTMAD_LINES_TRIPS = "transport/busemtmad/lines/{lineId}/trips/{dateRef}/"
TRANSPORT_BUSEMTMAD_TRAVELPLAN = "transport/busemtmad/travelplan/"


# API response keys
## General
ACCESS_TOKEN_KEY = "accessToken"
DATA_KEY = "data"
CODE_KEY = "code"

## Bus stop
NODE_KEY = "node"
GEOMETRY_KEY = "geometry"
COORDINATES_KEY = "coordinates"
WIFI_KEY = "wifi"
LINES_KEY = "lines"
NAME_KEY = "name"

## API response codes
OK_CODE = "00"
OK1_CODE = "01"

class BiciMAD:
    def __init__(self, authentication_file_path:str = "./keys.json", debug=True) -> None:
        with open(authentication_file_path) as authentication_file:
                authentication_data =  json.load(authentication_file)
        self.x_client_id = authentication_data['x_client_id']
        self.pass_key = authentication_data['pass_key']
        self.debug = debug
        self.accessToken = None

    def __get_request__(self, url: str, headers:dict = {}, debug=False):
        if self.accessToken:
            headers[ACCESS_TOKEN_KEY] = self.accessToken
        if debug:
            print(headers)
            print(url)
        response = requests.get(url, headers=headers)
        if response.status_code == 200:
            return response.json()
        else:
            print(response)
            return None
        
    def __post_request__(self, url: str, headers:dict = None, debug=False):
        # If access token is available, add to headers
        if self.accessToken:
            headers[ACCESS_TOKEN_KEY] = self.accessToken

        if debug:
            print(headers)
            print(url)
        response = requests.post(url, headers=headers)
        if response.status_code == 200:
            return response.json()
        else:
            if debug:
                print('Failed:', response.status_code, response.text)
            return None

    def __format_url__(self, method_name):
        return f'{BASE_URL}{method_name}'

    def hello(self):
        url = self.__format_url__(HELLO_METHOD)
        return self.__get_request__(url)
    
    def whoami(self):
        url = self.__format_url__(WHOAMI_METHOD)
        return self.__get_request__(url)
    
    def login(self):
        headers = {
            'X-ClientId' : self.x_client_id,
            'passKey' : self.pass_key,
        }
        url = self.__format_url__(LOGIN_METHOD)
        response = self.__get_request__(url, headers=headers)
        
        if validate_response(response):
            data = extract_data(response)
            data = data[0]
            if data:
                if ACCESS_TOKEN_KEY in data:
                    self.accessToken = data[ACCESS_TOKEN_KEY]
                else:
                    raise ValueError(f"Key '{ACCESS_TOKEN_KEY}' missing in data: '{response}'")
            else:
                raise ValueError(f"Received data is None: '{response}'")
        else:
            raise ValueError(f"Response is not valid: '{response}'")
    
    def logout(self):
        url = self.__format_url__(LOGOUT_METHOD)
        return self.__get_request__(url)
    
    def emt_list_stops(self, debug=False):
        url = self.__format_url__(TRANSPORT_BUSEMTMAD_STOPS_LIST_METHOD)
        response = self.__post_request__(url, headers={}, debug=debug)
        if validate_response(response):
            data = extract_data(response)
            return [convert_to_bus_stop(entry) for entry in data]
            
        return []

## Conversion utilities
def convert_to_bus_stop(entry):
    # {
    #     "node": "1",
    #     "geometry": {
    #         "type": "Point",
    #         "coordinates": [
    #             -3.782776719960321,
    #             40.47005438829035
    #         ]
    #     },
    #     "wifi": "0",
    #     "lines": [
    #         "161/1/1"
    #     ],
    #     "name": "Avenida Valdemarín-Blanca de Castilla"
    # },
    node = int(entry[NODE_KEY])
    geometry = entry[GEOMETRY_KEY]
    coordinate_x = float(geometry[COORDINATES_KEY][0])
    coordinate_y = float(geometry[COORDINATES_KEY][1])
    wifi = entry[WIFI_KEY] != '0'
    raw_lines = entry[LINES_KEY]
    # parse lines
    if raw_lines:
        lines = [raw_line.split('/') for raw_line in raw_lines]
    else:
        lines = []
    name = entry[NAME_KEY]
    
    return BusStop(node=node,
                   coordinate_x=coordinate_x,
                   coordinate_y=coordinate_y,
                   wifi=wifi,
                   lines=lines,
                   name=name)

## Utility methods
def validate_response(response):
    return response and CODE_KEY in response and (response[CODE_KEY] == OK_CODE or response[CODE_KEY] == OK1_CODE)

def extract_data(response, expected_size=None):
    if response and DATA_KEY in response:
        data = response[DATA_KEY]
        if expected_size:
            assert len(data) == expected_size, f"Length of data is unexpected {len(data)}"
        return data
    return None