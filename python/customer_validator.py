valid_genders = ["Male","Female","Other"]

def validate_customer(customer):
    errors = []

    if not customer.get("first_name"):
        errors.append("first name is missing")

    if not customer.get("last_name"):
        errors.append("Last name is missing")

    if not customer.get("email"):
        errors.append("Email is missing")
    
    if not customer.get("phone_number"):
        errors.append("phone number is missing")

    if customer.get("gender") not in valid_genders:
        errors.append("Invalid Gender")

    if customer.get("country") != "India":
        errors.append("Invalid Country")
    
    return len(errors) == 0, errors