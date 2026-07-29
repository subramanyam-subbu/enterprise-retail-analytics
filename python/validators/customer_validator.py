"""
customer_validator.py

Validates customer records before loading them into MySQL.
"""

from typing import Dict, List, Tuple

VALID_GENDERS = ["Male", "Female", "Other"]
VALID_COUNTRY = "India"


def validate_customer(customer: Dict) -> Tuple[bool, List[str]]:
    """
    Validate a single customer record.

    Parameters:
        customer (dict): Customer record

    Returns:
        tuple:
            (True, []) if valid
            (False, [errors]) if invalid
    """

    errors = []

    # First Name
    if not customer.get("first_name"):
        errors.append("First name is required.")

    # Last Name
    if not customer.get("last_name"):
        errors.append("Last name is required.")

    # Email
    email = customer.get("email", "")

    if "@" not in email:
        errors.append("Invalid email address.")

    # Phone Number
    phone = str(customer.get("phone_number", ""))

    if not phone.isdigit() or len(phone) != 10:
        errors.append("Phone number must contain exactly 10 digits.")

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