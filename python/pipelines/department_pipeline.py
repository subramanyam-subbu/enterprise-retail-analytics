from python.generators.department_generator import generate_department
from python.loaders.department_loader import load_department

TOTAL_DEPARTMENTS = 10


def run_pipeline():
    """
    Generate and load department data.
    """

    print("=" * 60)
    print("Department Pipeline Started")
    print("=" * 60)

    loaded = 0

    for index in range(TOTAL_DEPARTMENTS):

        department = generate_department(index)

        load_department(department)

        loaded += 1

        print(f"Department {loaded} loaded.")

    print("=" * 60)
    print("Pipeline Completed Successfully")
    print(f"Total Departments Loaded : {loaded}")
    print("=" * 60)


if __name__ == "__main__":
    run_pipeline()