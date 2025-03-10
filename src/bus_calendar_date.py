from dataclasses import dataclass
from enum import Enum
from datetime import datetime

class ParseableEnum(Enum):
    @classmethod
    def parse(cls, value):
        for item in cls:
            if item.value == value:
                return item
        raise ValueError(f"Unknwon value '{value}' for class '{cls.__name__}'")

class StrikeType(ParseableEnum):
    N = "N"
        
class DayType(ParseableEnum):
    BUSINESS_DAY = "LA"
    SATURDAY = "SA"
    FESTIVITY = "FE"

# {
# 'date': '10/03/2025 0:00:00',
# 'strike': 'N',
# 'dayType': 'LA'
# }
@dataclass
class BusCalendarDate:
    date : datetime
    strike : str
    day_type : str

    def __init__(self, date: datetime, strike: str, day_type: str):
        self.date = date
        self.strike = StrikeType.parse(strike)
        self.day_type = DayType.parse(day_type)

    def __str__(self):
        return f"BusCalendarDate:{self.date}\strike:({self.strike:.4f}\dat_type:{self.dat_type}"