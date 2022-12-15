import sys
import os
from datetime import datetime, date, timedelta

from batch_processing.tweet_loader import load_tweets
from batch_processing.batch_processor import spark_process
from batch_processing.tweet_analyzer import analyze_tweets
from batch_processing.sentiment_extractor import extract_sentiments


current_date = datetime.today()
old_date = (current_date - timedelta(days=7)).date

print(old_date)

print(sys.argv)
loader = load_tweets(sys.argv[1])
print(loader)
if loader == 0:
    spark_process()


analyze_tweets()
extract_sentiments()





sys.exit(0)