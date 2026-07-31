from python.generators.order_item_generator import generate_order_item
from python.loaders.order_items_loader import load_order_items
from python.database import get_connection
import random


def run_order_item_pipeline(number_of_items=1000):

    connection = get_connection()
    cursor = connection.cursor()

    # Get existing orders
    cursor.execute("SELECT order_id FROM orders")
    orders = [row[0] for row in cursor.fetchall()]

    # Get existing products and their prices
    cursor.execute("""
        SELECT product_id, unit_price
        FROM products
        WHERE product_status = 'Active'
    """)

    products = cursor.fetchall()

    cursor.close()
    connection.close()

    if not orders:
        print("No orders found.")
        return

    if not products:
        print("No active products found.")
        return

    print(f"Generating {number_of_items} order items...")

    for _ in range(number_of_items):

        order_id = random.choice(orders)

        product_id, unit_price = random.choice(products)

        order_item = generate_order_item(
            order_id=order_id,
            product_id=product_id,
            unit_price=float(unit_price)
        )

        load_order_items(order_item)

    print(f"Successfully loaded {number_of_items} order items.")


if __name__ == "__main__":
    run_order_item_pipeline(1000)