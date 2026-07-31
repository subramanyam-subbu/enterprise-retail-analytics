from python.generators.return_generator import generate_return
from python.loaders.return_loader import load_return
from python.database import get_connection
import random


def get_order_items():
    """
    Get existing order items along with customer information.
    """

    connection = get_connection()
    cursor = connection.cursor()

    try:
        cursor.execute("""
            SELECT
                oi.order_item_id,
                o.customer_id,
                oi.line_total
            FROM order_items oi
            JOIN orders o
                ON oi.order_id = o.order_id
        """)

        return cursor.fetchall()

    finally:
        cursor.close()
        connection.close()


def run_return_pipeline(number_of_returns=100):

    print("Fetching existing order items...")

    order_items = get_order_items()

    if not order_items:
        raise Exception("No order items found in database.")

    print(f"Found {len(order_items)} order items.")

    # Select unique order items so we don't create
    # multiple returns for the same item.
    selected_items = random.sample(
        order_items,
        min(number_of_returns, len(order_items))
    )

    print(
        f"Generating {len(selected_items)} returns..."
    )

    loaded_count = 0

    for order_item_id, customer_id, line_total in selected_items:

        return_record = generate_return(
            order_item_id=order_item_id,
            customer_id=customer_id,
            line_total=float(line_total)
        )

        load_return(return_record)

        loaded_count += 1

    print(
        f"Successfully loaded {loaded_count} returns."
    )


if __name__ == "__main__":
    run_return_pipeline(100)