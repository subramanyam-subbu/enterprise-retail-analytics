import random
import uuid
from datetime import datetime, timedelta


ORDER_STATUSES = [
    "Pending",
    "Confirmed",
    "Packed",
    "Shipped",
    "Delivered",
    "Cancelled",
    "Returned"
]

PAYMENT_STATUSES = [
    "Pending",
    "Paid",
    "Failed",
    "Refunded"
]


def generate_order(customer_id):
    """
    Generate one realistic customer order.
    """

    order_date = datetime.now() - timedelta(
        days=random.randint(0, 365)
    )

    subtotal = round(
        random.uniform(500, 50000),
        2
    )

    discount_amount = round(
        subtotal * random.uniform(0, 0.20),
        2
    )

    taxable_amount = subtotal - discount_amount

    tax_amount = round(
        taxable_amount * random.uniform(0.05, 0.18),
        2
    )

    shipping_charges = round(
        random.uniform(0, 500),
        2
    )

    total_amount = round(
        taxable_amount
        + tax_amount
        + shipping_charges,
        2
    )

    order_status = random.choices(
        ORDER_STATUSES,
        weights=[5, 8, 7, 10, 60, 7, 3],
        k=1
    )[0]

    if order_status == "Delivered":
        payment_status = "Paid"

    elif order_status == "Cancelled":
        payment_status = random.choice(
            ["Failed", "Refunded", "Pending"]
        )

    elif order_status == "Returned":
        payment_status = "Refunded"

    else:
        payment_status = random.choices(
            PAYMENT_STATUSES,
            weights=[15, 70, 5, 10],
            k=1
        )[0]

    order = {
        "order_number": f"ORD-{datetime.now().strftime('%Y%m%d%H%M%S%f')}-{uuid.uuid4().hex[:6].upper()}",
        "customer_id": customer_id,
        "order_date": order_date,
        "order_status": order_status,
        "payment_status": payment_status,
        "subtotal": subtotal,
        "discount_amount": discount_amount,
        "tax_amount": tax_amount,
        "shipping_charges": shipping_charges,
        "total_amount": total_amount
    }

    return order


if __name__ == "__main__":

    sample_order = generate_order(customer_id=1)

    print(sample_order)