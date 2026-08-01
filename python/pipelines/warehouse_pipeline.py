from python.generators.warehouse_generator import generate_warehouse
from python.loaders.warehouse_loader import load_warehouse


TOTAL_WAREHOUSES = 10


def run_pipeline():
    """
    Generate and load warehouse data.
    """

    print("=" * 60)
    print("Warehouse Pipeline Started")
    print("=" * 60)

    loaded = 0

    for index in range(TOTAL_WAREHOUSES):

        warehouse = generate_warehouse(index)

        load_warehouse(warehouse)

        loaded += 1

        print(f"Warehouse {loaded} loaded.")

    print("=" * 60)
    print(f"Pipeline Completed Successfully")
    print(f"Total Warehouses Loaded : {loaded}")
    print("=" * 60)


if __name__ == "__main__":
    run_pipeline()