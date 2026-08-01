from python.generators.supplier_generator import generate_supplier
from python.loaders.supplier_loader import load_supplier

TOTAL_SUPPLIERS = 20


def run_pipeline():
    """
    Generate and load supplier data.
    """

    print("=" * 60)
    print("Supplier Pipeline Started")
    print("=" * 60)

    loaded = 0

    for _ in range(TOTAL_SUPPLIERS):

        supplier = generate_supplier()

        load_supplier(supplier)

        loaded += 1

        print(f"Supplier {loaded} loaded.")

    print("=" * 60)
    print("Pipeline Completed Successfully")
    print(f"Total Suppliers Loaded : {loaded}")
    print("=" * 60)


if __name__ == "__main__":
    run_pipeline()