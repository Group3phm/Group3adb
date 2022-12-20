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

df = spark.read.format("csv").load("/mnt/tmpadls/silver/Product_{0}.csv".format(loaddate), header = True)
display(df)

# COMMAND ----------

# Fill the Null Values
df=df.fillna( {'ProductCategory':'Store Items'} )
display(df)

# COMMAND ----------

# Rename Columns
df=df.withColumnRenamed('PRODUCT_ID','PRODUCTID').withColumnRenamed('PRODUCT_NAME','PRODUCTNAME')

# COMMAND ----------

# Add New Columns 
df2 = df.withColumn("LoadDate", f.current_date())
display(df2)

# COMMAND ----------

#  we can perform multiple transformation here if required

# COMMAND ----------


loadDate = datetime.now().strftime("%Y-%m-%d")    
print(loadDate)
filename='Product_' + loadDate
df.write.format("parquet").mode("overwrite").save("/mnt/tmpadls/gold/"+filename)

# COMMAND ----------

df.printSchema()

# COMMAND ----------


