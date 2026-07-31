from python.generators.payment_generator import generate_payment
from python.loaders.payment_loader import load_payment
from python.database import get_connection


def get_orders():
    """
    Fetch existing orders from the database.
    """

    connection = get_connection()
    cursor = connection.cursor()

    try:
        cursor.execute("""
            SELECT
                order_id,
                order_status,
                total_amount
            FROM orders
            ORDER BY order_id
        """)

        return cursor.fetchall()

    finally:
        cursor.close()
        connection.close()


def run_payment_pipeline():

    print("Fetching existing orders...")

    orders = get_orders()

    if not orders:
        raise Exception("No orders found in database.")

    print(f"Found {len(orders)} orders.")

    loaded_count = 0

    for order_id, order_status, total_amount in orders:

        payment = generate_payment(
            order_id=order_id,
            payment_amount=total_amount,
            order_status=order_status
        )

        load_payment(payment)

        loaded_count += 1

    print(
        f"Successfully loaded {loaded_count} payments."
    )


if __name__ == "__main__":
    run_payment_pipeline()