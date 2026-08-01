from python.database import get_connection


def load_inventory_transaction(transaction):
    """
    Insert one inventory transaction into the inventory_transactions table.
    """

    connection = get_connection()
    cursor = connection.cursor()

    insert_query = """
        INSERT INTO inventory_transactions (
            inventory_id,
            transaction_type,
            quantity,
            reference_type,
            reference_id,
            remarks,
            transaction_date
        )
        VALUES (
            %s, %s, %s, %s, %s, %s, %s
        )
    """

    values = (
        transaction["inventory_id"],
        transaction["transaction_type"],
        transaction["quantity"],
        transaction["reference_type"],
        transaction["reference_id"],
        transaction["remarks"],
        transaction["transaction_date"]
    )

    try:
        cursor.execute(insert_query, values)
        connection.commit()

    except Exception as e:
        connection.rollback()
        print(f"Error loading inventory transaction: {e}")
        raise

    finally:
        cursor.close()
        connection.close()