from python.database import get_connection
from python.generators.inventory_transaction_generator import (
    generate_inventory_transaction
)
from python.loaders.inventory_transaction_loader import (
    load_inventory_transaction
)

TRANSACTIONS_PER_INVENTORY = 5


def get_inventory_ids():
    """
    Fetch all inventory IDs.
    """

    connection = get_connection()
    cursor = connection.cursor()

    try:

        cursor.execute("""
            SELECT inventory_id
            FROM inventory
            ORDER BY inventory_id
        """)

        return cursor.fetchall()

    finally:

        cursor.close()
        connection.close()


def run_pipeline():

    print("=" * 60)
    print("Inventory Transaction Pipeline Started")
    print("=" * 60)

    inventory_records = get_inventory_ids()

    print(f"Inventory Records Found : {len(inventory_records)}")

    loaded = 0

    for inventory in inventory_records:

        inventory_id = inventory[0]

        for _ in range(TRANSACTIONS_PER_INVENTORY):

            transaction = generate_inventory_transaction(
                inventory_id
            )

            load_inventory_transaction(transaction)

            loaded += 1

            if loaded % 500 == 0:
                print(f"{loaded} transactions loaded...")

    print("=" * 60)
    print("Pipeline Completed Successfully")
    print(f"Total Transactions Loaded : {loaded}")
    print("=" * 60)


if __name__ == "__main__":
    run_pipeline()