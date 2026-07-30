"""
customer_pipeline.py

Controls the customer ETL workflow:
Generate → Validate → Load
"""

from generators.customer_generator import generate_customer
from validators.customer_validator import validate_customer
from loaders.customer_loader import load_customer


def run_customer_pipeline():
    """
    Execute the customer ETL pipeline for one customer.
    """

    # Step 1: Generate customer
    customer = generate_customer()

    print("\nGenerated Customer")
    print("----------------------")
    print(customer)

    # Step 2: Validate customer
    is_valid, errors = validate_customer(customer)

    if not is_valid:

        print("\n❌ Validation Failed")

        for error in errors:
            print(f"- {error}")

        return False

    print("\n✅ Validation Passed")

    # Step 3: Load customer
    inserted = load_customer(customer)

    if inserted:
        print("\n✅ Customer ETL Completed Successfully")
        return True

    print("\n❌ Customer ETL Failed")
    return False