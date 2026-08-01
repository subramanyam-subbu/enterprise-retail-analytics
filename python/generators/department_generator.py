import random

DEPARTMENTS = [
    {
        "department_name": "Sales",
        "department_code": "DEP-SAL",
        "manager_name": "Rahul Sharma"
    },
    {
        "department_name": "Marketing",
        "department_code": "DEP-MKT",
        "manager_name": "Priya Reddy"
    },
    {
        "department_name": "Finance",
        "department_code": "DEP-FIN",
        "manager_name": "Amit Verma"
    },
    {
        "department_name": "Human Resources",
        "department_code": "DEP-HR",
        "manager_name": "Neha Kapoor"
    },
    {
        "department_name": "Information Technology",
        "department_code": "DEP-IT",
        "manager_name": "Suresh Kumar"
    },
    {
        "department_name": "Operations",
        "department_code": "DEP-OPS",
        "manager_name": "Vikram Singh"
    },
    {
        "department_name": "Customer Support",
        "department_code": "DEP-CS",
        "manager_name": "Anjali Gupta"
    },
    {
        "department_name": "Procurement",
        "department_code": "DEP-PRC",
        "manager_name": "Ramesh Naidu"
    },
    {
        "department_name": "Logistics",
        "department_code": "DEP-LOG",
        "manager_name": "Kiran Rao"
    },
    {
        "department_name": "Quality Assurance",
        "department_code": "DEP-QA",
        "manager_name": "Deepak Mishra"
    }
]


def generate_department(index):
    """
    Generate one department record.
    """

    department = DEPARTMENTS[index]

    return {
        "department_name": department["department_name"],
        "department_code": department["department_code"],
        "manager_name": department["manager_name"],
        "department_status": random.choices(
            ["Active", "Inactive"],
            weights=[90, 10],
            k=1
        )[0]
    }


if __name__ == "__main__":

    for index in range(len(DEPARTMENTS)):
        print(generate_department(index))