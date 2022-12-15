from pyspark.sql import SparkSession
from pyspark.sql.functions import to_date
import logging

def spark_process():
    logging.basicConfig(level=logging.INFO)
    logging.info("********** Loading Spark Session **************")
    spark = SparkSession.Builder().config("spark.jars","ikea_analytics\\batch_processing\\postgresql-42.2.5.jar").master("local[*]").appName("twitter_batch").getOrCreate()

    logging.info("********** Loading tweets into spark **************")
    df = spark.read.option("header","true").options(delimiter='\t').csv('ikea_analytics\\batch_processing\\data\\raw_data\\')
    date_df = df.withColumn("created_date",to_date("created_at"))
    selected_df = date_df.select("id","text","created_at","retweet_count","reply_count","like_count","quote_count","created_date")
    selected_df.show()
    selected_df.repartition("created_date").write.mode("overwrite").partitionBy("created_date").csv("ikea_analytics\\batch_processing\\data\\processed_data\\")
    logging.info("********** partitioned data loaded into ikea_analytics\\batch_processing\\data\\processed_data **************")
    mode = "overwrite"
    url = "jdbc:postgresql://localhost:5432/ikea_db"
    properties = {"user": "postgres","password": "docker","driver": "org.postgresql.Driver"}
    selected_df.write.jdbc(url=url, table="tweets", mode=mode, properties=properties)
    logging.info("********** data loaded into tweets table **************")
