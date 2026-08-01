from python.database import get_connection


def load_employee(employee):
    """
    Insert one employee into the employees table.
    """

    connection = get_connection()
    cursor = connection.cursor()

    insert_query = """
        INSERT INTO employees (
            department_id,
            first_name,
            last_name,
            email,
            phone_number,
            designation,
            hire_date,
            salary,
            manager_id,
            employment_status
        )
        VALUES (
            %s, %s, %s, %s, %s,
            %s, %s, %s, %s, %s
        )
    """

    values = (
        employee["department_id"],
        employee["first_name"],
        employee["last_name"],
        employee["email"],
        employee["phone_number"],
        employee["designation"],
        employee["hire_date"],
        employee["salary"],
        employee["manager_id"],
        employee["employment_status"]
    )

    try:
        cursor.execute(insert_query, values)
        connection.commit()

    except Exception as e:
        connection.rollback()
        print(f"Error loading employee: {e}")
        raise

    finally:
        cursor.close()
        connection.close()