from python.database import get_connection


def load_order_items(order_items):
    """
    Insert generated order items into the order_items table.
    """

    connection = get_connection()
    cursor = connection.cursor()

    insert_query = """
        INSERT INTO order_items (
            order_id,
            product_id,
            unit_price,
            discount_amount,
            tax_amount,
            line_total
        )
        VALUES (
            %s, %s, %s, %s, %s, %s
        )
    """

    values = (
        order_items["order_id"],
        order_items["product_id"],
        order_items["unit_price"],
        order_items["discount_amount"],
        order_items["tax_amount"],
        order_items["line_total"]
    )

    cursor.execute(insert_query, values)

    connection.commit()

    cursor.close()
    connection.close()