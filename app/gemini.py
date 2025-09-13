from typing import List
import os
import google.generativeai as genai

from app.db import get_all_weather_sols
from app.models import WeatherSol


def query_gemini_api(query: str, model: str = "gemini-1.5-flash") -> str:
    KEY = os.getenv("GEMINI_API_KEY")
    if not KEY:
        return "Error: GEMINI_API_KEY environment variable not set"
    
    genai.configure(api_key=KEY)
    data = get_all_weather_sols()
    context = set_context(data)
    prompt = f"Según la siguiente información del clima en Marte:\n{context}\n\nPregunta: {query}"

    try:
        model_instance = genai.GenerativeModel(model)
        response = model_instance.generate_content(prompt)
        return response.text.strip() if response.text else "No hubo respuesta del modelo."
    except Exception as e:
        return f"Error querying Gemini API: {str(e)}"


def set_context(data: List[WeatherSol]) -> str:
    return "\n".join(
        f"Sol: {item.sol}, Temp Avg: {item.temp_av}, Temp Max: {item.temp_max}, Temp Min: {item.temp_min}, Season: {item.season}"
        for item in data
    )
