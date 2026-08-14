from pyspark.sql import SparkSession
from pyspark.sql.functions import *

spark = SparkSession.builder \
.appName("RetailETL") \
.getOrCreate()

df = spark.read.format("bigquery") \
.option("table",
"project-df65380f-e50e-43c9-9b6.walmart_demo.sales") \
.load()

df = df.withColumn(
"total_sales",
col("quantity")*col("price"))

df=df.filter(col("quantity")>0)

df=df.dropDuplicates()
df.write.mode("overwrite") \
.parquet(
"gs://test_gds1/processed/parquet/")
df.write \
.mode("overwrite") \
.option("header", "true") \
.csv("gs://test_gds1/processed/csv/")
df.show()