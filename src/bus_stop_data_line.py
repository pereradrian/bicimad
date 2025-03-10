from dataclasses import dataclass
from typing import List
from datetime import time

# {
#     "headerB": "CHAMARTIN",
#     "direction": "B",
#     "headerA": "SOL/SEVILLA",
#     "label": "5",
#     "stopTime": "22:58",
#     "minFreq": "9",
#     "startTime": "06:30",
#     "maxFreq": "20",
#     "dayType": "LA",
#     "line": "005"
# },

@dataclass
class BusStopDataLine:
    line_id : int
    label : str
    direction : str
    max_freq : int
    min_freq : int
    header_a : str
    header_b : str
    start_time : time
    stop_time : time
    day_type : str

    def __str__(self):
        return f"LineId:{self.line_id}\tLabel:{self.label}\tDirection:{self.direction}\tMaxFreq:{self.max_freq}\tMinFreq:{self.min_freq}\tHeaderA:{self.header_a}\tHeaderB:{self.header_b}\tStartTime:{self.start_time}\tStopTime:{self.stop_time}\tDayType:{self.day_type}\t"