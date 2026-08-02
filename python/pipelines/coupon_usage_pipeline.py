import random

from python.database import get_connection
from python.generators.coupon_usage_generator import generate_coupon_usage
from python.loaders.coupon_usage_loader import load_coupon_usage

TOTAL_USAGES = 100


def fetch_ids(query):
    """
    Execute a query and return the first column as a list.
    """

    connection = get_connection()
    cursor = connection.cursor()

    try:
        cursor.execute(query)
        return [row[0] for row in cursor.fetchall()]

    finally:
        cursor.close()
        connection.close()


def run_pipeline():

    print("=" * 60)
    print("Coupon Usage Pipeline Started")
    print("=" * 60)

    coupon_ids = fetch_ids("""
        SELECT coupon_id
        FROM coupons
    """)

    customer_ids = fetch_ids("""
        SELECT customer_id
        FROM customers
    """)

    order_ids = fetch_ids("""
        SELECT order_id
        FROM orders
    """)

    if not coupon_ids:
        print("No coupons found.")
        return

    if not customer_ids:
        print("No customers found.")
        return

    if not order_ids:
        print("No orders found.")
        return

    # order_id must be UNIQUE in coupon_usage
    random.shuffle(order_ids)

    total_records = min(
        TOTAL_USAGES,
        len(order_ids)
    )

    loaded = 0

    for order_id in order_ids[:total_records]:

        coupon_id = random.choice(coupon_ids)
        customer_id = random.choice(customer_ids)

        usage = generate_coupon_usage(
            coupon_id,
            customer_id,
            order_id
        )

        load_coupon_usage(usage)

        loaded += 1

        if loaded % 20 == 0:
            print(f"{loaded} coupon usages loaded...")

    print("=" * 60)
    print("Pipeline Completed Successfully")
    print(f"Total Coupon Usage Loaded : {loaded}")
    print("=" * 60)


if __name__ == "__main__":
    run_pipeline()