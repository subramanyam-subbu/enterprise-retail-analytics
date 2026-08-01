import random
from faker import Faker

fake = Faker("en_IN")

ADDRESS_TYPES = [
    "Home",
    "Office",
    "Other"
]


def generate_customer_address(customer_id):
    """
    Generate one customer address.
    """

    address = {
        "customer_id": customer_id,
        "address_type": random.choices(
            ADDRESS_TYPES,
            weights=[70, 20, 10],
            k=1
        )[0],
        "address_line1": fake.street_address(),
        "address_line2": f"Flat {random.randint(101, 1200)}",
        "landmark": fake.street_name(),
        "city": fake.city(),
        "state": fake.state(),
        "country": "India",
        "pincode": fake.postcode(),
        "is_default": random.choices(
            [1, 0],
            weights=[80, 20],
            k=1
        )[0]
    }

    return address


if __name__ == "__main__":

    sample = generate_customer_address(1)

    print(sample)