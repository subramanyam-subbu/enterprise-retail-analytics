"""
customer_loader.py

Loads validated customer records into MySQL.
"""

import mysql.connector

from config.database import get_connection


def load_customer(customer: dict) -> bool:
    """
    Inserts a single customer into MySQL.

    Returns:
        True  -> Success
        False -> Failure
    """

    connection = get_connection()

    if connection is None:
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
        %s,%s,%s,%s,%s,%s,%s,%s
    )
    """

    values = (
        customer["first_name"],
        customer["last_name"],
        customer["gender"],
        customer["email"],
        customer["phone_number"],
        customer["city"],
        customer["state"],
        customer["country"]
    )

    try:

        cursor.execute(query, values)

        connection.commit()

        print("✅ Customer inserted successfully.")

        return True

    except mysql.connector.Error as err:

        print(f"Database Error : {err}")

        connection.rollback()

        return False

    finally:

        cursor.close()

        connection.close()