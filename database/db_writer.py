import sqlite3
from kafka import KafkaConsumer
import json
import logging

# Logging setup
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s'
)

# SQLite connection
conn = sqlite3.connect("supply_chain.db")

cursor = conn.cursor()

# Create table
cursor.execute("""
CREATE TABLE IF NOT EXISTS orders (
    order_id TEXT,
    customer_id TEXT,
    warehouse_id TEXT,
    product_id TEXT,
    quantity INTEGER,
    price REAL,
    status TEXT,
    timestamp TEXT
)
""")

conn.commit()

# Kafka Consumer
consumer = KafkaConsumer(
    'orders_topic',
    bootstrap_servers='localhost:9092',
    value_deserializer=lambda m: json.loads(m.decode('utf-8'))
)

logging.info("Kafka consumer started")

for message in consumer:

    try:

        data = message.value

        cursor.execute("""
        INSERT INTO orders VALUES (?, ?, ?, ?, ?, ?, ?, ?)
        """, (
            data['order_id'],
            data['customer_id'],
            data['warehouse_id'],
            data['product_id'],
            data['quantity'],
            data['price'],
            data['status'],
            data['timestamp']
        ))

        conn.commit()

        logging.info(f"Inserted order: {data['order_id']}")

    except Exception as e:

        logging.error(f"Pipeline error: {e}")