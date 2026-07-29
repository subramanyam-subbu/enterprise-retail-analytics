from faker import Faker 
import random
from datetime import datetime,timedelta

fake = Faker("en_IN")

gender = ["Male", "Female", "Other"]
country = "India"

def generate_customer():
    customer = {
        "first_name":fake.first_name(),
        "last_name" : fake.last_name(),
        "gender" : random.choice(gender),
        "email" : fake.unique.email(),
        "phone_number":fake.unique.msisdn()[:10],
        "city":fake.city(),
        "state":fake.state(),
        "country":country
    }

    return customer

if __name__ =="__main__":
    customer = generate_customer()
    print(customer)