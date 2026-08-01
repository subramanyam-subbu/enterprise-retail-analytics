from python.database import get_connection
from python.generators.loyalty_account_generator import (
    generate_loyalty_account
)
from python.loaders.loyalty_account_loader import (
    load_loyalty_account
)


def get_customer_ids():
    """
    Fetch all customer IDs.
    """

    connection = get_connection()
    cursor = connection.cursor()

    try:
        cursor.execute("""
            SELECT customer_id
            FROM customers
            ORDER BY customer_id
        """)

        return cursor.fetchall()

    finally:
        cursor.close()
        connection.close()


def run_pipeline():

    print("=" * 60)
    print("Loyalty Account Pipeline Started")
    print("=" * 60)

    customers = get_customer_ids()

    print(f"Customers Found : {len(customers)}")

    loaded = 0

    for customer in customers:

        customer_id = customer[0]

        account = generate_loyalty_account(customer_id)

        load_loyalty_account(account)

        loaded += 1

        if loaded % 100 == 0:
            print(f"{loaded} loyalty accounts loaded...")

    print("=" * 60)
    print("Pipeline Completed Successfully")
    print(f"Total Loyalty Accounts Loaded : {loaded}")
    print("=" * 60)


if __name__ == "__main__":
    run_pipeline()