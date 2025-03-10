from dataclasses import dataclass
from typing import List
from .bus_stop_data_line import BusStopDataLine

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

@dataclass
class BusStopDetail:
    stop_id : int
    name : str
    postal_address : str
    coordinate_x : float
    coordinate_y : float
    pmv : int
    data_lines : List[BusStopDataLine]

    def __str__(self):
        return (f"StopId:{self.stop_id}\tName:{self.name}\tPostalAddress:{self.postal_address}\tCoordinates:({self.coordinate_x:.4f},{self.coordinate_y:.4f})\tPMV:{self.pmv}\nLines:\n" + 
                "\n".join(str(data_line) for data_line in self.data_lines))