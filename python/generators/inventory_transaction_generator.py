import random
from datetime import datetime, timedelta


TRANSACTION_TYPES = [
    "Purchase",
    "Sale",
    "Return",
    "Transfer In",
    "Transfer Out",
    "Adjustment",
    "Damaged"
]

REFERENCE_MAPPING = {
    "Purchase": "Purchase Order",
    "Sale": "Sales Order",
    "Return": "Return",
    "Transfer In": "Warehouse Transfer",
    "Transfer Out": "Warehouse Transfer",
    "Adjustment": "Manual Adjustment",
    "Damaged": "Manual Adjustment"
}

REMARKS = {
    "Purchase": "Stock received from supplier.",
    "Sale": "Stock sold to customer.",
    "Return": "Customer returned product.",
    "Transfer In": "Stock transferred into warehouse.",
    "Transfer Out": "Stock transferred to another warehouse.",
    "Adjustment": "Inventory adjusted after audit.",
    "Damaged": "Damaged stock removed from inventory."
}


def generate_inventory_transaction(inventory_id):
    """
    Generate one inventory transaction.
    """

    transaction_type = random.choices(
        TRANSACTION_TYPES,
        weights=[25, 35, 8, 8, 8, 10, 6],
        k=1
    )[0]

    transaction = {
        "inventory_id": inventory_id,
        "transaction_type": transaction_type,
        "quantity": random.randint(1, 50),
        "reference_type": REFERENCE_MAPPING[transaction_type],
        "reference_id": f"REF-{random.randint(100000,999999)}",
        "remarks": REMARKS[transaction_type],
        "transaction_date": datetime.now() - timedelta(
            days=random.randint(0, 365)
        )
    }

    return transaction


if __name__ == "__main__":

    sample = generate_inventory_transaction(1)

    print(sample)