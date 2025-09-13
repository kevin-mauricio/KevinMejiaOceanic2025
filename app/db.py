import sqlite3
from typing import List

from app.models import WeatherSol
database = "weather_data.sqlite3"

def init_db(database: str = database):
    connection = sqlite3.connect(database)
    cursor = connection.cursor()
    cursor.execute('''CREATE TABLE IF NOT EXISTS weather_sol (
        sol INTEGER PRIMARY KEY,
        temp_av REAL,
        temp_max REAL,
        temp_min REAL,
        season TEXT
    )''')
    connection.commit()
    connection.close()

def insert_weather_sol(rows: List[WeatherSol], database: str = database):
    connection = sqlite3.connect(database)
    cursor = connection.cursor()
    data_tuples = [(row.sol, row.temp_av, row.temp_max, row.temp_min, row.season) for row in rows]
    cursor.executemany('''
        INSERT OR REPLACE INTO weather_sol (sol, temp_av, temp_max, temp_min, season)
        VALUES (?, ?, ?, ?, ?)
    ''', data_tuples)
    connection.commit()
    connection.close()
    
def get_all_weather_sols(database: str = database) -> List[WeatherSol]:
    connection = sqlite3.connect(database)
    cursor = connection.cursor()
    cursor.execute('SELECT sol, temp_av, temp_max, temp_min, season FROM weather_sol')
    rows = cursor.fetchall()
    connection.close()
    return [WeatherSol(sol=row[0], temp_av=row[1], temp_max=row[2], temp_min=row[3], season=row[4]) for row in rows]
