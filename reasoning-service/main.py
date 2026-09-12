from fastapi import FastAPI
from pydantic import BaseModel

from interpretation import (
    classify_temperature,
    classify_wind,
    classify_humidity,
    classify_precipitation,
)
from requirements import build_requirements, ClothingRequirements

class WeatherSnapshot(BaseModel):
    city : str
    country : str
    temperature : float
    feelsLike : float
    tempMin : float
    tempMax : float
    humidity : int
    windSpeed : float
    condition : str
    conditionDescription : str
    cloudCover : int
    timestamp : str

app = FastAPI()

@app.post("/recommend")
def recommend(snapshot : WeatherSnapshot) -> ClothingRequirements:
    return build_requirements(
        classify_temperature(snapshot.feelsLike), 
        classify_wind(snapshot.windSpeed), 
        classify_humidity(snapshot.humidity), 
        classify_precipitation(snapshot.condition))