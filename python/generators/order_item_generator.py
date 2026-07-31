import random


def generate_order_item(order_id, product_id, unit_price):
    """
    Generate one realistic order item.
    """

    quantity = random.randint(1, 5)

    discount_amount = round(
        unit_price * quantity * random.uniform(0, 0.15),
        2
    )

    taxable_amount = (
        unit_price * quantity
    ) - discount_amount

    tax_amount = round(
        taxable_amount * random.uniform(0.05, 0.18),
        2
    )

    line_total = round(
        taxable_amount + tax_amount,
        2
    )

    order_item = {
        "order_id": order_id,
        "product_id": product_id,
        "unit_price": unit_price,
        "discount_amount": discount_amount,
        "tax_amount": tax_amount,
        "line_total": line_total
    }

    return order_item


if __name__ == "__main__":

    sample_item = generate_order_item(
        order_id=1,
        product_id=1,
        unit_price=999.99
    )

    print(sample_item)