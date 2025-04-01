import requests
import json
from datetime import datetime

from .bus_stop import BusStop
from .bus_stop_detail import BusStopDetail
from .bus_stop_data_line import BusStopDataLine
from .bus_calendar_date import BusCalendarDate
from .bus_infoline_general import InfoLineGeneral

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
TRANSPORT_BUSEMTMAD_CALENDAR = "transport/busemtmad/calendar/{startDate}/{endDate}/"
TRANSPORT_BUSEMTMAD_LINES_INCIDENTS = "transport/busemtmad/lines/incidents/{lineId}/"
TRANSPORT_BUSEMTMAD_LINES_INFOLINE_DETAIL = "transport/busemtmad/lines/{lineId}/info/{dateRef}/"
TRANSPORT_BUSEMTMAD_LINES_INFOLINE_GENERAL = "transport/busemtmad/lines/info/{dateRef}/"
TRANSPORT_BUSEMTMAD_STOPS_LIST = "transport/busemtmad/stops/list/"
TRANSPORT_BUSEMTMAD_LINES_STOPS = "transport/busemtmad/lines/{lineId}/stops/{direction}/"
# OBS: MEthod repeated with another name as "list stops" and "infostops(general)"
#TRANSPORT_BUSEMTMAD_LINES_STOPS = "transport/busemtmad/stops/list/"
TRANSPORT_BUSEMTMAD_LINES_OPERATION_GROUPS = "transport/busemtmad/lines/groups/"
TRANSPORT_BUSEMTMAD_LINES_ROUTE = "transport/busemtmad/lines/{labelId}/route/"
TRANSPORT_BUSEMTMAD_STOPS_AROUNDSTREET = "transport/busemtmad/stops/arroundstreet/{namePlace}/{number_or_zero_street_number}/{radius}/"
TRANSPORT_BUSEMTMAD_LINES_TIMETABLE = "transport/busemtmad/lines/{lineId}/timetable/"
TRANSPORT_BUSEMTMAD_LINES_TRIPS = "transport/busemtmad/lines/{lineId}/trips/{dateRef}/"
TRANSPORT_BUSEMTMAD_TRAVELPLAN = "transport/busemtmad/travelplan/"

## BICIMAD
TRANSPORT_BICIMAD_BIKES_GO_AVAILABLES = "transport/bicimadgo/bikes/availability/"
TRANSPORT_BICIMAD_BIKES_GO_AVAILABLES_BIKE_ID = "transport/bicimadgo/bikes/availability/{bikeId}/"
TRANSPORT_BICIMAD_BIKES_GO_AVAILABLES_AROUND_XY = "transport/bicimadgo/bikes/availability/arroundxy/{longitude}/{latitude}/{radius}/"
TRANSPORT_BICIMAD_LIST_BICIMAD_STATIONS = "transport/bicimad/stations/{idStation}/"


ALL_TRANSPORT_METHODS = {
    TRANSPORT_BUSEMTMAD_STOPS_DETAIL : lambda bicimad: bicimad.default_method,
    TRANSPORT_BUSEMTMAD_STOPS_AROUNDSTOP : lambda bicimad: bicimad.default_method,
    TRANSPORT_BUSEMTMAD_STOPS_AROUNDXY : lambda bicimad: bicimad.default_method,
    TRANSPORT_BUSEMTMAD_STOPS_ARRIVES : lambda bicimad: bicimad.default_method,
    TRANSPORT_BUSEMTMAD_CALENDAR : lambda bicimad: bicimad.default_method,
    TRANSPORT_BUSEMTMAD_LINES_INCIDENTS : lambda bicimad: bicimad.default_method,
    TRANSPORT_BUSEMTMAD_LINES_INFOLINE_DETAIL : lambda bicimad: bicimad.default_method,
    TRANSPORT_BUSEMTMAD_LINES_INFOLINE_GENERAL : lambda bicimad: bicimad.default_method,
    TRANSPORT_BUSEMTMAD_STOPS_LIST : lambda bicimad: bicimad.transport_busemtmad_stops_detail,
    TRANSPORT_BUSEMTMAD_LINES_STOPS : lambda bicimad: bicimad.default_method,
    TRANSPORT_BUSEMTMAD_LINES_OPERATION_GROUPS : lambda bicimad: bicimad.default_method,
    TRANSPORT_BUSEMTMAD_LINES_ROUTE : lambda bicimad: bicimad.default_method,
    TRANSPORT_BUSEMTMAD_STOPS_AROUNDSTREET : lambda bicimad: bicimad.default_method,
    TRANSPORT_BUSEMTMAD_LINES_TIMETABLE : lambda bicimad: bicimad.default_method,
    TRANSPORT_BUSEMTMAD_LINES_TRIPS : lambda bicimad: bicimad.default_method,
    TRANSPORT_BUSEMTMAD_TRAVELPLAN : lambda bicimad: bicimad.default_method,

    TRANSPORT_BICIMAD_BIKES_GO_AVAILABLES : lambda bicimad: bicimad.default_method, 
}


# API response keys
## General
ACCESS_TOKEN_KEY = "accessToken"
DATA_KEY = "data"
CODE_KEY = "code"


## Bus stop
STOPS_KEY = "stops"
STOP_NODE_KEY = "node"
STOP_GEOMETRY_KEY = "geometry"
STOP_COORDINATES_KEY = "coordinates"
STOP_WIFI_KEY = "wifi"
STOP_LINES_KEY = "lines"
STOP_NAME_KEY = "name"

## Bus stop detail
STOP_DETAILS_ID_KEY = "stop"
STOP_DETAILS_NAME_KEY = "name"
STOP_DETAILS_POSTAL_ADDRESS_KEY = "postalAddress"
STOP_DETAILS_PMV_KEY = "pmv"
STOP_DETAILS_DATALINE_KEY = "dataLine"

## Data line
DATALINE_LINE_KEY = "line"
DATALINE_LABEL_KEY = "label"
DATALINE_DIRECTION_KEY = "direction"
DATALINE_MAXFREQ_KEY = "maxFreq"
DATALINE_MINFREQ_KEY = "minFreq"
DATALINE_HEADER_A_KEY = "headerA"
DATALINE_HEADER_B_KEY = "headerB"
DATALINE_STARTTIME_KEY = "startTime"
DATALINE_STOPTIME_KEY = "stopTime"
DATALINE_DAYTYPE_KEY = "dayType"

## Calendar
CALENDAR_DATE_KEY = "date"
CALENDAR_STRIKE_KEY = "strike"
CALENDAR_DAY_TYPE_KEY = "dayType"

## Incidents
INCIDENTS_ITEM_KEY = "item"

INFOLINE_LINE_ID_KEY = "line"
INFOLINE_LABEL_KEY = "label"
INFOLINE_NAME_A_KEY = "nameA"
INFOLINE_NAME_B_KEY = "nameB"
INFOLINE_GROUP_KEY = "group"

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
            prompt(headers)
            prompt(url)
        response = requests.get(url, headers=headers)
        if response.status_code == 200:
            return response.json()
        else:
            prompt(response)
            return None

    def __post_request__(self, url: str, headers:dict = None, data=None, json=None, debug=False):
        # If access token is available, add to headers
        if self.accessToken:
            headers[ACCESS_TOKEN_KEY] = self.accessToken

        if debug:
            prompt(headers)
            prompt(url)
        response = requests.post(url, headers=headers, data=data, json=json)
        if response.status_code == 200:
            return response.json()
        else:
            if debug:
                prompt(f'Failed: {response.status_code} {response.text}')
            return None

    def __format_url__(self, method_name):
        return f'{BASE_URL}{method_name}'

    def default_method(self):
        prompt("Not implemented.")
        pass

    ## Block 0: General
    def hello(self):
        url = self.__format_url__(HELLO_METHOD)
        return self.__get_request__(url)

    ## Block 1: User identity
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

    ## Block 3: Transport BUSEMTMAD
    # TRANSPORT_BUSEMTMAD_STOPS_DETAIL : lambda bicimad: bicimad.default_method(),
    def transport_busemtmad_stops_detail(self, bus_stop : BusStop, debug=False):
        urlFragment = TRANSPORT_BUSEMTMAD_STOPS_DETAIL.format(stopId=bus_stop.stop_id)
        url = self.__format_url__(urlFragment)
        response = self.__get_request__(url, headers={}, debug=debug)
        if validate_response(response):
            data = extract_data(response)
            assert len(data) == 1
            data = data[0]
            stops = data[STOPS_KEY]
            assert len(stops) == 1
            stop = stops[0]
            return convert_to_bus_stop_detail(stop)
        return []

    # TRANSPORT_BUSEMTMAD_STOPS_AROUNDSTOP : lambda bicimad: bicimad.default_method(),
    def transport_busemtmad_stops_aroundstop(self, bus_stop : BusStop, radius:int, debug=False, include_details=True, limit=None):
        urlFragment = TRANSPORT_BUSEMTMAD_STOPS_AROUNDSTOP.format(stopId=bus_stop.stop_id, radius=radius)
        url = self.__format_url__(urlFragment)
        response = self.__get_request__(url, headers={}, debug=debug)
        if validate_response(response):
            data = extract_data(response)
            assert len(data) == 1
            data = data[0]
            # Validate format
            assert len(data.keys()) == 1 and STOPS_KEY in data
            data = data[STOPS_KEY]
            bus_stops = [convert_to_bus_stop_detail(entry) for entry in data]
            if limit:
                bus_stops = bus_stops[:limit]
            if include_details:
                for bus_stop in bus_stops:
                    bus_stop_detail = self.transport_busemtmad_stops_detail(bus_stop=bus_stop, debug=debug)
                    bus_stop.bus_stop_detail = bus_stop_detail
            return bus_stops
        return []
        
    # TRANSPORT_BUSEMTMAD_STOPS_AROUNDXY : lambda bicimad: bicimad.default_method(),
    def transport_busemtmad_stops_aroundxy(self, longitude: int, latitude:float, radius:float, debug=False, include_details=True, limit=None):
        urlFragment = TRANSPORT_BUSEMTMAD_STOPS_AROUNDXY.format(longitude=longitude, latitude=latitude, radius=radius)
        url = self.__format_url__(urlFragment)
        response = self.__get_request__(url, headers={}, debug=debug)
        if validate_response(response):
            data = extract_data(response)
            assert len(data) == 1
            data = data[0]
            # Validate format
            assert len(data.keys()) == 1 and STOPS_KEY in data
            data = data[STOPS_KEY]
            bus_stops = [convert_to_bus_stop_detail(entry) for entry in data]
            if limit:
                bus_stops = bus_stops[:limit]
            if include_details:
                for bus_stop in bus_stops:
                    bus_stop_detail = self.transport_busemtmad_stops_detail(bus_stop=bus_stop, debug=debug)
                    bus_stop.bus_stop_detail = bus_stop_detail
            return bus_stops
        return []

    # TRANSPORT_BUSEMTMAD_STOPS_ARRIVES : lambda bicimad: bicimad.default_method(),
    # TODO: Server fails!
    def transport_busemtmad_stops_arrives(self, bus_stop : BusStop, line : BusStopDataLine, debug=False):
        urlFragment = TRANSPORT_BUSEMTMAD_STOPS_ARRIVES.format(stopId=bus_stop.stop_id, lineArrive=line.line_id)
        url = self.__format_url__(urlFragment)
        payload = {
            "cultureInfo":"EN", #Could be EN for english or ES for spanish
            "Text_StopRequired_YN":"Y", #Y(es) for getting name stop or N(ot)
            "Text_EstimationsRequired_YN":"Y", #Y(es) for data estimations to arrival Bus or N(ot)
            "Text_IncidencesRequired_YN":"Y", #Y(es) for getting incidents related to lines in this stop s or N(ot)
            "DateTime_Referenced_Incidencies_YYYYMMDD":"20250307", #year-month-day to reference of incidents
        }
        {"cultureInfo":"EN", "Text_StopRequired_YN":"Y", "Text_EstimationsRequired_YN":"Y", "Text_IncidencesRequired_YN":"Y", "DateTime_Referenced_Incidencies_YYYYMMDD":"20250307"}
        response = self.__post_request__(url, headers={}, data=payload, debug=debug)
        if validate_response(response):
            return extract_data(response)
        return []

    # TRANSPORT_BUSEMTMAD_CALENDAR : lambda bicimad: bicimad.default_method(),
    def transport_busemtmad_calendar(self, start_date : str, end_date : str, debug=False):
        urlFragment = TRANSPORT_BUSEMTMAD_CALENDAR.format(startDate=start_date, endDate=end_date)
        url = self.__format_url__(urlFragment)
        response = self.__get_request__(url, headers={}, debug=debug)
        if validate_response(response):
            date_entries = extract_data(response)
            return [convert_to_calendar_date(date_entry) for date_entry in date_entries]
        else:
            raise ValueError(f"ERROR: {response}")


    # TRANSPORT_BUSEMTMAD_LINES_INCIDENTS : lambda bicimad: bicimad.default_method(),
    def transport_busemtmad_lines_incidents(self, line_id : int, debug=False):
        urlFragment = TRANSPORT_BUSEMTMAD_LINES_INCIDENTS.format(lineId=line_id)
        url = self.__format_url__(urlFragment)
        response = self.__get_request__(url, headers={}, debug=debug)
        if validate_response(response):
            data = extract_data(response)
            return data[0][INCIDENTS_ITEM_KEY]
        else:
            raise ValueError(f"ERROR: {response}")

    # TRANSPORT_BUSEMTMAD_LINES_INFOLINE_DETAIL : lambda bicimad: bicimad.default_method(),
    ## TODO: Raises an error
    def transport_busemtmad_lines_infoline_detail(self, line_id : int, reference_date : str, debug=False):
        urlFragment = TRANSPORT_BUSEMTMAD_LINES_INFOLINE_DETAIL.format(lineId=line_id, dateRef=reference_date)
        url = self.__format_url__(urlFragment)
        response = self.__get_request__(url, headers={}, debug=debug)
        if validate_response(response):
            return extract_data(response)
        else:
            raise ValueError(f"ERROR: {response}")

    # TRANSPORT_BUSEMTMAD_LINES_INFOLINE_GENERAL : lambda bicimad: bicimad.default_method(),
    def transport_busemtmad_lines_infoline_general(self, reference_date : str, debug=False):
        urlFragment = TRANSPORT_BUSEMTMAD_LINES_INFOLINE_GENERAL.format(dateRef=reference_date)
        url = self.__format_url__(urlFragment)
        response = self.__get_request__(url, headers={}, debug=debug)
        if validate_response(response):
            infoline_list = extract_data(response)
            return [convert_to_infoline_general(infoline) for infoline in infoline_list]
        else:
            raise ValueError(f"ERROR: {response}")

    # TRANSPORT_BUSEMTMAD_STOPS_LIST : lambda bicimad: bicimad.transport_busemtmad_stops_detail(),
    def transport_busemtmad_stops_list(self, include_details = False, limit=None, debug=False):
        url = self.__format_url__(TRANSPORT_BUSEMTMAD_STOPS_LIST)
        response = self.__post_request__(url, headers={}, debug=debug)
        if validate_response(response):
            data = extract_data(response)
            bus_stops = [convert_to_bus_stop(entry) for entry in data]
            if limit:
                bus_stops = bus_stops[:limit]
            if include_details:
                for bus_stop in bus_stops:
                    bus_stop_detail = self.transport_busemtmad_stops_detail(bus_stop=bus_stop, debug=debug)
                    bus_stop.bus_stop_detail = bus_stop_detail

            return bus_stops

        return []

    # TRANSPORT_BUSEMTMAD_LINES_STOPS : lambda bicimad: bicimad.default_method(),
    def transport_busemtmad_stops_list(self, line_id : int, direction :int, debug=False):
        url = self.__format_url__(TRANSPORT_BUSEMTMAD_LINES_STOPS.format(lineId=line_id, direction=direction))
        response = self.__get_request__(url, headers={}, debug=debug)
        if validate_response(response):
            data = extract_data(response)
            assert len(data) == 1
            data = data[0]
            return [convert_to_bus_stop(stop) for stop in data[STOPS_KEY]]
        return []

    # TRANSPORT_BUSEMTMAD_LINES_OPERATION_GROUPS : lambda bicimad: bicimad.default_method(),
    def transport_busemtmad_lines_operation_groups(self, debug=False):
        url = self.__format_url__(TRANSPORT_BUSEMTMAD_LINES_OPERATION_GROUPS)
        response = self.__get_request__(url, headers={}, debug=debug)
        if validate_response(response):
            return response
        else:
            return []

    # TRANSPORT_BUSEMTMAD_LINES_ROUTE : lambda bicimad: bicimad.default_method(),
    def transport_busemtmad_lines_route(self, line_id : str, debug=False):
        url = self.__format_url__(TRANSPORT_BUSEMTMAD_LINES_ROUTE.format(labelId=line_id))
        response = self.__get_request__(url, headers={}, debug=debug)
        if validate_response(response):
            return response
        else:
            return None

    # TRANSPORT_BUSEMTMAD_STOPS_AROUNDSTREET : lambda bicimad: bicimad.default_method(),
    def transport_busemtmad_stops_around_street(self, debug=False):
        raise ValueError("Not implemented")

    # TRANSPORT_BUSEMTMAD_LINES_TIMETABLE : lambda bicimad: bicimad.default_method(),
    def transport_busemtmad_lines_timetable(self, line_id : str, debug=False):
        url = self.__format_url__(TRANSPORT_BUSEMTMAD_LINES_TIMETABLE.format(lineId=line_id))
        response = self.__get_request__(url, headers={}, debug=debug)
        if validate_response(response):
            return response
        else:
            return None

    # TRANSPORT_BUSEMTMAD_LINES_TRIPS : lambda bicimad: bicimad.default_method(),
    def transport_busemtmad_lines_trips(self, line_id : int, reference_date : str, debug=False):
        url = self.__format_url__(TRANSPORT_BUSEMTMAD_LINES_TRIPS.format(lineId=line_id, dateRef=reference_date))
        response = self.__get_request__(url, headers={}, debug=debug)
        if validate_response(response):
            data = extract_data(response)
            return data
        else:
            return None

    # TRANSPORT_BUSEMTMAD_TRAVELPLAN : lambda bicimad: bicimad.default_method(),
    def transport_busemtmad_travel_plan(self, debug=False):
        raise ValueError("Not implemented")

    ##########################################################################
    ##########################################################################
    ##########################################################################
    ### BICIMAD
    ##########################################################################
    ##########################################################################
    ##########################################################################
    # TRANSPORT_BICIMAD_BIKES_GO_AVAILABLES : lambda bicimad: bicimad.default_method(),
    def transport_bicimad_bikes_go_availables(self, bike_id=None, longitude=None, latitude=None, radius=None, debug=False):
        # /arroundxy/longitude/latitude/radius/ bikes arround Point
        if bike_id is not None:
            url = self.__format_url__(TRANSPORT_BICIMAD_BIKES_GO_AVAILABLES_BIKE_ID.format(bikeId=bike_id))
        elif longitude is not None:
            url = self.__format_url__(TRANSPORT_BICIMAD_BIKES_GO_AVAILABLES_AROUND_XY.format(longitude=longitude, latitude=latitude, radius=radius))
        else:
            url = self.__format_url__(TRANSPORT_BICIMAD_BIKES_GO_AVAILABLES)
        response = self.__get_request__(url, headers={}, debug=debug)
        if validate_response(response):
            data = extract_data(response)
            return data
        else:
            return None
    
    # TRANSPORT_BICIMAD_LIST_BICIMAD_STATIONS
    def transport_bicimad_list_bicimad_stations(self, station_id : int, debug=False):
        url = self.__format_url__(TRANSPORT_BICIMAD_LIST_BICIMAD_STATIONS.format(idStation=station_id))
        response = self.__get_request__(url, headers={}, debug=debug)
        if validate_response(response):
            data = extract_data(response)
            return data
        else:
            return None

def convert_to_infoline_general(infoline):
    line_id = infoline[INFOLINE_LINE_ID_KEY]
    label = infoline[INFOLINE_LABEL_KEY]
    name_A = infoline[INFOLINE_NAME_A_KEY]
    name_B = infoline[INFOLINE_NAME_B_KEY]
    group = infoline[INFOLINE_GROUP_KEY]
    return InfoLineGeneral(line_id=line_id, label=label, name_A=name_A, name_B=name_B, group=group)


## Conversion utilities
def extract_coordinates(entry):
    geometry = entry[STOP_GEOMETRY_KEY]
    coordinate_x = float(geometry[STOP_COORDINATES_KEY][0])
    coordinate_y = float(geometry[STOP_COORDINATES_KEY][1])
    return coordinate_x, coordinate_y

def extract_dataline(entry):
    line_id = int(entry[DATALINE_LINE_KEY])
    label = entry[DATALINE_LABEL_KEY]
    direction = entry[DATALINE_DIRECTION_KEY]
    max_freq = int(entry[DATALINE_MAXFREQ_KEY])
    min_freq = int(entry[DATALINE_MINFREQ_KEY])
    header_a = entry[DATALINE_HEADER_A_KEY]
    header_b = entry[DATALINE_HEADER_B_KEY]
    start_time = datetime.strptime(entry[DATALINE_STARTTIME_KEY], "%H:%M").time()
    stop_time = datetime.strptime(entry[DATALINE_STOPTIME_KEY], "%H:%M").time()
    day_type = entry[DATALINE_DAYTYPE_KEY]
    return BusStopDataLine(line_id = line_id,
            label = label,
            direction = direction,
            max_freq = max_freq,
            min_freq = min_freq,
            header_a = header_a,
            header_b = header_b,
            start_time = start_time,
            stop_time = stop_time,
            day_type = day_type)

def convert_to_bus_stop_detail(stop):
    stop_id = int(stop[STOP_DETAILS_ID_KEY])
    name = stop[STOP_DETAILS_NAME_KEY]
    postal_address = stop[STOP_DETAILS_POSTAL_ADDRESS_KEY]
    coordinate_x, coordinate_y = extract_coordinates(stop)
    pmv = stop[STOP_DETAILS_PMV_KEY]
    data_lines = [extract_dataline(entry) for entry in stop[STOP_DETAILS_DATALINE_KEY]]
#
    return BusStopDetail(stop_id=stop_id, name=name, postal_address=postal_address, coordinate_x=coordinate_x, coordinate_y=coordinate_y, pmv=pmv, data_lines=data_lines)

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
    if STOP_NODE_KEY in entry:
        stop_id = int(entry[STOP_NODE_KEY])
    else:
        stop_id = int(entry[STOP_DETAILS_ID_KEY])
    coordinate_x, coordinate_y = extract_coordinates(entry)
    if STOP_WIFI_KEY in entry:
        wifi = entry[STOP_WIFI_KEY] != '0'
    else:
        wifi = False
    if STOP_LINES_KEY in entry:
        raw_line_ids = entry[STOP_LINES_KEY]
        # parse lines
        if raw_line_ids:
            line_ids = [raw_line_id.split('/') for raw_line_id in raw_line_ids]
        else:
            line_ids = []
    else:
            line_ids = entry[STOP_DETAILS_DATALINE_KEY]
    name = entry[STOP_NAME_KEY]

    return BusStop(stop_id=stop_id,
                   coordinate_x=coordinate_x,
                   coordinate_y=coordinate_y,
                   wifi=wifi,
                   line_ids=line_ids,
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

def prompt(string):
    print(string)

def convert_to_calendar_date(date_entry : dict):
    date = datetime.strptime(date_entry[CALENDAR_DATE_KEY], "%d/%m/%Y %H:%M:%S")
    strike = date_entry[CALENDAR_STRIKE_KEY]
    day_type = date_entry[CALENDAR_DAY_TYPE_KEY]
    return BusCalendarDate(date=date, strike=strike, day_type=day_type)