from interpretation import classify_temperature, TemperatureBand

def test_freezing():
    assert classify_temperature(-5) == TemperatureBand.FREEZING