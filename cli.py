from services import fetch_users
from config import API_URL

def main():
    try:
        users = fetch_users(API_URL)
        for user in users:
            print(f"{user['id']} - {user['email']}")
    except Exception as e:
        print(f"Erro ao buscar dados: {e}")

if __name__ == "__main__":
    main()
