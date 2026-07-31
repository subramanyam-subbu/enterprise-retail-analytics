from python.generators.shipment_generator import generate_shipment
from python.loaders.shipment_loader import load_shipment
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
                order_status
            FROM orders
            ORDER BY order_id
        """)

        return cursor.fetchall()

    finally:
        cursor.close()
        connection.close()


def run_shipment_pipeline():

    print("Fetching existing orders...")

    orders = get_orders()

    if not orders:
        raise Exception("No orders found in database.")

    print(f"Found {len(orders)} orders.")

    loaded_count = 0

    for order_id, order_status in orders:

        shipment = generate_shipment(
            order_id=order_id,
            order_status=order_status
        )

        load_shipment(shipment)

        loaded_count += 1

    print(
        f"Successfully loaded {loaded_count} shipments."
    )


if __name__ == "__main__":
    run_shipment_pipeline()