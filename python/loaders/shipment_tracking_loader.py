from python.database import get_connection


def load_tracking_event(tracking_event):
    """
    Insert one shipment tracking event into the shipment_tracking table.
    """

    connection = get_connection()
    cursor = connection.cursor()

    insert_query = """
        INSERT INTO shipment_tracking (
            shipment_id,
            tracking_status,
            tracking_location,
            remarks,
            event_time
        )
        VALUES (
            %s, %s, %s, %s, %s
        )
    """

    values = (
        tracking_event["shipment_id"],
        tracking_event["tracking_status"],
        tracking_event["tracking_location"],
        tracking_event["remarks"],
        tracking_event["event_time"]
    )

    try:
        cursor.execute(insert_query, values)
        connection.commit()

    except Exception as e:
        connection.rollback()
        print(f"Error loading tracking event: {e}")
        raise

    finally:
        cursor.close()
        connection.close()