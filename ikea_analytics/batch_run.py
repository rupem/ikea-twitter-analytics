import sys
import os
from datetime import datetime, date, timedelta

from batch_processing.tweet_loader import load_tweets
from batch_processing.batch_processor import spark_process


current_date = datetime.today()
old_date = (current_date - timedelta(days=7)).date

print(old_date)

print(sys.argv)
loader = load_tweets('#IKEA')

if loader == 0:
    spark_process()


if os.path.exists("demofile.txt"):
  os.remove("demofile.txt")
else:
  print("The file does not exist")

sys.exit(0)