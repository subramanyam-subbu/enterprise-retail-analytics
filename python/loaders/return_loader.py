from python.database import get_connection


def load_return(return_record):
    """
    Insert one return record into the returns table.
    """

    connection = get_connection()
    cursor = connection.cursor()

    insert_query = """
        INSERT INTO returns (
            order_item_id,
            customer_id,
            return_reason,
            return_status,
            refund_amount,
            return_date,
            remarks
        )
        VALUES (
            %s, %s, %s, %s, %s, %s, %s
        )
    """

    values = (
        return_record["order_item_id"],
        return_record["customer_id"],
        return_record["return_reason"],
        return_record["return_status"],
        return_record["refund_amount"],
        return_record["return_date"],
        return_record["remarks"]
    )

    try:
        cursor.execute(insert_query, values)
        connection.commit()

        print("Return loaded successfully.")

    except Exception as e:
        connection.rollback()
        print("Error while loading return:", e)
        raise

    finally:
        cursor.close()
        connection.close()