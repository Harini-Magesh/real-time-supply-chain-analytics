# Real-Time Supply Chain & Inventory Analytics Platform

## Project Overview

This project is a real-time supply chain analytics platform designed to simulate modern warehouse and logistics monitoring systems used in large-scale e-commerce and cloud-native environments.

The system streams live order events through Kafka, processes them using streaming architecture concepts, stores analytics data, and visualizes operational KPIs using an interactive dashboard.

The platform demonstrates:

- Real-time event streaming
- Distributed pipeline architecture
- Operational analytics
- Warehouse monitoring
- Dashboard visualization
- Event-driven system design
- Data engineering concepts

This project resembles simplified versions of analytics systems used in logistics and large-scale retail operations.

---

# Architecture

```text
Order Generator
      ↓
Kafka Producer
      ↓
Kafka Topic (orders_topic)
      ↓
Streaming Consumer
      ↓
SQLite Analytics Database
      ↓
Streamlit Dashboard
```

---

# High-Level Architecture

```text
                ┌─────────────────────┐
                │ Order Generator     │
                │ Fake Order Events   │
                └──────────┬──────────┘
                           │
                           ▼
                ┌─────────────────────┐
                │ Kafka Producer      │
                │ Real-Time Streaming │
                └──────────┬──────────┘
                           │
                           ▼
                ┌─────────────────────┐
                │ Kafka Topic         │
                │ orders_topic        │
                └──────────┬──────────┘
                           │
                           ▼
                ┌─────────────────────┐
                │ Analytics Consumer  │
                │ Event Processing    │
                └──────────┬──────────┘
                           │
                           ▼
                ┌─────────────────────┐
                │ SQLite Database     │
                │ Analytics Storage   │
                └──────────┬──────────┘
                           │
                           ▼
                ┌─────────────────────┐
                │ Streamlit Dashboard │
                │ Live Visualization  │
                └─────────────────────┘
```

---

# Tech Stack

| Layer | Technology |
|---|---|
| Language | Python |
| Streaming | Apache Kafka |
| Containerization | Docker |
| Data Processing | Python Consumers |
| Database | SQLite |
| Dashboard | Streamlit |
| Fake Data Generation | Faker |
| Version Control | Git & GitHub |

---

# Features

## Real-Time Order Streaming

- Generates live warehouse order events
- Streams events continuously into Kafka topics
- Simulates e-commerce operational traffic

---

## Warehouse Analytics

Tracks:

- Total Orders
- Revenue
- Warehouse Load
- Quantity Distribution
- Order Status
- Product Demand

---

## Dashboard Analytics

Interactive dashboard displaying:

- Live KPIs
- Warehouse performance
- Order distribution
- Revenue metrics
- Recent orders table
- Shipment status analytics

---

# Data Flow

## Step 1 — Order Generation

Fake order events are generated using:

- Faker
- Randomized product/warehouse logic

Generated fields:

- order_id
- customer_id
- warehouse_id
- product_id
- quantity
- price
- status
- timestamp

---

## Step 2 — Kafka Streaming

Orders are streamed into:

```text
orders_topic
```

using Kafka Producer APIs.

---

## Step 3 — Event Consumption

Kafka consumers continuously read events from:

```text
orders_topic
```

and process incoming streaming data.

---

## Step 4 — Analytics Storage

Processed events are inserted into SQLite database tables for analytics querying.

---

## Step 5 — Dashboard Visualization

Streamlit dashboard reads analytics data and displays:

- operational KPIs
- warehouse metrics
- revenue insights
- live order monitoring

---

# Project Structure

```text
real-time-supply-chain-analytics/
│
├── producer/
│   ├── order_generator.py
│   └── kafka_producer.py
│
├── spark_streaming/
│   └── stream_processor.py
│
├── database/
│   ├── db_writer.py
│   ├── check_data.py
│   └── schema.sql
│
├── dashboards/
│   └── app.py
│
├── docker/
│   └── docker-compose.yml
│
├── ml_layer/
│   └── train_model.py
│
├── aws/
│
├── supply_chain.db
│
└── README.md
```

---

# Setup Instructions

## 1. Clone Repository

```bash
git clone <repository-url>
cd real-time-supply-chain-analytics
```

---

## 2. Create Virtual Environment

```bash
python -m venv venv
```

Activate:

### Windows

```bash
venv\Scripts\activate
```

---

## 3. Install Dependencies

```bash
pip install faker kafka-python streamlit pandas sqlite3
```

---

## 4. Start Docker Containers

```bash
docker compose -f docker/docker-compose.yml up -d
```

---

## 5. Create Kafka Topic

```bash
docker exec -it kafka bash
```

Then:

```bash
kafka-topics --create \
--topic orders_topic \
--bootstrap-server localhost:9092
```

---

## 6. Run Kafka Producer

```bash
python producer/kafka_producer.py
```

---

## 7. Run Database Consumer

```bash
python database/db_writer.py
```

---

## 8. Launch Dashboard

```bash
streamlit run dashboards/app.py
```

---

# Dashboard Features

## KPI Metrics

- Total Orders
- Average Price
- Total Quantity
- Total Revenue

---

## Warehouse Analytics

Visualizes:

- Orders by warehouse
- Warehouse activity distribution
- Operational traffic

---

## Shipment Monitoring

Tracks:

- PLACED orders
- SHIPPED orders
- DELIVERED orders

---

## Live Operational Dashboard

Displays:

- Recent orders
- Real-time updates
- Analytics metrics
- Streaming event insights

---

# Future Improvements

## Planned Enhancements

### Spark Streaming Integration

- Real-time ETL pipelines
- Distributed stream processing

---

### AWS S3 Data Lake

- Historical analytics storage
- Cloud-native architecture

---

### Machine Learning Layer

Predict:

- shipment delays
- warehouse overload
- order spikes

---

### Grafana Integration

Advanced operational dashboards for:

- monitoring
- observability
- alerting systems

---

### Kubernetes Deployment

Container orchestration for scalable deployment.

---

# Screenshots

## Dashboard Overview

(Add screenshot here)

---

## Warehouse Analytics

(Add screenshot here)

---

## Recent Orders Table

(Add screenshot here)

---

# Learning Outcomes

This project demonstrates practical understanding of:

- Event-driven systems
- Streaming architecture
- Kafka pipelines
- Operational analytics
- Real-time dashboards
- Dockerized environments
- Data engineering workflows

---

# Resume Description

```text
Built a real-time supply chain analytics platform using Kafka, Docker, Python, SQLite, and Streamlit. Implemented live event streaming, operational analytics, warehouse monitoring, and dashboard visualization for real-time logistics insights.
```

---

# Author

Harini M

Data Engineering | Real-Time Analytics | Cloud & Streaming Systems
