from python.generators.product_generator import generate_product
from python.loaders.product_loader import load_products


def run_product_pipeline(number_of_products=100):
    """
    Generate and load products into the RDS database.
    """

    print(f"Generating {number_of_products} products...")

    products = []

    for _ in range(number_of_products):
        product = generate_product()
        products.append(product)

    print(f"Generated {len(products)} products.")

    print("Loading products into RDS...")

    load_products(products)

    print("Product pipeline completed successfully.")


if __name__ == "__main__":
    run_product_pipeline(100)