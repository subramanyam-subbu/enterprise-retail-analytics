import random
from datetime import datetime, timedelta


RETURN_REASONS = [
    "Damaged",
    "Wrong Item",
    "Defective",
    "Changed Mind",
    "Size Issue",
    "Late Delivery",
    "Other"
]

RETURN_STATUSES = [
    "Requested",
    "Approved",
    "Rejected",
    "Refunded"
]

REMARKS = [
    "Customer requested return",
    "Product received damaged",
    "Wrong product delivered",
    "Product not working properly",
    "Customer changed mind",
    "Size was not suitable",
    "Delivery was delayed",
    "Customer reported an issue"
]


def generate_return(
    order_item_id,
    customer_id,
    line_total
):
    """
    Generate one realistic return record.
    """

    return_reason = random.choice(
        RETURN_REASONS
    )

    return_status = random.choices(
        RETURN_STATUSES,
        weights=[15, 20, 10, 55],
        k=1
    )[0]

    # Refund only when the return is approved/refunded
    if return_status in ["Approved", "Refunded"]:
        refund_amount = round(
            line_total * random.uniform(0.80, 1.00),
            2
        )
    else:
        refund_amount = 0.00

    return_date = (
        datetime.now()
        - timedelta(days=random.randint(0, 365))
    )

    remarks = random.choice(REMARKS)

    return_record = {
        "order_item_id": order_item_id,
        "customer_id": customer_id,
        "return_reason": return_reason,
        "return_status": return_status,
        "refund_amount": refund_amount,
        "return_date": return_date,
        "remarks": remarks
    }

    return return_record


if __name__ == "__main__":

    sample_return = generate_return(
        order_item_id=1,
        customer_id=1,
        line_total=2500.00
    )

    print(sample_return)