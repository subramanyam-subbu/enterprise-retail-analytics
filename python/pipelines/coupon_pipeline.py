import random

from python.generators.coupon_generator import generate_coupon
from python.loaders.coupon_loader import load_coupon

TOTAL_COUPONS = 100
TOTAL_CAMPAIGNS = 10


def run_pipeline():
    """
    Generate and load coupon data.
    """

    print("=" * 60)
    print("Coupon Pipeline Started")
    print("=" * 60)

    loaded = 0

    for _ in range(TOTAL_COUPONS):

        campaign_id = random.randint(1, TOTAL_CAMPAIGNS)

        coupon = generate_coupon(campaign_id)

        load_coupon(coupon)

        loaded += 1

        if loaded % 20 == 0:
            print(f"{loaded} coupons loaded...")

    print("=" * 60)
    print("Pipeline Completed Successfully")
    print(f"Total Coupons Loaded : {loaded}")
    print("=" * 60)


if __name__ == "__main__":
    run_pipeline()