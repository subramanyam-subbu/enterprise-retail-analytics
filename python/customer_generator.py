from faker import Faker 
import random
from datetime import datetime, timedelta

fake = Faker("en_IN")

Gender = ["Male","Female","Other"]
country = "India"

def generate_customer():
    """
        Generate Single Customer
    """
    customer = {
        "first_name": fake.first_name(),
        "last_name": fake.last_name(),
        "gender": random.choice(Gender),
        "email": fake.unique.email(),
        "phone_number": fake.unique.msisdn()[:10],
        "city": fake.city(),
        "state": fake.state(),
        "country": country
    }

    return customer

def generate_customers(number_of_customers):
    customers = []

    for _ in range(number_of_customers):
        customers.append(generate_customer())

    return customers

if __name__ == "__main__":
    customers = generate_customers(2)

    for i, customer in enumerate(customers,start=1):
        print(f"\nCustomer {i}")
        print("-"*50)

        for key,value in customer.items():
            print(f"{key:20}:{value}")
    
    