from python.database import get_connection


def load_warehouse(warehouse):
    """
    Insert one warehouse into the warehouses table.
    """

    connection = get_connection()
    cursor = connection.cursor()

    insert_query = """
        INSERT INTO warehouses (
            warehouse_name,
            warehouse_code,
            city,
            state,
            country,
            warehouse_status
        )
        VALUES (
            %s, %s, %s, %s, %s, %s
        )
    """

    values = (
        warehouse["warehouse_name"],
        warehouse["warehouse_code"],
        warehouse["city"],
        warehouse["state"],
        warehouse["country"],
        warehouse["warehouse_status"]
    )

    try:
        cursor.execute(insert_query, values)
        connection.commit()

    except Exception as e:
        connection.rollback()
        print(f"Error loading warehouse: {e}")
        raise

    finally:
        cursor.close()
        connection.close()