from python.generators.shipment_tracking_generator import (
    generate_tracking_event
)
from python.loaders.shipment_tracking_loader import (
    load_tracking_event
)
from python.database import get_connection
from datetime import timedelta


def get_shipments():
    """
    Fetch existing shipments with their delivery information.
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


def run_shipment_tracking_pipeline():

    print("Fetching existing shipments...")

    shipments = get_shipments()

    if not shipments:
        raise Exception("No shipments found in database.")

    print(f"Found {len(shipments)} shipments.")

    loaded_count = 0

    for (
        shipment_id,
        shipment_status,
        shipped_date,
        actual_delivery_date
    ) in shipments:

        # Shipment Created
        base_time = shipped_date

        if base_time is None:
            continue

        events = []

        events.append(
            (
                "Shipment Created",
                base_time
            )
        )

        # Picked Up
        events.append(
            (
                "Picked Up",
                base_time + timedelta(hours=6)
            )
        )

        # In Transit
        events.append(
            (
                "In Transit",
                base_time + timedelta(days=1)
            )
        )

        # Arrived At Hub
        events.append(
            (
                "Arrived At Hub",
                base_time + timedelta(days=2)
            )
        )

        # Out For Delivery
        if shipment_status in [
            "Out For Delivery",
            "Delivered"
        ]:

            events.append(
                (
                    "Out For Delivery",
                    base_time + timedelta(days=3)
                )
            )

        # Delivered
        if shipment_status == "Delivered":

            delivery_time = (
                actual_delivery_date
                if actual_delivery_date
                else base_time + timedelta(days=4)
            )

            events.append(
                (
                    "Delivered",
                    delivery_time
                )
            )

        # Failed
        elif shipment_status == "Failed":

            events.append(
                (
                    "Delivery Failed",
                    base_time + timedelta(days=3)
                )
            )

        # Returned
        elif shipment_status == "Returned":

            events.append(
                (
                    "Returned",
                    base_time + timedelta(days=4)
                )
            )

        for tracking_status, event_time in events:

            tracking_event = generate_tracking_event(
                shipment_id=shipment_id,
                tracking_status=tracking_status,
                event_time=event_time
            )

            load_tracking_event(tracking_event)

            loaded_count += 1

    print(
        f"Successfully loaded {loaded_count} tracking events."
    )


if __name__ == "__main__":
    run_shipment_tracking_pipeline()