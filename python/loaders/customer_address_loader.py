from python.database import get_connection


def load_customer_address(address):
    """
    Insert one customer address.
    """

    connection = get_connection()
    cursor = connection.cursor()

    insert_query = """
        INSERT INTO customer_addresses (
            customer_id,
            address_type,
            address_line1,
            address_line2,
            landmark,
            city,
            state,
            country,
            pincode,
            is_default
        )
        VALUES (
            %s, %s, %s, %s, %s,
            %s, %s, %s, %s, %s
        )
    """

    values = (
        address["customer_id"],
        address["address_type"],
        address["address_line1"],
        address["address_line2"],
        address["landmark"],
        address["city"],
        address["state"],
        address["country"],
        address["pincode"],
        address["is_default"]
    )

    try:
        cursor.execute(insert_query, values)
        connection.commit()

    except Exception as e:
        connection.rollback()
        print(f"Error loading customer address: {e}")
        raise

    finally:
        cursor.close()
        connection.close()