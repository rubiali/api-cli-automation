import argparse
from services import fetch_users
from config import API_URL
from logger import logger

def main():
    parser = argparse.ArgumentParser(description="CLI para consumo de API")
    parser.add_argument("--limit", type=int, default=5, help="Limite de usuários")
    parser.add_argument("--save", type=str, help="Salvar resultado em arquivo JSON")

    args = parser.parse_args()

    try:
        users = fetch_users(API_URL)[:args.limit]

        for user in users:
            print(f"{user['id']} - {user['email']}")

    except Exception as e:
        logger.error(f"Erro ao buscar dados: {e}")

def save_to_file(data, filename):
    import json
    with open(filename, "w", encoding="utf-8") as f:
        json.dump(data, f, indent=2)

if __name__ == "__main__":
    main()
