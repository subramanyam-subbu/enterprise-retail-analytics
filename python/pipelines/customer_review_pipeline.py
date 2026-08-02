import random

from python.database import get_connection
from python.generators.customer_review_generator import (
    generate_customer_review
)
from python.loaders.customer_review_loader import (
    load_customer_review
)

TOTAL_REVIEWS = 500


def fetch_rows(query):
    """
    Execute query and return all rows.
    """
    connection = get_connection()
    cursor = connection.cursor()

    try:
        cursor.execute(query)
        return cursor.fetchall()

    finally:
        cursor.close()
        connection.close()


def run_pipeline():

    print("=" * 60)
    print("Customer Review Pipeline Started")
    print("=" * 60)

    # Fetch order details because reviews should belong to actual purchases
    order_rows = fetch_rows("""
        SELECT DISTINCT
            o.customer_id,
            oi.product_id,
            o.order_id
        FROM orders o
        INNER JOIN order_items oi
            ON o.order_id = oi.order_id
    """)

    if not order_rows:
        print("No order data found.")
        return

    # Shuffle for randomness
    random.shuffle(order_rows)

    total_reviews = min(TOTAL_REVIEWS, len(order_rows))

    loaded = 0

    for customer_id, product_id, order_id in order_rows[:total_reviews]:

        review = generate_customer_review(
            customer_id=customer_id,
            product_id=product_id,
            order_id=order_id
        )

        load_customer_review(review)

        loaded += 1

        if loaded % 50 == 0:
            print(f"{loaded} customer reviews loaded...")

    print("=" * 60)
    print("Pipeline Completed Successfully")
    print(f"Total Customer Reviews Loaded : {loaded}")
    print("=" * 60)


if __name__ == "__main__":
    run_pipeline()