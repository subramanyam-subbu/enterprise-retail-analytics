import mysql.connector

from config.settings import settings

def get_connection():
    try:
        connection = mysql.connector.connect(
            host=settings.DB_HOST,
            port=settings.DB_PORT,
            database=settings.DB_NAME,
            user=settings.DB_USER,
            password=settings.DB_PASSWORD
        )

        return connection

    except mysql.connector.Error as err:
        print(f"Database erros:{err}")
        return None



