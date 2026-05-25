from faker import Faker
import random
import uuid
from datetime import datetime
import json
import time

# Create Faker object
fake = Faker()

# Warehouse IDs
warehouses = ["WH001", "WH002", "WH003", "WH004"]

# Product IDs
products = ["P100", "P200", "P300", "P400", "P500"]

# Order status
statuses = ["PLACED", "SHIPPED", "DELIVERED", "CANCELLED"]


# Function to generate fake order
def generate_order():

    order = {
        "order_id": str(uuid.uuid4()),

        "customer_id": str(uuid.uuid4()),

        "warehouse_id": random.choice(warehouses),

        "product_id": random.choice(products),

        "quantity": random.randint(1, 5),

        "price": round(random.uniform(100, 5000), 2),

        "status": random.choice(statuses),

        "timestamp": datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    }

    return order


# Continuous order generation
while True:

    fake_order = generate_order()

    # Print formatted JSON
    print(json.dumps(fake_order, indent=4))

    print("-" * 50)

    # Wait 2 seconds
    time.sleep(2)