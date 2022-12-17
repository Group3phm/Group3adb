# Databricks notebook source
# MAGIC %run /Group3Assignment/SharedLibraryImport

# COMMAND ----------

# PipeLineName = getArgument('PipeLineName')
# FactoryName=getArgument('FactoryName')
# ErrorDetail=getArgument('ErrorDetail')


# COMMAND ----------

df = [['Customers_Order_Master_PL_Adv_Gen2', 'Group3TrngDataFactory', 'Activity Failed']]
col=  ['PipeLineName', 'FactoryName', 'ErrorDetail']
dfErrorLog = spark.createDataFrame(df, col)
display(dfErrorLog)

# COMMAND ----------

dfErrorLog.write.format("parquet").save("/mnt/tmpadls/PLRunLog/ErrorLog.txt")
