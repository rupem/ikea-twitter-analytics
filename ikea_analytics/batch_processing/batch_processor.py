from pyspark.sql import SparkSession

spark = SparkSession.Builder().master("local[*]").appName("twitter_batch").getOrCreate()

spark.read.json('ikea_analytics\\batch_processing\\data\\raw_data\\').show()