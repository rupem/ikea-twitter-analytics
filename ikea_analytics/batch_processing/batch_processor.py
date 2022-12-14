from pyspark.sql import SparkSession
from pyspark.sql.functions import to_date
import logging

def spark_process():
    logging.basicConfig(level=logging.INFO)
    logging.info("********** Loading Spark Session **************")
    spark = SparkSession.Builder().master("local[*]").appName("twitter_batch").getOrCreate()

    logging.info("********** Loading tweets into spark **************")
    df = spark.read.option("header","true").options(delimiter='\t').csv('ikea_analytics\\batch_processing\\data\\raw_data\\')
    date_df = df.withColumn("created_date",to_date("created_at"))
    date_df.show()
    date_df.repartition("created_date").write.mode("overwrite").partitionBy("created_date").csv("ikea_analytics\\batch_processing\\data\\processed_data\\")
    logging.info("********** partitioned data loaded into ikea_analytics\\batch_processing\\data\\processed_data **************")