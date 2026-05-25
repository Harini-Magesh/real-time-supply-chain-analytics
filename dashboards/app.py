import streamlit as st
import pandas as pd
import sqlite3

st.title("Real-Time Supply Chain Analytics")

# Connect SQLite
conn = sqlite3.connect("supply_chain.db")

# Read data
df = pd.read_sql("SELECT * FROM orders", conn)

# Metrics
total_orders = len(df)
average_price = round(df['price'].mean(), 2)
total_quantity = df['quantity'].sum()
total_revenue = round(df['price'].sum(), 2)

# Dashboard metrics
st.metric("Total Orders", total_orders)
st.metric("Average Price", average_price)
st.metric("Total Quantity", total_quantity)
st.metric("Total Revenue", total_revenue)
# Convert timestamp
df['timestamp'] = pd.to_datetime(df['timestamp'])

# Orders over time
orders_trend = df.groupby(
    df['timestamp'].dt.strftime('%H:%M:%S')
).size()

st.subheader("Live Order Trend")

st.line_chart(orders_trend)

# Warehouse analytics
warehouse_df = df.groupby("warehouse_id").size().reset_index(name="orders")

st.subheader("Orders by Warehouse")
st.bar_chart(
    warehouse_df.set_index("warehouse_id")
)

# Recent orders
st.subheader("Recent Orders")
st.dataframe(df.tail(10))
status_counts = df['status'].value_counts()

st.subheader("Shipment Status Distribution")

st.bar_chart(status_counts)

product_counts = df['product_id'].value_counts()

st.subheader("Top Products")

st.bar_chart(product_counts)

inventory_data = {
    "Product": ["P100", "P200", "P300", "P400"],
    "Stock": [5, 40, 8, 22]
}

inventory_df = pd.DataFrame(inventory_data)

low_stock = inventory_df[inventory_df['Stock'] < 10]

st.subheader("Low Stock Alerts")

st.dataframe(low_stock)