# Databricks notebook source
df = spark.read.format("csv").load("/mnt/tmpadls/silver/orders_20221216.csv", header = True)
display(df)

# COMMAND ----------

df.write.format("parquet").save("/mnt/tmpadls/gold/orders_20221216.csv")

# COMMAND ----------

df.printSchema()

# COMMAND ----------


