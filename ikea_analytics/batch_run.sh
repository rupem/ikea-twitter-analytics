echo "Fetching data for given hashtag"
python ikea_analytics/batch_processing/tweet_loader.py
echo "Running batch processor"
python ikea_analytics/batch_processing/batch_processor.py