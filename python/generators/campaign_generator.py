import random
from datetime import date, timedelta

CAMPAIGN_TYPES = [
    "Seasonal",
    "Festival",
    "Flash Sale",
    "Clearance",
    "Email",
    "Social Media"
]

CAMPAIGN_STATUS = [
    "Planned",
    "Active",
    "Completed",
    "Cancelled"
]

CAMPAIGN_NAMES = [
    "Summer Sale",
    "Diwali Bonanza",
    "Black Friday",
    "Christmas Deals",
    "New Year Blast",
    "Mega Electronics Sale",
    "Fashion Fiesta",
    "Weekend Specials",
    "Republic Day Offers",
    "Customer Appreciation Week"
]


def generate_campaign(index):

    start_date = date.today() - timedelta(
        days=random.randint(0, 180)
    )

    end_date = start_date + timedelta(
        days=random.randint(15, 60)
    )

    budget = random.randint(100000, 1000000)

    expected_revenue = budget * random.uniform(2.5, 6.0)

    return {
        "campaign_name": CAMPAIGN_NAMES[index],
        "campaign_type": random.choice(CAMPAIGN_TYPES),
        "start_date": start_date,
        "end_date": end_date,
        "campaign_budget": round(budget, 2),
        "expected_revenue": round(expected_revenue, 2),
        "campaign_status": random.choices(
            CAMPAIGN_STATUS,
            weights=[10, 50, 35, 5],
            k=1
        )[0]
    }


if __name__ == "__main__":

    for i in range(len(CAMPAIGN_NAMES)):
        print(generate_campaign(i))