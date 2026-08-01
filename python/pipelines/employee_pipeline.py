from python.database import get_connection
from python.generators.employee_generator import generate_employee
from python.loaders.employee_loader import load_employee

EMPLOYEES_PER_DEPARTMENT = 10


def get_departments():
    """
    Fetch all department IDs.
    """

    connection = get_connection()
    cursor = connection.cursor()

    try:
        cursor.execute("""
            SELECT department_id
            FROM departments
            ORDER BY department_id
        """)

        return cursor.fetchall()

    finally:
        cursor.close()
        connection.close()


def run_pipeline():

    print("=" * 60)
    print("Employee Pipeline Started")
    print("=" * 60)

    departments = get_departments()

    print(f"Departments Found : {len(departments)}")

    loaded = 0

    for department in departments:

        department_id = department[0]

        for _ in range(EMPLOYEES_PER_DEPARTMENT):

            employee = generate_employee(department_id)

            load_employee(employee)

            loaded += 1

            if loaded % 10 == 0:
                print(f"{loaded} employees loaded...")

    print("=" * 60)
    print("Pipeline Completed Successfully")
    print(f"Total Employees Loaded : {loaded}")
    print("=" * 60)


if __name__ == "__main__":
    run_pipeline()
    