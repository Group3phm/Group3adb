# Databricks notebook source
df = spark.read.format("csv").load("/mnt/tmpadls/silver/Product_20221216.csv", header = True)
display(df)

# COMMAND ----------

df.write.format("parquet").save("/mnt/tmpadls/gold/Product_20221216")

# COMMAND ----------

df.printSchema()

# COMMAND ----------


