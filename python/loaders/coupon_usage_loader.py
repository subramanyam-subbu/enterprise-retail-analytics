from python.database import get_connection


def load_coupon_usage(coupon_usage):
    """
    Insert one coupon usage record.
    """

    connection = get_connection()
    cursor = connection.cursor()

    insert_query = """
        INSERT INTO coupon_usage (
            coupon_id,
            customer_id,
            order_id,
            discount_amount,
            redeemed_at
        )
        VALUES (
            %s, %s, %s, %s, %s
        )
    """

    values = (
        coupon_usage["coupon_id"],
        coupon_usage["customer_id"],
        coupon_usage["order_id"],
        coupon_usage["discount_amount"],
        coupon_usage["redeemed_at"]
    )

    try:
        cursor.execute(insert_query, values)
        connection.commit()

    except Exception as e:
        connection.rollback()
        print(f"Error loading coupon usage: {e}")
        raise

    finally:
        cursor.close()
        connection.close()