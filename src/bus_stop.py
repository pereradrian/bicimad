from dataclasses import dataclass
from typing import List
from .bus_stop_detail import BusStopDetail

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
class BusStop:
    stop_id : int
    coordinate_x : float
    coordinate_y : float
    wifi : bool
    line_ids : List[str]
    name : str
    bus_stop_detail : BusStopDetail = None

    def __str__(self):
        return f"Node:{self.stop_id}\tcoordinates:({self.coordinate_x:.4f},{self.coordinate_y:.4f})\twifi:{self.wifi}\tlines:{self.line_ids}\tname:{self.name}\nbus_stop_detail:{self.bus_stop_detail}"