from python.database import get_connection


def load_shipment(shipment):
    """
    Insert one shipment record into the shipments table.
    """

    connection = get_connection()
    cursor = connection.cursor()

    insert_query = """
        INSERT INTO shipments (
            order_id,
            courier_name,
            tracking_number,
            shipment_status,
            shipping_cost,
            shipped_date,
            expected_delivery_date,
            actual_delivery_date
        )
        VALUES (
            %s, %s, %s, %s, %s, %s, %s, %s
        )
    """

    values = (
        shipment["order_id"],
        shipment["courier_name"],
        shipment["tracking_number"],
        shipment["shipment_status"],
        shipment["shipping_cost"],
        shipment["shipped_date"],
        shipment["expected_delivery_date"],
        shipment["actual_delivery_date"]
    )

    try:
        cursor.execute(insert_query, values)
        connection.commit()

        print("Shipment loaded successfully.")

    except Exception as e:
        connection.rollback()
        print("Error while loading shipment:", e)
        raise

    finally:
        cursor.close()
        connection.close()