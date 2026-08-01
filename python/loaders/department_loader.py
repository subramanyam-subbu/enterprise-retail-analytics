from python.database import get_connection


def load_department(department):
    """
    Insert one department into the departments table.
    """

    connection = get_connection()
    cursor = connection.cursor()

    insert_query = """
        INSERT INTO departments (
            department_name,
            department_code,
            manager_name,
            department_status
        )
        VALUES (
            %s, %s, %s, %s
        )
    """

    values = (
        department["department_name"],
        department["department_code"],
        department["manager_name"],
        department["department_status"]
    )

    try:
        cursor.execute(insert_query, values)
        connection.commit()

    except Exception as e:
        connection.rollback()
        print(f"Error loading department: {e}")
        raise

    finally:
        cursor.close()
        connection.close()