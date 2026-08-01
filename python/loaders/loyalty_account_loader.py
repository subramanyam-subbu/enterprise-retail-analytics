from python.database import get_connection


def load_loyalty_account(account):
    """
    Insert one loyalty account into the loyalty_accounts table.
    """

    connection = get_connection()
    cursor = connection.cursor()

    insert_query = """
        INSERT INTO loyalty_accounts (
            customer_id,
            loyalty_number,
            tier,
            points_balance,
            lifetime_points,
            join_date,
            last_activity_date,
            account_status
        )
        VALUES (
            %s, %s, %s, %s,
            %s, %s, %s, %s
        )
    """

    values = (
        account["customer_id"],
        account["loyalty_number"],
        account["tier"],
        account["points_balance"],
        account["lifetime_points"],
        account["join_date"],
        account["last_activity_date"],
        account["account_status"]
    )

    try:
        cursor.execute(insert_query, values)
        connection.commit()

    except Exception as e:
        connection.rollback()
        print(f"Error loading loyalty account: {e}")
        raise

    finally:
        cursor.close()
        connection.close()  