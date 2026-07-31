from python.database import get_connection


def load_payment(payment):
    """
    Insert one payment record into the payments table.
    """

    connection = get_connection()
    cursor = connection.cursor()

    insert_query = """
        INSERT INTO payments (
            order_id,
            payment_method,
            payment_status,
            transaction_reference,
            payment_amount,
            payment_date
        )
        VALUES (
            %s, %s, %s, %s, %s, %s
        )
    """

    values = (
        payment["order_id"],
        payment["payment_method"],
        payment["payment_status"],
        payment["transaction_reference"],
        payment["payment_amount"],
        payment["payment_date"]
    )

    try:
        cursor.execute(insert_query, values)
        connection.commit()

        print("Payment loaded successfully.")

    except Exception as e:
        connection.rollback()
        print("Error while loading payment:", e)
        raise

    finally:
        cursor.close()
        connection.close()