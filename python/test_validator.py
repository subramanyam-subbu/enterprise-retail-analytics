from customer_generator import generate_customer
from customer_validator import validate_customer


customer = generate_customer()

is_valid, errors = validate_customer(customer)

print("Customer")

print(customer)

print("\nValidation Result")

print(is_valid)

if errors:
    print(errors)
else:
    print("No validation errors")