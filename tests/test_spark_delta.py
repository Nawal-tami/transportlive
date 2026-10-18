from pyspark.sql import SparkSession

spark = SparkSession.builder \
    .appName("TransportLive-Test") \
    .master("local[2]") \
    .config("spark.driver.memory", "1g") \
    .config("spark.sql.extensions", "io.delta.sql.DeltaSparkSessionExtension") \
    .config("spark.sql.catalog.spark_catalog", "org.apache.spark.sql.delta.catalog.DeltaCatalog") \
    .config("spark.jars.packages", "io.delta:delta-spark_2.12:3.2.1") \
    .getOrCreate()

data = [("bus_39", "stop_678", 300), ("bus_66", "stop_123", -60)]
df = spark.createDataFrame(data, ["trip_id", "stop_id", "delay"])
print("=== DataFrame cree ===")
df.show()

df.write.format("delta").mode("overwrite").save("data/bronze/test_table")
print("=== Ecriture Delta OK ===")

df_read = spark.read.format("delta").load("data/bronze/test_table")
print("=== Lecture Delta OK ===")
df_read.show()

from delta.tables import DeltaTable
delta_table = DeltaTable.forPath(spark, "data/bronze/test_table")

new_data = [("bus_39", "stop_678", 500), ("bus_99", "stop_456", 120)]
new_df = spark.createDataFrame(new_data, ["trip_id", "stop_id", "delay"])

delta_table.alias("old").merge(
    new_df.alias("new"),
    "old.trip_id = new.trip_id AND old.stop_id = new.stop_id"
).whenMatchedUpdate(set={"delay": "new.delay"}
).whenNotMatchedInsertAll(
).execute()

print("=== MERGE OK ===")
delta_table.toDF().show()

spark.stop()
print("=== TOUS LES TESTS PASSENT ===")