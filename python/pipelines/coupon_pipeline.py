import random

from python.database import get_connection
from python.generators.coupon_generator import generate_coupon
from python.loaders.coupon_loader import load_coupon

TOTAL_COUPONS = 100


def get_campaign_ids():
    """
    Fetch all available campaign IDs from the database.
    """

    connection = get_connection()
    cursor = connection.cursor()

    cursor.execute("""
        SELECT campaign_id
        FROM campaigns
    """)

    campaign_ids = [row[0] for row in cursor.fetchall()]

    cursor.close()
    connection.close()

    return campaign_ids


def run_pipeline():

    print("=" * 60)
    print("Coupon Pipeline Started")
    print("=" * 60)

    campaign_ids = get_campaign_ids()

    if not campaign_ids:
        print("No campaigns found. Please run campaign_pipeline.py first.")
        return

    loaded = 0

    for _ in range(TOTAL_COUPONS):

        campaign_id = random.choice(campaign_ids)

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