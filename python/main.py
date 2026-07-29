from generators.customer_generator import generate_customer
from validators.customer_validator import validate_customer


def main():

    customer = generate_customer()

    print("\nGenerated Customer")
    print("----------------------")
    print(customer)

    is_valid, errors = validate_customer(customer)

    print("\nValidation Result")
    print("----------------------")
    print(f"Valid : {is_valid}")

    if errors:
        print("\nErrors")

        for error in errors:
            print(f"- {error}")
    else:
        print("No validation errors.")


if __name__ == "__main__":
    main()