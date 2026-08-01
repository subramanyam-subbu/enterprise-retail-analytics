from python.database import get_connection


def load_coupon(coupon):
    """
    Insert one coupon into the coupons table.
    """

    connection = get_connection()
    cursor = connection.cursor()

    insert_query = """
        INSERT INTO coupons (
            campaign_id,
            coupon_code,
            discount_type,
            discount_value,
            minimum_order_amount,
            maximum_discount,
            valid_from,
            valid_to,
            usage_limit,
            coupon_status
        )
        VALUES (
            %s, %s, %s, %s, %s,
            %s, %s, %s, %s, %s
        )
    """

    values = (
        coupon["campaign_id"],
        coupon["coupon_code"],
        coupon["discount_type"],
        coupon["discount_value"],
        coupon["minimum_order_amount"],
        coupon["maximum_discount"],
        coupon["valid_from"],
        coupon["valid_to"],
        coupon["usage_limit"],
        coupon["coupon_status"]
    )

    try:
        cursor.execute(insert_query, values)
        connection.commit()

    except Exception as e:
        connection.rollback()
        print(f"Error loading coupon: {e}")
        raise

    finally:
        cursor.close()
        connection.close()