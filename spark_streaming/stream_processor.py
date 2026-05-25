from pyspark.sql import SparkSession
from pyspark.sql.functions import *
from pyspark.sql.types import *

# Create Spark Session
spark = SparkSession.builder \
    .appName("SupplyChainStreaming") \
    .master("local[*]") \
    .config(
        "spark.jars.packages",
        "org.apache.spark:spark-sql-kafka-0-10_2.12:3.5.1"
    ) \
    .getOrCreate()

spark.sparkContext.setLogLevel("WARN")

# Define Schema
schema = StructType([
    StructField("order_id", StringType(), True),
    StructField("customer_id", StringType(), True),
    StructField("warehouse_id", StringType(), True),
    StructField("product_id", StringType(), True),
    StructField("quantity", IntegerType(), True),
    StructField("price", DoubleType(), True),
    StructField("status", StringType(), True),
    StructField("timestamp", StringType(), True)
])

# Read stream from Kafka
df = spark.readStream \
    .format("kafka") \
    .option("kafka.bootstrap.servers", "localhost:9092") \
    .option("subscribe", "orders_topic") \
    .option("startingOffsets", "latest") \
    .load()

# Convert binary to string
json_df = df.selectExpr("CAST(value AS STRING)")

# Parse JSON
parsed_df = json_df.select(
    from_json(col("value"), schema).alias("data")
).select("data.*")

# Analytics
metrics_df = parsed_df.groupBy("warehouse_id") \
    .agg(
        count("order_id").alias("total_orders"),
        avg("price").alias("average_price"),
        sum("quantity").alias("total_quantity")
    )

# Output stream
query = metrics_df.writeStream \
    .outputMode("complete") \
    .format("console") \
    .option("truncate", False) \
    .option("checkpointLocation", "C:/tmp/spark-checkpoints") \
    .start()

query.awaitTermination()