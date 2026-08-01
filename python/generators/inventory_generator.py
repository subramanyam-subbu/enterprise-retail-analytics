import random
from datetime import datetime


def generate_inventory(warehouse_id, product_id):
    """
    Generate one inventory record.
    """

    available_quantity = random.randint(20, 500)
    reserved_quantity = random.randint(0, 20)
    damaged_quantity = random.randint(0, 10)

    reorder_level = random.choice([
        10,
        20,
        30,
        40,
        50
    ])

    inventory = {
        "warehouse_id": warehouse_id,
        "product_id": product_id,
        "available_quantity": available_quantity,
        "reserved_quantity": reserved_quantity,
        "damaged_quantity": damaged_quantity,
        "reorder_level": reorder_level,
        "last_stock_update": datetime.now()
    }

    return inventory


if __name__ == "__main__":

    sample = generate_inventory(
        warehouse_id=1,
        product_id=1
    )

    print(sample)