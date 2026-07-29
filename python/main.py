from generators.customer_generator import generate_customer
from validators.customer_validator import validate_customer
from loaders.customer_loader import load_customer


def main():

    customer = generate_customer()

    print("\nGenerated Customer")
    print(customer)

    is_valid, errors = validate_customer(customer)

    if not is_valid:

        print("\nValidation Failed")

        for error in errors:
            print(error)

        return

    print("\nValidation Passed")

    inserted = load_customer(customer)

    if inserted:
        print("ETL Completed Successfully")
    else:
        print("ETL Failed")


if __name__ == "__main__":
    main()