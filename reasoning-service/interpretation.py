from enum import Enum

class TemperatureBand(str, Enum):
    FREEZING = "freezing"
    COLD = "cold"
    COOL = "cool"
    PLEASANT = "pleasant"
    WARM = "warm"
    HOT = "hot"
    VERY_HOT = "very_hot"

class WindBand(str, Enum):
    CALM = "calm"
    BREEZY = "breezy"
    WINDY = "windy"
    VERY_WINDY = "very_windy"

def classify_temperature(temp: float) -> TemperatureBand:

    if temp <= 0:
        return TemperatureBand.FREEZING
    elif 0 < temp <= 10:
        return TemperatureBand.COLD
    elif 10 < temp <= 18:
        return TemperatureBand.COOL
    elif 18 < temp <= 27:
        return TemperatureBand.PLEASANT
    elif 27 < temp <= 31:
        return TemperatureBand.WARM
    elif 31 < temp <= 34:
        return TemperatureBand.HOT
    else:
        return TemperatureBand.VERY_HOT

def classify_wind(speed: float) -> WindBand:
    if speed <= 3:
        return WindBand.CALM
    elif speed <= 9:
        return WindBand.BREEZY
    elif speed <= 13:
        return WindBand.WINDY
    else:
        return WindBand.VERY_WINDY