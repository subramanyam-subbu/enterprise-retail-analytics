import random
import uuid
from datetime import datetime, timedelta


PAYMENT_METHODS = [
    "Credit Card",
    "Debit Card",
    "UPI",
    "Net Banking",
    "Cash on Delivery",
    "Wallet",
    "Gift Card"
]


def generate_payment(order_id, payment_amount, order_status):
    """
    Generate one realistic payment record.
    """

    if order_status == "Cancelled":
        payment_status = random.choice(
            ["Failed", "Refunded", "Pending"]
        )

    elif order_status == "Returned":
        payment_status = "Refunded"

    elif order_status == "Pending":
        payment_status = random.choice(
            ["Pending", "Failed"]
        )

    else:
        payment_status = random.choices(
            ["Success", "Failed", "Pending"],
            weights=[90, 5, 5],
            k=1
        )[0]

    payment_method = random.choice(PAYMENT_METHODS)

    if payment_status == "Success":
        payment_date = datetime.now() - timedelta(
            days=random.randint(0, 365)
        )
    else:
        payment_date = datetime.now() - timedelta(
            days=random.randint(0, 365)
        )

    transaction_reference = (
        f"TXN-{uuid.uuid4().hex[:16].upper()}"
    )

    payment = {
        "order_id": order_id,
        "payment_method": payment_method,
        "payment_status": payment_status,
        "transaction_reference": transaction_reference,
        "payment_amount": round(float(payment_amount), 2),
        "payment_date": payment_date
    }

    return payment


if __name__ == "__main__":

    sample_payment = generate_payment(
        order_id=1,
        payment_amount=2500.00,
        order_status="Delivered"
    )

    print(sample_payment)