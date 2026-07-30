import random
from faker import Faker

fake = Faker("en_IN")

PRODUCT_CATEGORIES = [
    "Electronics",
    "Home Appliances",
    "Furniture",
    "Grocery",
    "Fashion",
    "Beauty",
    "Sports",
    "Books",
    "Toys",
    "Personal Care"
]

BRANDS = [
    "Samsung",
    "LG",
    "Sony",
    "Whirlpool",
    "Philips",
    "Nike",
    "Adidas",
    "Puma",
    "Prestige",
    "Havells",
    "Boat",
    "Levis",
    "Dell",
    "HP",
    "Apple"
]


def generate_product(category_id=None, brand_id=None):
    """
    Generate one realistic product record.
    """

    unit_price = round(random.uniform(100, 100000), 2)

    # Cost price should normally be lower than selling price
    cost_price = round(
        unit_price * random.uniform(0.50, 0.85),
        2
    )

    product = {
        "product_name": fake.catch_phrase(),
        "product_sku": fake.unique.bothify(
            text="SKU-####-????"
        ).upper(),
        "category_id": category_id or random.randint(1, 10),
        "brand_id": brand_id or random.randint(1, 15),
        "supplier_id": random.randint(1, 10),
        "unit_price": unit_price,
        "cost_price": cost_price,
        "stock_quantity": random.randint(0, 500),
        "reorder_level": random.randint(5, 50),
        "product_status": random.choices(
            ["Active", "Inactive", "Discontinued"],
            weights=[85, 10, 5],
            k=1
        )[0]
    }

    return product


if __name__ == "__main__":
    product = generate_product()
    print(product)