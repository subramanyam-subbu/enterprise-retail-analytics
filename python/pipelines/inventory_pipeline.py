from python.database import get_connection
from python.generators.inventory_generator import generate_inventory
from python.loaders.inventory_loader import load_inventory


def get_warehouses():
    """
    Fetch all warehouse IDs.
    """
    connection = get_connection()
    cursor = connection.cursor()

    cursor.execute("""
        SELECT warehouse_id
        FROM warehouses
        ORDER BY warehouse_id
    """)

    warehouses = cursor.fetchall()

    cursor.close()
    connection.close()

    return warehouses


def get_products():
    """
    Fetch all product IDs.
    """
    connection = get_connection()
    cursor = connection.cursor()

    cursor.execute("""
        SELECT product_id
        FROM products
        ORDER BY product_id
    """)

    products = cursor.fetchall()

    cursor.close()
    connection.close()

    return products


def run_pipeline():

    print("=" * 60)
    print("Inventory Pipeline Started")
    print("=" * 60)

    warehouses = get_warehouses()
    products = get_products()

    print(f"Warehouses Found : {len(warehouses)}")
    print(f"Products Found   : {len(products)}")

    loaded = 0

    for warehouse in warehouses:

        warehouse_id = warehouse[0]

        for product in products:

            product_id = product[0]

            inventory = generate_inventory(
                warehouse_id,
                product_id
            )

            load_inventory(inventory)

            loaded += 1

            if loaded % 100 == 0:
                print(f"{loaded} inventory records loaded...")

    print("=" * 60)
    print("Pipeline Completed Successfully")
    print(f"Total Inventory Records Loaded : {loaded}")
    print("=" * 60)


if __name__ == "__main__":
    run_pipeline()