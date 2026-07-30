from python.database import get_connection


def load_products(products):
    """
    Insert generated product records into the products table.
    """

    connection = get_connection()
    cursor = connection.cursor()

    insert_query = """
        INSERT INTO products (
            product_name,
            product_sku,
            category_id,
            brand_id,
            supplier_id,
            unit_price,
            cost_price,
            stock_quantity,
            reorder_level,
            product_status
        )
        VALUES (
            %s, %s, %s, %s, %s,
            %s, %s, %s, %s, %s
        )
    """

    try:
        for product in products:

            values = (
                product["product_name"],
                product["product_sku"],
                product["category_id"],
                product["brand_id"],
                product["supplier_id"],
                product["unit_price"],
                product["cost_price"],
                product["stock_quantity"],
                product["reorder_level"],
                product["product_status"]
            )

            cursor.execute(insert_query, values)

        connection.commit()

        print(f"Successfully loaded {len(products)} products.")

    except Exception as e:

        connection.rollback()
        print("Error while loading products:", e)
        raise

    finally:

        cursor.close()
        connection.close()