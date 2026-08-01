import random
from datetime import date, timedelta


TIERS = [
    "Bronze",
    "Silver",
    "Gold",
    "Platinum"
]

ACCOUNT_STATUS = [
    "Active",
    "Inactive",
    "Blocked"
]


def generate_loyalty_account(customer_id):
    """
    Generate one loyalty account.
    """

    join_date = date.today() - timedelta(
        days=random.randint(30, 2000)
    )

    last_activity_date = join_date + timedelta(
        days=random.randint(1, max(1, (date.today() - join_date).days))
    )

    lifetime_points = random.randint(500, 100000)

    points_balance = random.randint(
        0,
        lifetime_points
    )

    tier = random.choices(
        TIERS,
        weights=[50, 25, 18, 7],
        k=1
    )[0]

    account = {
        "customer_id": customer_id,
        "loyalty_number": f"LOY-{customer_id:06d}",
        "tier": tier,
        "points_balance": points_balance,
        "lifetime_points": lifetime_points,
        "join_date": join_date,
        "last_activity_date": last_activity_date,
        "account_status": random.choices(
            ACCOUNT_STATUS,
            weights=[90, 7, 3],
            k=1
        )[0]
    }

    return account


if __name__ == "__main__":

    sample = generate_loyalty_account(1)

    print(sample)