from python.generators.order_generator import generate_order
from python.loaders.order_loader import load_orders
from python.database import get_connection


def get_customer_ids():
    """
    Get existing customer IDs from the database.
    """

    connection = get_connection()
    cursor = connection.cursor()

    try:
        cursor.execute("""
            SELECT customer_id
            FROM customers
            ORDER BY customer_id
        """)

        rows = cursor.fetchall()

        return [row[0] for row in rows]

    finally:
        cursor.close()
        connection.close()


def run_order_pipeline(number_of_orders=1000):

    print("Fetching existing customers...")

    customer_ids = get_customer_ids()

    if not customer_ids:
        raise Exception("No customers found in database.")

    print(f"Found {len(customer_ids)} customers.")

    print(f"Generating {number_of_orders} orders...")

    orders = []

    for _ in range(number_of_orders):

        customer_id = customer_ids[
            __import__("random").randint(
                0,
                len(customer_ids) - 1
            )
        ]

        order = generate_order(customer_id)

        orders.append(order)

    print(f"Generated {len(orders)} orders.")

    print("Loading orders into RDS...")

    load_orders(orders)

    print("Order pipeline completed successfully.")


if __name__ == "__main__":
    run_order_pipeline(1000)