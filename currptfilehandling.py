# Databricks notebook source


# COMMAND ----------

from pyspark.sql import SparkSession

spark = SparkSession.builder.appName("spark DataFrame").getOrCreate()

# COMMAND ----------

df = spark.read.format('.csv')
.option('header','true')
.option('inferSchema','true')
.option('mode','permissive')
.load('/Volumes/pyspark/daily/projectdata/curruptdata.csv')

# COMMAND ----------

df=spark.read.format("csv")\
    .option("header",True)\
    .option("inferSchema",True)\
    .option("delimiter",",")\
    .option("mode","dropmalformed")\
    .load("/Volumes/pyspark/daily/projectdata/curruptdata.csv")
df.show()

# COMMAND ----------



# COMMAND ----------

df= spark.read.format("csv")\
    .option("header",True)\
    .option("inferSchema",True)\
    .option("delimiter",","|")\
    .option("mode","failfast")\
    .load('/Volumes/pyspark/daily/projectdata/curruptdata.csv')
df.show()

# COMMAND ----------



# COMMAND ----------



# COMMAND ----------



# COMMAND ----------

#new changes have been made in this notebook