import argparse
from services import fetch_users
from config import API_URL
from storage import save_to_file
from logger import logger

def main():
    parser = argparse.ArgumentParser(description="CLI para consumo de API")
    parser.add_argument("--limit", type=int, default=5)
    parser.add_argument("--save", type=str)

    args = parser.parse_args()

    try:
        users = fetch_users(API_URL)[:args.limit]

        for user in users:
            print(f"{user['id']} - {user['email']}")

        if args.save:
            save_to_file(users, args.save)

    except Exception as e:
        logger.error(f"Erro ao buscar dados: {e}")

if __name__ == "__main__":
    main()
