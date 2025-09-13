from pydantic import BaseModel


class WeatherSol(BaseModel):
    sol: int
    temp_av: float
    temp_max: float
    temp_min: float
    season: str