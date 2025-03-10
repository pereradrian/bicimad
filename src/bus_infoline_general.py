from dataclasses import dataclass
from typing import List
from .bus_stop_detail import BusStopDetail

# {
#     "line": "361",
#     "label": "001",
#     "nameA": "ESTACION DE ATOCHA",
#     "nameB": "MONCLOA",
#     "group": "110",
# },

@dataclass
class InfoLineGeneral:
    line_id : int
    label : str
    name_A : str
    name_B : str
    group : str

    def __str__(self):
        return f"Line ID:{self.line_id}\tlabel:{self.label}\tnameA:{self.name_A}\tnameB:{self.name_B}\tgroup:{self.group}"