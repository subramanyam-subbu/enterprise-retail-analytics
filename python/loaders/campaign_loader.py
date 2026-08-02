from python.database import get_connection


def load_campaign(campaign):
    """
    Insert one campaign into the campaigns table.
    """

    connection = get_connection()
    cursor = connection.cursor()

    insert_query = """
        INSERT INTO campaigns (
            campaign_name,
            campaign_type,
            start_date,
            end_date,
            campaign_budget,
            expected_revenue,
            campaign_status
        )
        VALUES (
            %s, %s, %s, %s,
            %s, %s, %s
        )
    """

    values = (
        campaign["campaign_name"],
        campaign["campaign_type"],
        campaign["start_date"],
        campaign["end_date"],
        campaign["campaign_budget"],
        campaign["expected_revenue"],
        campaign["campaign_status"]
    )

    try:
        cursor.execute(insert_query, values)
        connection.commit()

    except Exception as e:
        connection.rollback()
        print(f"Error loading campaign: {e}")
        raise

    finally:
        cursor.close()
        connection.close()