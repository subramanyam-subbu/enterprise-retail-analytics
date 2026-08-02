import random
from datetime import datetime, timedelta


def generate_coupon_usage(
    coupon_id,
    customer_id,
    order_id
):
    """
    Generate one coupon usage record.
    """

    discount_amount = round(
        random.uniform(50, 1000),
        2
    )

    redeemed_at = datetime.now() - timedelta(
        days=random.randint(1, 180),
        hours=random.randint(0, 23),
        minutes=random.randint(0, 59)
    )

    return {
        "coupon_id": coupon_id,
        "customer_id": customer_id,
        "order_id": order_id,
        "discount_amount": discount_amount,
        "redeemed_at": redeemed_at
    }


if __name__ == "__main__":

    sample = generate_coupon_usage(
        coupon_id=1,
        customer_id=1,
        order_id=1
    )

    print(sample)