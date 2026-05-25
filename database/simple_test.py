import psycopg2

try:
    conn = psycopg2.connect(
        host="127.0.0.1",
        port="5433",
        dbname="supply_chain_db",
        user="postgres"
    )

    print("CONNECTED SUCCESSFULLY")

    conn.close()

except Exception as e:
    print(e)