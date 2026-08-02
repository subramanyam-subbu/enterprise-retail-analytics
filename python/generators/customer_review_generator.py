import random
from datetime import datetime, timedelta


REVIEW_TITLES = [
    "Excellent Product",
    "Very Good",
    "Worth Buying",
    "Highly Recommended",
    "Good Value",
    "Average Quality",
    "Satisfied",
    "Not Bad",
    "Amazing Experience",
    "Could Be Better"
]

REVIEW_TEXTS = [
    "Excellent quality and fast delivery.",
    "Very happy with this purchase.",
    "Good value for the money.",
    "The product works exactly as expected.",
    "Packaging was excellent.",
    "Delivery was quick and hassle-free.",
    "Quality exceeded my expectations.",
    "Would definitely recommend this product.",
    "Satisfied with the purchase.",
    "Will buy again."
]


def generate_customer_review(
    customer_id,
    product_id,
    order_id
):
    """
    Generate one customer review.
    """

    rating = random.choices(
        [5, 4, 3, 2, 1],
        weights=[45, 30, 15, 7, 3],
        k=1
    )[0]

    review_date = datetime.now() - timedelta(
        days=random.randint(1, 180),
        hours=random.randint(0, 23),
        minutes=random.randint(0, 59)
    )

    return {
        "customer_id": customer_id,
        "product_id": product_id,
        "order_id": order_id,
        "rating": rating,
        "review_title": random.choice(REVIEW_TITLES),
        "review_text": random.choice(REVIEW_TEXTS),
        "is_verified_purchase": 1,
        "review_date": review_date
    }


if __name__ == "__main__":

    sample = generate_customer_review(
        customer_id=1,
        product_id=1,
        order_id=1
    )

    print(sample)