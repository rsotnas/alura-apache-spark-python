# Import the necessary modules
from pyspark.sql import SparkSession
from pyspark.sql.functions import *

# Create a SparkSession
spark = SparkSession.builder \
    .master('local[*]') \
    .appName('Starting com Spark') \
    .config('spark.ui.port', '4050') \
    .getOrCreate()

rdd = spark.sparkContext.parallelize(range(1, 100))

print("THE SUM IS HERE: ", rdd.sum())
# Stop the SparkSession



spark.stop()