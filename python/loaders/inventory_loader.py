from python.database import get_connection


def load_inventory(inventory):
    """
    Insert one inventory record into the inventory table.
    """

    connection = get_connection()
    cursor = connection.cursor()

    insert_query = """
        INSERT INTO inventory (
            warehouse_id,
            product_id,
            available_quantity,
            reserved_quantity,
            damaged_quantity,
            reorder_level,
            last_stock_update
        )
        VALUES (
            %s, %s, %s, %s, %s, %s, %s
        )
    """

    values = (
        inventory["warehouse_id"],
        inventory["product_id"],
        inventory["available_quantity"],
        inventory["reserved_quantity"],
        inventory["damaged_quantity"],
        inventory["reorder_level"],
        inventory["last_stock_update"]
    )

    try:
        cursor.execute(insert_query, values)
        connection.commit()

    except Exception as e:
        connection.rollback()
        print(f"Error loading inventory: {e}")
        raise

    finally:
        cursor.close()
        connection.close()