import json
from logger import logger

def save_to_file(data, filename: str):
    logger.info(f"Salvando dados em {filename}")
    with open(filename, "w", encoding="utf-8") as f:
        json.dump(data, f, indent=2)
