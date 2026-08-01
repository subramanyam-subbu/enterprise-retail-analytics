from python.database import get_connection
from python.generators.customer_address_generator import generate_customer_address
from python.loaders.customer_address_loader import load_customer_address


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
    print("Customer Address Pipeline Started")
    print("=" * 60)

    customers = get_customer_ids()

    print(f"Customers Found : {len(customers)}")

    loaded = 0

    for customer in customers:

        customer_id = customer[0]

        address = generate_customer_address(customer_id)

        load_customer_address(address)

        loaded += 1

        if loaded % 100 == 0:
            print(f"{loaded} customer addresses loaded...")

    print("=" * 60)
    print("Pipeline Completed Successfully")
    print(f"Total Customer Addresses Loaded : {loaded}")
    print("=" * 60)


if __name__ == "__main__":
    run_pipeline()