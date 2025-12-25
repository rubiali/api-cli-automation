import requests
from logger import logger

def fetch_users(api_url: str):
    logger.info(f"Buscando usuários em {api_url}")

    response = requests.get(api_url, timeout=5)
    response.raise_for_status()

    logger.info("Usuários obtidos com sucesso")
    return response.json()
