import random
from datetime import datetime, timedelta


TRACKING_STATUSES = [
    "Shipment Created",
    "Picked Up",
    "In Transit",
    "Arrived At Hub",
    "Out For Delivery",
    "Delivered",
    "Delivery Failed",
    "Returned"
]

TRACKING_LOCATIONS = [
    "Chennai",
    "Bangalore",
    "Hyderabad",
    "Mumbai",
    "Delhi",
    "Pune",
    "Kolkata",
    "Ahmedabad",
    "Coimbatore",
    "Vijayawada"
]

REMARKS = {
    "Shipment Created": "Shipment created successfully",
    "Picked Up": "Package picked up from seller",
    "In Transit": "Package is in transit",
    "Arrived At Hub": "Package arrived at delivery hub",
    "Out For Delivery": "Package is out for delivery",
    "Delivered": "Package delivered successfully",
    "Delivery Failed": "Delivery attempt failed",
    "Returned": "Package returned to seller"
}


def generate_tracking_event(
    shipment_id,
    tracking_status,
    event_time
):
    """
    Generate one shipment tracking event.
    """

    tracking_location = random.choice(
        TRACKING_LOCATIONS
    )

    remarks = REMARKS.get(
        tracking_status,
        "Shipment status updated"
    )

    tracking_event = {
        "shipment_id": shipment_id,
        "tracking_status": tracking_status,
        "tracking_location": tracking_location,
        "remarks": remarks,
        "event_time": event_time
    }

    return tracking_event


if __name__ == "__main__":

    sample_event = generate_tracking_event(
        shipment_id=1,
        tracking_status="In Transit",
        event_time=datetime.now()
    )

    print(sample_event)