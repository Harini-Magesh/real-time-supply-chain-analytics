import pg8000

try:
    conn = pg8000.connect(
        user="postgres",
        password="postgres",
        host="127.0.0.1",
        port=5433,
        database="supply_chain_db"
    )

    print("SUCCESS: Connected to PostgreSQL")

    conn.close()

except Exception as e:
    print("ERROR:")
    print(e)