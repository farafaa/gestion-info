"""
file.py — Persistencia de datos
Lectura y escritura segura del archivo JSON.
"""

import json
import os

# Ruta relativa al archivo de datos (desde src/)
DATA_PATH = os.path.join(os.path.dirname(__file__), "..", "data", "records.json")


def load_records() -> list:
    """
    Carga y retorna la lista de registros desde el archivo JSON.
    Retorna lista vacía si el archivo no existe o está corrupto.
    """
    try:
        with open(DATA_PATH, "r", encoding="utf-8") as f:
            data = json.load(f)
            if isinstance(data, list):
                return data
            return []
    except FileNotFoundError:
        return []
    except json.JSONDecodeError as e:
        print(f"[ADVERTENCIA] El archivo de datos está corrupto: {e}")
        return []


def save_records(records: list) -> bool:
    """
    Guarda la lista de registros en el archivo JSON.
    Retorna True si tuvo éxito, False en caso de error.
    """
    try:
        # Asegura que el directorio data/ exista
        os.makedirs(os.path.dirname(DATA_PATH), exist_ok=True)

        with open(DATA_PATH, "w", encoding="utf-8") as f:
            json.dump(records, f, ensure_ascii=False, indent=2)
        return True
    except OSError as e:
        print(f"[ERROR] No se pudo guardar el archivo: {e}")
        return False
