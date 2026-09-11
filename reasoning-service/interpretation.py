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

class HumidityBand(str, Enum):
    DRY = "dry"
    COMFORTABLE = "comfortable"
    HUMID = "humid"
    VERY_HUMID = "very_humid"

class PrecipitationBand(str, Enum):
    NONE = "none"
    LIGHT = "light"
    RAIN = "rain"
    HEAVY = "heavy"
    SNOW = "snow"

_PRECIPITATION_MAP = {
    "Clear": PrecipitationBand.NONE,
    "Clouds": PrecipitationBand.NONE,
    "Atmosphere": PrecipitationBand.NONE,
    "Drizzle": PrecipitationBand.LIGHT,
    "Rain": PrecipitationBand.RAIN,
    "Thunderstorm": PrecipitationBand.HEAVY,
    "Snow": PrecipitationBand.SNOW,
}

def classify_temperature(temp: float) -> TemperatureBand:

    if temp <= 0:
        return TemperatureBand.FREEZING
    elif temp <= 10:
        return TemperatureBand.COLD
    elif temp <= 18:
        return TemperatureBand.COOL
    elif temp <= 27:
        return TemperatureBand.PLEASANT
    elif temp <= 31:
        return TemperatureBand.WARM
    elif temp <= 34:
        return TemperatureBand.HOT
    else:
        return TemperatureBand.VERY_HOT

def classify_wind(speed: float) -> WindBand:
    if speed <= 3:
        return WindBand.CALM
    elif speed <= 8:
        return WindBand.BREEZY
    elif speed <= 13:
        return WindBand.WINDY
    else:
        return WindBand.VERY_WINDY

def classify_humidity(humidity: int) -> HumidityBand:
    if humidity <= 30:
        return HumidityBand.DRY
    elif humidity <= 60:
        return HumidityBand.COMFORTABLE
    elif humidity <= 75:
        return HumidityBand.HUMID
    else:
        return HumidityBand.VERY_HUMID

def classify_precipitation(condition: str) -> PrecipitationBand:
    if condition in _PRECIPITATION_MAP:
        return _PRECIPITATION_MAP[condition]
    else:
        return PrecipitationBand.NONE
    