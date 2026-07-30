"""
customer_loader.py

Loads customer records into MySQL using batch processing.
"""

import mysql.connector

from config.database import get_connection


def load_customers(customers: list[dict]) -> bool:
    """
    Insert multiple customer records into MySQL.

    Parameters:
        customers: List of validated customer dictionaries.

    Returns:
        True if the batch is successfully inserted.
        False if an error occurs.
    """

    if not customers:
        print("No customers to load.")
        return False

    connection = get_connection()

    if connection is None:
        print("Database connection failed.")
        return False

    cursor = connection.cursor()

    query = """
        INSERT INTO customers
        (
            first_name,
            last_name,
            gender,
            email,
            phone_number,
            city,
            state,
            country
        )
        VALUES
        (
            %s, %s, %s, %s,
            %s, %s, %s, %s
        )
    """

    values = [
        (
            customer["first_name"],
            customer["last_name"],
            customer["gender"],
            customer["email"],
            customer["phone_number"],
            customer["city"],
            customer["state"],
            customer["country"]
        )
        for customer in customers
    ]

    try:
        cursor.executemany(query, values)

        connection.commit()

        print(
            f"✅ Successfully inserted "
            f"{cursor.rowcount} customers."
        )

        return True

    except mysql.connector.Error as err:

        print(f"❌ Database Error: {err}")

        connection.rollback()

        return False

    finally:

        cursor.close()
        connection.close()