"""
customer_pipeline.py

Customer ETL pipeline:
Generate → Validate → Load
"""

from generators.customer_generator import generate_customer
from validators.customer_validator import validate_customer
from loaders.customer_loader import load_customers


def run_customer_pipeline(batch_size: int = 100):
    """
    Generate, validate and load customers in batches.

    Parameters:
        batch_size: Number of customers generated per batch.
    """

    print("\n====================================")
    print("CUSTOMER ETL PIPELINE")
    print("====================================")

    customers = []
    rejected_customers = []

    # Generate customers
    for _ in range(batch_size):

        customer = generate_customer()

        is_valid, errors = validate_customer(customer)

        if is_valid:
            customers.append(customer)
        else:
            rejected_customers.append(
                {
                    "customer": customer,
                    "errors": errors
                }
            )

    print(f"\nGenerated Customers : {batch_size}")
    print(f"Valid Customers     : {len(customers)}")
    print(f"Rejected Customers  : {len(rejected_customers)}")

    # Load valid customers
    if customers:

        success = load_customers(customers)

        if success:
            print("\n✅ Customer batch loaded successfully.")
        else:
            print("\n❌ Customer batch loading failed.")

    else:
        print("\n❌ No valid customers available for loading.")

    # Rejected records
    if rejected_customers:

        print("\nRejected Customer Details:")

        for rejected in rejected_customers:
            print(
                rejected["errors"]
            )