import random
from datetime import date, timedelta
from faker import Faker

fake = Faker("en_IN")

DESIGNATIONS = [
    "Sales Executive",
    "Sales Manager",
    "Data Analyst",
    "Business Analyst",
    "Software Engineer",
    "Senior Software Engineer",
    "HR Executive",
    "HR Manager",
    "Finance Executive",
    "Finance Manager",
    "Warehouse Executive",
    "Warehouse Manager",
    "Inventory Analyst",
    "Procurement Executive",
    "Customer Support Executive",
    "Operations Executive",
    "QA Engineer",
    "QA Lead",
    "Marketing Executive",
    "Marketing Manager"
]

EMPLOYMENT_STATUS = [
    "Active",
    "Inactive",
    "Resigned"
]


def generate_employee(department_id):
    """
    Generate one employee record.
    """

    first_name = fake.first_name()
    last_name = fake.last_name()

    hire_date = date.today() - timedelta(
        days=random.randint(30, 3650)
    )

    employee = {
        "department_id": department_id,
        "first_name": first_name,
        "last_name": last_name,
        "email": fake.unique.email(),
        "phone_number": fake.unique.msisdn()[:10],
        "designation": random.choice(DESIGNATIONS),
        "hire_date": hire_date,
        "salary": round(random.uniform(25000, 180000), 2),
        "manager_id": None,
        "employment_status": random.choices(
            EMPLOYMENT_STATUS,
            weights=[85, 5, 10],
            k=1
        )[0]
    }

    return employee


if __name__ == "__main__":

    sample = generate_employee(1)

    print(sample)