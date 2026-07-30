"""
duplicate_checker.py

Detects duplicate customer records against:
1. Existing MySQL records
2. Duplicate records within the current batch
"""

from config.database import get_connection


def find_database_duplicates(
    customers: list[dict]
) -> list[dict]:
    """
    Find customers that already exist in MySQL
    based on email or phone number.
    """

    if not customers:
        return []

    connection = get_connection()

    if connection is None:
        raise ConnectionError(
            "Unable to connect to the database."
        )

    cursor = connection.cursor(dictionary=True)

    query = """
        SELECT email, phone_number
        FROM customers
        WHERE email = %s
           OR phone_number = %s
    """

    duplicates = []

    try:

        for customer in customers:

            cursor.execute(
                query,
                (
                    customer["email"],
                    customer["phone_number"]
                )
            )

            if cursor.fetchone():
                duplicates.append(customer)

    finally:

        cursor.close()
        connection.close()

    return duplicates


def find_batch_duplicates(
    customers: list[dict]
) -> list[dict]:
    """
    Find duplicate customers within the current batch.

    Email and phone number are used as unique identifiers.
    """

    seen_emails = set()
    seen_phones = set()

    duplicates = []

    for customer in customers:

        email = customer["email"].lower().strip()
        phone = customer["phone_number"]

        if (
            email in seen_emails
            or phone in seen_phones
        ):
            duplicates.append(customer)

        else:

            seen_emails.add(email)
            seen_phones.add(phone)

    return duplicates   