"""
customer_validator.py

Validates customer records before loading them into MySQL.
"""

import re
from typing import Dict, List, Tuple


VALID_GENDERS = ["Male", "Female", "Other"]
VALID_COUNTRY = "India"


def validate_customer(customer: Dict) -> Tuple[bool, List[str]]:
    """
    Validate a single customer record.

    Returns:
        (True, []) if valid
        (False, errors) if invalid
    """

    errors = []

    # First name
    first_name = customer.get("first_name")

    if not first_name or not str(first_name).strip():
        errors.append("First name is required.")

    # Last name
    last_name = customer.get("last_name")

    if not last_name or not str(last_name).strip():
        errors.append("Last name is required.")

    # Email
    email = str(customer.get("email", "")).strip()

    email_pattern = r"^[^@\s]+@[^@\s]+\.[^@\s]+$"

    if not re.match(email_pattern, email):
        errors.append("Invalid email address.")

    # Phone
    phone = str(customer.get("phone_number", ""))

    if not phone.isdigit() or len(phone) != 10:
        errors.append(
            "Phone number must contain exactly 10 digits."
        )

    # Gender
    gender = customer.get("gender")

    if gender not in VALID_GENDERS:
        errors.append("Invalid gender.")

    # Country
    country = customer.get("country")

    if country != VALID_COUNTRY:
        errors.append("Country must be India.")

    if errors:
        return False, errors

    return True, []