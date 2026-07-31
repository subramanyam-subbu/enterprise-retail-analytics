import random
import uuid
from datetime import datetime, timedelta


COURIERS = [
    "Blue Dart",
    "Delhivery",
    "DTDC",
    "Ecom Express",
    "XpressBees",
    "Ekart",
    "FedEx",
    "DHL"
]

SHIPMENT_STATUSES = [
    "Pending",
    "Packed",
    "Shipped",
    "In Transit",
    "Out For Delivery",
    "Delivered",
    "Failed",
    "Returned"
]


def generate_shipment(order_id, order_status):
    """
    Generate one realistic shipment record.
    """

    # Cancelled orders normally don't get shipped
    if order_status == "Cancelled":
        shipment_status = "Pending"

    elif order_status == "Returned":
        shipment_status = "Returned"

    elif order_status == "Delivered":
        shipment_status = "Delivered"

    else:
        shipment_status = random.choices(
            SHIPMENT_STATUSES,
            weights=[5, 8, 15, 20, 10, 35, 4, 3],
            k=1
        )[0]

    courier_name = random.choice(COURIERS)

    tracking_number = (
        f"TRK-{uuid.uuid4().hex[:16].upper()}"
    )

    shipping_cost = round(
        random.uniform(40, 500),
        2
    )

    base_date = datetime.now() - timedelta(
        days=random.randint(0, 365)
    )

    shipped_date = None
    expected_delivery_date = None
    actual_delivery_date = None

    if shipment_status not in ["Pending"]:

        shipped_date = base_date

        expected_delivery_date = (
            shipped_date + timedelta(
                days=random.randint(2, 7)
            )
        )

        if shipment_status == "Delivered":

            actual_delivery_date = (
                expected_delivery_date
                - timedelta(
                    days=random.randint(0, 2)
                )
            )

    shipment = {
        "order_id": order_id,
        "courier_name": courier_name,
        "tracking_number": tracking_number,
        "shipment_status": shipment_status,
        "shipping_cost": shipping_cost,
        "shipped_date": shipped_date,
        "expected_delivery_date": expected_delivery_date,
        "actual_delivery_date": actual_delivery_date
    }

    return shipment


if __name__ == "__main__":

    sample_shipment = generate_shipment(
        order_id=1,
        order_status="Delivered"
    )

    print(sample_shipment)