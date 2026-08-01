import random
from datetime import datetime


TRACKING_LOCATIONS = [
    "Chennai",
    "Hyderabad",
    "Bangalore",
    "Mumbai",
    "Delhi",
    "Pune",
    "Kolkata",
    "Ahmedabad",
    "Vijayawada",
    "Coimbatore"
]


REMARKS = {
    "Shipment Created": "Shipment has been created.",
    "Picked Up": "Shipment picked up from warehouse.",
    "In Transit": "Shipment is in transit.",
    "Arrived At Hub": "Shipment arrived at destination hub.",
    "Out For Delivery": "Shipment is out for delivery.",
    "Delivered": "Shipment delivered successfully.",
    "Delivery Failed": "Delivery attempt failed.",
    "Returned": "Shipment returned to warehouse."
}


def generate_tracking_event(
    shipment_id,
    tracking_status,
    event_time
):
    """
    Generate one shipment tracking event.
    """

    tracking_event = {
        "shipment_id": shipment_id,
        "tracking_status": tracking_status,
        "tracking_location": random.choice(TRACKING_LOCATIONS),
        "remarks": REMARKS.get(
            tracking_status,
            "Shipment status updated."
        ),
        "event_time": event_time
    }

    return tracking_event


if __name__ == "__main__":

    sample = generate_tracking_event(
        shipment_id=1,
        tracking_status="In Transit",
        event_time=datetime.now()
    )

    print(sample)