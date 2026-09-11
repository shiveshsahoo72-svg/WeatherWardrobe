from requirements import TemperatureBand, WindBand, HumidityBand, PrecipitationBand, ClothingRequirements, build_requirements

def test_cool_and_calm_needs_no_waterproofing():
    assert build_requirements(TemperatureBand.COOL, WindBand.CALM, HumidityBand.COMFORTABLE, PrecipitationBand.NONE) == ClothingRequirements(3, False, False, "low", True)

def test_cool_and_rainy_needs_waterproof_and_windproof():
    assert build_requirements(TemperatureBand.COOL, WindBand.WINDY, HumidityBand.COMFORTABLE, PrecipitationBand.RAIN) == ClothingRequirements(3, True, True, "low", True)

def test_different_conditions_differ():
    calm = build_requirements(TemperatureBand.COOL, WindBand.CALM, HumidityBand.COMFORTABLE, PrecipitationBand.NONE)
    windy = build_requirements(TemperatureBand.COOL, WindBand.WINDY, HumidityBand.COMFORTABLE, PrecipitationBand.NONE)

    assert calm != windy