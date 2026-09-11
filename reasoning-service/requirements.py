from dataclasses import dataclass, field
from interpretation import TemperatureBand, WindBand, HumidityBand, PrecipitationBand

@dataclass
class ClothingRequirements:
    insulation_level: int
    waterproof_needed: bool
    windproof_needed: bool
    breathability: str
    layering_recommended: bool

_INSULATION_BY_BAND = {TemperatureBand.FREEZING : 5, 
              TemperatureBand.COLD : 4, 
              TemperatureBand.COOL : 3,
              TemperatureBand.PLEASANT : 2,
              TemperatureBand.WARM : 1,
              TemperatureBand.HOT : 1,
              TemperatureBand.VERY_HOT : 1}

def build_requirements(temp_band: TemperatureBand, wind_band: WindBand, humidity_band: HumidityBand, precipitation_band: PrecipitationBand) -> ClothingRequirements:
    water_proof = True
    wind_proof = False
    layering = False

    if precipitation_band == PrecipitationBand.NONE:
        water_proof = False

    if wind_band == WindBand.WINDY or wind_band == WindBand.VERY_WINDY:
        wind_proof = True

    if temp_band in [TemperatureBand.WARM, TemperatureBand.HOT, TemperatureBand.VERY_HOT] or humidity_band in [HumidityBand.HUMID, HumidityBand.VERY_HUMID]:
        breathability = "high"
    elif temp_band == TemperatureBand.PLEASANT:
        breathability = "medium"
    else:
        breathability = "low"

    if temp_band in [TemperatureBand.COOL, TemperatureBand.COLD, TemperatureBand.FREEZING]:
        layering = True

    
    return ClothingRequirements(_INSULATION_BY_BAND[temp_band], water_proof, wind_proof, breathability, layering)