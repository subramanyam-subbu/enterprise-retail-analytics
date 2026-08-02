from python.database import get_connection


def load_customer_review(review):
    """
    Insert one customer review into the customer_reviews table.
    """

    connection = get_connection()
    cursor = connection.cursor()

    insert_query = """
        INSERT INTO customer_reviews (
            customer_id,
            product_id,
            order_id,
            rating,
            review_title,
            review_text,
            is_verified_purchase,
            review_date
        )
        VALUES (
            %s, %s, %s, %s,
            %s, %s, %s, %s
        )
    """

    values = (
        review["customer_id"],
        review["product_id"],
        review["order_id"],
        review["rating"],
        review["review_title"],
        review["review_text"],
        review["is_verified_purchase"],
        review["review_date"]
    )

    try:
        cursor.execute(insert_query, values)
        connection.commit()

    except Exception as e:
        connection.rollback()
        print(f"Error loading customer review: {e}")
        raise

    finally:
        cursor.close()
        connection.close()