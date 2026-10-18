SPARK_CONFIG = {
    "spark.app.name": "TransportLive",
    "spark.master": "local[2]",
    "spark.driver.memory": "1g",
    "spark.executor.memory": "1g",
    "spark.sql.extensions": "io.delta.sql.DeltaSparkSessionExtension",
    "spark.sql.catalog.spark_catalog": "org.apache.spark.sql.delta.catalog.DeltaCatalog",
    "spark.jars.packages": "io.delta:delta-spark_2.12:3.2.1,org.apache.spark:spark-sql-kafka-0-10_2.12:3.5.3",
}