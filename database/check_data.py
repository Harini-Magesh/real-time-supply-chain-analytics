import sqlite3
import pandas as pd

conn = sqlite3.connect("supply_chain.db")

df = pd.read_sql("SELECT * FROM orders", conn)

print(df.head())