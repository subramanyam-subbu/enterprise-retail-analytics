from python.database import get_connection


def load_orders(orders):
    """
    Insert generated orders into the orders table.
    """

    connection = get_connection()
    cursor = connection.cursor()

    insert_query = """
        INSERT INTO orders (
            order_number,
            customer_id,
            order_date,
            order_status,
            payment_status,
            subtotal,
            discount_amount,
            tax_amount,
            shipping_charges,
            total_amount
        )
        VALUES (
            %s, %s, %s, %s, %s,
            %s, %s, %s, %s, %s
        )
    """

    try:

        for order in orders:

            values = (
                order["order_number"],
                order["customer_id"],
                order["order_date"],
                order["order_status"],
                order["payment_status"],
                order["subtotal"],
                order["discount_amount"],
                order["tax_amount"],
                order["shipping_charges"],
                order["total_amount"]
            )

            cursor.execute(insert_query, values)

        connection.commit()

        print(f"Successfully loaded {len(orders)} orders.")

    except Exception as e:

        connection.rollback()

        print("Error while loading orders:", e)

        raise

    finally:

        cursor.close()
        connection.close()