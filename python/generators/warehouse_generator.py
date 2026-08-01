import random

WAREHOUSES = [
    ("Chennai Central Warehouse", "WH-CHN-001", "Chennai", "Tamil Nadu"),
    ("Bangalore Distribution Center", "WH-BLR-001", "Bangalore", "Karnataka"),
    ("Hyderabad Fulfillment Center", "WH-HYD-001", "Hyderabad", "Telangana"),
    ("Mumbai Logistics Hub", "WH-MUM-001", "Mumbai", "Maharashtra"),
    ("Delhi Regional Warehouse", "WH-DEL-001", "New Delhi", "Delhi"),
    ("Kolkata Supply Center", "WH-KOL-001", "Kolkata", "West Bengal"),
    ("Pune Storage Facility", "WH-PUN-001", "Pune", "Maharashtra"),
    ("Ahmedabad Distribution Hub", "WH-AHM-001", "Ahmedabad", "Gujarat"),
    ("Coimbatore Warehouse", "WH-CBE-001", "Coimbatore", "Tamil Nadu"),
    ("Vijayawada Fulfillment Center", "WH-VJA-001", "Vijayawada", "Andhra Pradesh"),
]

STATUSES = [
    "Active",
    "Inactive"
]


def generate_warehouse(index):
    """
    Generate one warehouse record.
    """

    warehouse = WAREHOUSES[index]

    return {
        "warehouse_name": warehouse[0],
        "warehouse_code": warehouse[1],
        "city": warehouse[2],
        "state": warehouse[3],
        "country": "India",
        "warehouse_status": random.choices(
            STATUSES,
            weights=[90, 10],
            k=1
        )[0]
    }


if __name__ == "__main__":

    for i in range(len(WAREHOUSES)):
        print(generate_warehouse(i))