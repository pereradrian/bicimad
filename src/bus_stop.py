from dataclasses import dataclass
from typing import List

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
    node : int
    coordinate_x : float
    coordinate_y : float
    wifi : bool
    lines : List[str]
    name : str

    def __str__(self):
        return f"Node:{self.node}\tcoordinates:({self.coordinate_x:.4f},{self.coordinate_y:.4f})\twifi:{self.wifi}\tlines:{self.lines}\tname:{self.name}"