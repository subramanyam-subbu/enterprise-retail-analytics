from python.database import get_connection


def load_supplier(supplier):
    """
    Insert one supplier into the suppliers table.
    """

    connection = get_connection()
    cursor = connection.cursor()

    insert_query = """
        INSERT INTO suppliers (
            supplier_name,
            contact_person,
            email,
            phone,
            country,
            state,
            city,
            gst_number,
            payment_terms,
            supplier_status
        )
        VALUES (
            %s, %s, %s, %s, %s,
            %s, %s, %s, %s, %s
        )
    """

    values = (
        supplier["supplier_name"],
        supplier["contact_person"],
        supplier["email"],
        supplier["phone"],
        supplier["country"],
        supplier["state"],
        supplier["city"],
        supplier["gst_number"],
        supplier["payment_terms"],
        supplier["supplier_status"]
    )

    try:
        cursor.execute(insert_query, values)
        connection.commit()

    except Exception as e:
        connection.rollback()
        print(f"Error loading supplier: {e}")
        raise

    finally:
        cursor.close()
        connection.close()