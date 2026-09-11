from interpretation import classify_temperature, classify_wind, classify_humidity, TemperatureBand, WindBand, HumidityBand

def test_freezing():
    assert classify_temperature(-5) == TemperatureBand.FREEZING

def test_windy():
    assert classify_wind(8) == WindBand.BREEZY

def test_humidity():
    assert classify_humidity(45) == HumidityBand.COMFORTABLE