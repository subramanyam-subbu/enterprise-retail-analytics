from generators.customer_generator import generate_customer
from validators.customer_validator import validate_customer
from loaders.customer_loader import load_customer
from pipelines.customer_pipeline import run_customer_pipeline


def main():
    run_customer_pipeline()


if __name__ == "__main__":
    main()