# KevinMejiaOceanic2025

Backend en **FastAPI** para el microproyecto técnico de Oceanic.

Este proyecto consiste en una aplicación backend desarrollada con FastAPI que permite consultar información del clima en Marte proveniente de la misión InSight de la NASA y complementarla con un modelo de inteligencia artificial para responder preguntas en lenguaje natural sobre los datos almacenados.

## Endpoints / Funcionalidades
- `GET /fetch-and-store-data` → Consume API de la nasa NASA y almacena en SQLite.
- `GET /gemini-prompt?query=` → Intelifencia Artificial response sobre el clima en Marte.

## Tecnologías usadas
- Python (v3.13.7)
- FastAPI (v0.116.1)
- Uvicorn (v0.35.0)
- Pydantic (v2.11.9)
- Requests (v2.32.5)
- Python-dotenv (v1.1.1)
- SQLite3

## Instalación
```bash
python -m venv venv
source venv/bin/activate   # Linux / macOS
venv\Scripts\activate    # Windows
pip install -r requirements.txt
```

## Ejecución
```bash
uvicorn app.main:app --reload
```

Luego abre en: http://127.0.0.1:8000/docs

