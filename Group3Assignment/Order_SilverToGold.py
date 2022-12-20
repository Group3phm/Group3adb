# Databricks notebook source
dbutils.widgets.text("loaddate", "")
loaddate = dbutils.widgets.get("loaddate")

# COMMAND ----------

import os
import json
from pyspark import SparkConf,SparkContext
from pyspark.sql import SparkSession, SQLContext
from datetime import datetime
import pyspark.sql.functions as f

# COMMAND ----------

df = spark.read.format("csv").load("/mnt/tmpadls/silver/orders_{0}.csv".format(loaddate), header = True)
display(df)

# COMMAND ----------

# Fill the Null Values
df=df.fillna( {'PaymentMode' : 'Online'} )
df=df.fillna( {'OrderDiscount' : '10%'} )

# COMMAND ----------

# Rename Columns
df=df.withColumnRenamed('CUSTOMER_ID','CUSTOMERID').withColumnRenamed('STORE_ID','STOREID')

# COMMAND ----------

# Add New Columns 
df = df.withColumn("LoadDate", f.current_date())

# COMMAND ----------

loadDate = datetime.now().strftime("%Y-%m-%d")    
print(loadDate)
filename='Orders_' + loadDate
df.write.format("parquet").mode("overwrite").save("/mnt/tmpadls/gold/"+filename)

# COMMAND ----------

df.printSchema()
