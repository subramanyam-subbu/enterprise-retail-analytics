from config.database import get_connection

def main():
    connection = get_connection()

    if connection:
        print("✅ Connected Successfully")
        connection.close()
    else:
        print("❌ Connection Failed")

if __name__ == "__main__":
    main()