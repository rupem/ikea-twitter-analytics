#!/bin/bash
hashtag=$1
echo "Fetching data for given hashtag $hashtag"
python batch_processing/tweet_loader.py $hashtag
echo "Running batch processor"
python batch_processing/batch_processor.py