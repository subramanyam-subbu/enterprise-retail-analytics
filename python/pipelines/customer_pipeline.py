"""
customer_pipeline.py

Customer ETL pipeline:

Generate
    ↓
Validate
    ↓
Duplicate Check
    ↓
Load
    ↓
Metrics
"""

from generators.customer_generator import generate_customer
from validators.customer_validator import validate_customer
from validators.duplicate_checker import (
    find_database_duplicates,
    find_batch_duplicates
)
from loaders.customer_loader import load_customers
from utils.error_logger import log_rejected_customer
from utils.etl_metrics import ETLMetrics


def run_customer_pipeline(batch_size: int = 100):

    metrics = ETLMetrics(
        pipeline_name="Customer ETL"
    )

    metrics.start()

    print("\n====================================")
    print("CUSTOMER ETL PIPELINE")
    print("====================================")

    customers = []

    rejected_count = 0
    duplicate_count = 0

    # ---------------------------------
    # 1. Generate + Validate
    # ---------------------------------

    for _ in range(batch_size):

        customer = generate_customer()

        metrics.generated += 1

        is_valid, errors = validate_customer(
            customer
        )

        if is_valid:

            customers.append(customer)

            metrics.valid += 1

        else:

            rejected_count += 1

            metrics.rejected += 1

            log_rejected_customer(
                customer,
                errors
            )

    print(
        f"\nGenerated Customers : "
        f"{metrics.generated}"
    )

    print(
        f"Valid Customers     : "
        f"{metrics.valid}"
    )

    print(
        f"Rejected Customers  : "
        f"{metrics.rejected}"
    )

    # ---------------------------------
    # 2. Batch Duplicate Detection
    # ---------------------------------

    batch_duplicates = find_batch_duplicates(
        customers
    )

    if batch_duplicates:

        duplicate_count += len(
            batch_duplicates
        )

        metrics.duplicates += len(
            batch_duplicates
        )

        for customer in batch_duplicates:

            log_rejected_customer(
                customer,
                ["Duplicate customer within batch"]
            )

        duplicate_emails = {
            customer["email"]
            for customer in batch_duplicates
        }

        customers = [
            customer
            for customer in customers
            if customer["email"]
            not in duplicate_emails
        ]

    # ---------------------------------
    # 3. Database Duplicate Detection
    # ---------------------------------

    database_duplicates = find_database_duplicates(
        customers
    )

    if database_duplicates:

        duplicate_count += len(
            database_duplicates
        )

        metrics.duplicates += len(
            database_duplicates
        )

        for customer in database_duplicates:

            log_rejected_customer(
                customer,
                ["Customer already exists in database"]
            )

        duplicate_emails = {
            customer["email"]
            for customer in database_duplicates
        }

        customers = [
            customer
            for customer in customers
            if customer["email"]
            not in duplicate_emails
        ]

    # ---------------------------------
    # 4. Load
    # ---------------------------------

    if customers:

        success = load_customers(
            customers
        )

        if success:

            metrics.loaded = len(
                customers
            )

            print(
                "\n✅ Customer batch loaded successfully."
            )

        else:

            print(
                "\n❌ Customer batch loading failed."
            )

    else:

        print(
            "\n❌ No customers available for loading."
        )

    # ---------------------------------
    # 5. Finish Metrics
    # ---------------------------------

    metrics.finish()

    metrics.print_report()