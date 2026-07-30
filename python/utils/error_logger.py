"""
error_logger.py

Stores rejected customer records for later investigation.
"""

import csv
import os
from datetime import datetime


ERROR_FILE = "logs/customer_rejected_records.csv"


def log_rejected_customer(customer: dict, errors: list[str]):
    """
    Save a rejected customer record to CSV.
    """

    os.makedirs("logs", exist_ok=True)

    file_exists = os.path.exists(ERROR_FILE)

    with open(
        ERROR_FILE,
        mode="a",
        newline="",
        encoding="utf-8"
    ) as file:

        writer = csv.writer(file)

        if not file_exists:
            writer.writerow(
                [
                    "timestamp",
                    "first_name",
                    "last_name",
                    "email",
                    "phone_number",
                    "errors"
                ]
            )

        writer.writerow(
            [
                datetime.now().isoformat(),
                customer.get("first_name"),
                customer.get("last_name"),
                customer.get("email"),
                customer.get("phone_number"),
                " | ".join(errors)
            ]
        )