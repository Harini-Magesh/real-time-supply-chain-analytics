from faker import Faker
import random
import uuid
import json
import time

fake = Faker()

while True:

    order = {
        "order_id": str(uuid.uuid4()),
        "customer_id": str(uuid.uuid4()),
        "warehouse_id": random.choice(["WH001", "WH002", "WH003"]),
        "product_id": random.choice(["P100", "P200", "P300"]),
        "quantity": random.randint(1, 5),
        "price": round(random.uniform(100, 5000), 2),
        "status": random.choice([
            "PLACED",
            "SHIPPED",
            "DELIVERED",
            "CANCELLED"
        ]),
        "timestamp": fake.date_time_this_year().strftime("%Y-%m-%d %H:%M:%S")
    }

    print(json.dumps(order, indent=4))

    print("-----------")

    time.sleep(2)