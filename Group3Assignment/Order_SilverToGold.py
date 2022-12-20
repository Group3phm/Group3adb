# Databricks notebook source
dbutils.widgets.text("loaddate", "")
loaddate = dbutils.widgets.get("loaddate")

# COMMAND ----------

df = spark.read.format("csv").load("/mnt/tmpadls/silver/orders_{0}.csv".format(loaddate), header = True)
display(df)

# COMMAND ----------

df.write.format("parquet").save("/mnt/tmpadls/gold/orders_{0}.csv".format(loaddate))

# COMMAND ----------

df.printSchema()

# COMMAND ----------


