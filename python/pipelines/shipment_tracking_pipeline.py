from datetime import timedelta

from python.database import get_connection
from python.generators.shipment_tracking_generator import (
    generate_tracking_event,
)
from python.loaders.shipment_tracking_loader import (
    load_tracking_event,
)


def get_shipments():
    """
    Fetch shipments from database.
    """

    connection = get_connection()
    cursor = connection.cursor()

    try:
        cursor.execute("""
            SELECT
                shipment_id,
                shipment_status,
                shipped_date,
                actual_delivery_date
            FROM shipments
            ORDER BY shipment_id
        """)

        return cursor.fetchall()

    finally:
        cursor.close()
        connection.close()


def build_tracking_events(
    shipment_status,
    shipped_date,
    actual_delivery_date
):
    """
    Build tracking timeline for a shipment.
    """

    if shipped_date is None:
        return []

    events = []

    # Every shipped order gets these events
    events.append(("Shipment Created", shipped_date))
    events.append(("Picked Up", shipped_date + timedelta(hours=6)))
    events.append(("In Transit", shipped_date + timedelta(days=1)))
    events.append(("Arrived At Hub", shipped_date + timedelta(days=2)))

    if shipment_status == "Delivered":

        events.append((
            "Out For Delivery",
            shipped_date + timedelta(days=3)
        ))

        delivery_time = (
            actual_delivery_date
            if actual_delivery_date
            else shipped_date + timedelta(days=4)
        )

        events.append(("Delivered", delivery_time))

    elif shipment_status == "Out For Delivery":

        events.append((
            "Out For Delivery",
            shipped_date + timedelta(days=3)
        ))

    elif shipment_status == "Returned":

        events.append((
            "Returned",
            shipped_date + timedelta(days=3)
        ))

    elif shipment_status == "Failed":

        events.append((
            "Delivery Failed",
            shipped_date + timedelta(days=3)
        ))

    return events


def run_pipeline():

    print("=" * 60)
    print("Shipment Tracking Pipeline Started")
    print("=" * 60)

    shipments = get_shipments()

    print(f"Shipments Found : {len(shipments)}")

    total_loaded = 0

    for shipment in shipments:

        shipment_id = shipment[0]
        shipment_status = shipment[1]
        shipped_date = shipment[2]
        actual_delivery_date = shipment[3]

        events = build_tracking_events(
            shipment_status,
            shipped_date,
            actual_delivery_date
        )

        for tracking_status, event_time in events:

            tracking_event = generate_tracking_event(
                shipment_id=shipment_id,
                tracking_status=tracking_status,
                event_time=event_time
            )

            load_tracking_event(tracking_event)

            total_loaded += 1

            if total_loaded % 500 == 0:
                print(
                    f"{total_loaded} tracking events loaded..."
                )

    print("=" * 60)
    print(f"Pipeline Completed Successfully")
    print(f"Total Tracking Events : {total_loaded}")
    print("=" * 60)


if __name__ == "__main__":
    run_pipeline()