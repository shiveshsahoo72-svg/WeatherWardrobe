from interpretation import classify_temperature, classify_wind, TemperatureBand, WindBand

def test_freezing():
    assert classify_temperature(-5) == TemperatureBand.FREEZING

def test_windy():
    assert classify_wind(8) == WindBand.BREEZY