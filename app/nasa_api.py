

import os
import requests
from dotenv import load_dotenv
from app.db import insert_weather_sol
from app.models import WeatherSol

load_dotenv()
URL_BASE = 'https://api.nasa.gov/insight_weather/'
KEY = os.getenv('NASA_API_KEY')

def get_insight_data():
    if not KEY:
        return {"error": "NASA_API_KEY environment variable not set"}   
    
    params = {
        "api_key": KEY,
        "feedtype": "json",
        "ver": "1.0"
    }
    response = requests.get(URL_BASE, params=params,timeout=15)
    if response.status_code != 200:
        return {"error": "Failed to fetch data from NASA API"}
    
    return response.json()

def store_data():
    response = get_insight_data()
    if "error" in response:
        return response
    
    records = extract_rows(response)
    if not records or len(records) == 0:
        return {"error": "No valid weather data found"}
    
    insert_weather_sol(records)
    return {"message": "Data fetched and stored successfully. Row count: {}".format(len(records))}

def extract_rows(data: dict):
    sol_keys = data.get("sol_keys", [])
    print(sol_keys)
    rows = []
    
    for key in sol_keys:
        sol = data.get(key, {})
        temp_av = sol.get("AT", {}).get("av")
        temp_max = sol.get("AT", {}).get("mx")
        temp_min = sol.get("AT", {}).get("mn")
        season = sol.get("Season")
        
        if None in (temp_av, temp_max, temp_min, season):
            return None
        
        row = WeatherSol(
            sol=int(key),
            temp_av=float(temp_av),
            temp_max=float(temp_max),
            temp_min=float(temp_min),
            season=season
        )
        rows.append(row)

    return rows
