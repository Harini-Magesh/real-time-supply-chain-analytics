from kafka import KafkaProducer
from faker import Faker
import json
import uuid
import random
import time
from datetime import datetime

# Kafka Producer
producer = KafkaProducer(
    bootstrap_servers='localhost:9092',
    value_serializer=lambda v: json.dumps(v).encode('utf-8')
)

fake = Faker()

warehouses = ["WH001", "WH002", "WH003"]
products = ["P100", "P200", "P300", "P400"]
statuses = ["PLACED", "SHIPPED", "DELIVERED"]

# Generate fake order
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

# Continuous streaming
while True:

    order = generate_order()

    producer.send('orders_topic', value=order)

    print(f'Sent: {order}')

    time.sleep(2)