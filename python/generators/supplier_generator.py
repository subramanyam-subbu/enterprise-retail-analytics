import random
from faker import Faker

fake = Faker("en_IN")

PAYMENT_TERMS = [
    "Advance",
    "15 Days",
    "30 Days",
    "45 Days",
    "60 Days"
]

SUPPLIER_STATUS = [
    "Active",
    "Inactive",
    "Blocked"
]

COMPANY_SUFFIXES = [
    "Traders",
    "Distributors",
    "Enterprises",
    "Industries",
    "Solutions",
    "Supplies",
    "Corporation",
    "Retail Pvt Ltd",
    "Wholesale Pvt Ltd",
    "Manufacturing Pvt Ltd"
]


def generate_gst():
    """
    Generate a fake GST number.
    """

    state_code = str(random.randint(10, 38)).zfill(2)

    pan = fake.bothify(
        text="?????####?"
    ).upper()

    return f"{state_code}{pan}1Z5"


def generate_supplier():
    """
    Generate one supplier record.
    """

    company_name = (
        fake.company() +
        " " +
        random.choice(COMPANY_SUFFIXES)
    )

    supplier = {
        "supplier_name": company_name,
        "contact_person": fake.name(),
        "email": fake.unique.company_email(),
        "phone": fake.unique.msisdn()[:10],
        "country": "India",
        "state": fake.state(),
        "city": fake.city(),
        "gst_number": generate_gst(),
        "payment_terms": random.choice(
            PAYMENT_TERMS
        ),
        "supplier_status": random.choices(
            SUPPLIER_STATUS,
            weights=[85, 10, 5],
            k=1
        )[0]
    }

    return supplier


if __name__ == "__main__":

    supplier = generate_supplier()

    print(supplier)