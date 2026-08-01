import random
from datetime import date, timedelta

DISCOUNT_TYPES = [
    "Percentage",
    "Flat Amount",
    "Free Shipping"
]

COUPON_STATUS = [
    "Active",
    "Inactive",
    "Expired"
]


def generate_coupon(campaign_id):
    """
    Generate one coupon.
    """

    valid_from = date.today() - timedelta(
        days=random.randint(0, 90)
    )

    valid_to = valid_from + timedelta(
        days=random.randint(30, 180)
    )

    discount_type = random.choice(DISCOUNT_TYPES)

    if discount_type == "Percentage":
        discount_value = random.choice([5, 10, 15, 20, 25, 30])
        maximum_discount = random.choice(
            [250, 500, 750, 1000]
        )

    elif discount_type == "Flat Amount":
        discount_value = random.choice(
            [100, 200, 300, 500, 1000]
        )
        maximum_discount = None

    else:
        discount_value = 0
        maximum_discount = None

    coupon = {
        "campaign_id": campaign_id,
        "coupon_code": f"SAVE{random.randint(10000,99999)}",
        "discount_type": discount_type,
        "discount_value": discount_value,
        "minimum_order_amount": random.choice(
            [500, 1000, 2000, 5000]
        ),
        "maximum_discount": maximum_discount,
        "valid_from": valid_from,
        "valid_to": valid_to,
        "usage_limit": random.randint(100, 5000),
        "coupon_status": random.choices(
            COUPON_STATUS,
            weights=[80, 10, 10],
            k=1
        )[0]
    }

    return coupon


if __name__ == "__main__":

    sample = generate_coupon(1)

    print(sample)