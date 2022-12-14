"""
This is the first step in batch processing of analytics.
This module reads required arguments and fetch related tweets.
"""

import tweepy
import json
import yaml
from datetime import datetime
from datetime import date
from yaml.loader import SafeLoader
import pandas as pd
import sys
import logging

def load_tweets(hash_tag):
    logging.basicConfig(level=logging.INFO)
    logging.info("**********Loading user credentials**************")
    # Open the file and load the file
    with open('ikea_analytics\\batch_processing\\user_details.yaml') as f:
        user_data = yaml.load(f, Loader=SafeLoader)
        
    today_timestamp = datetime(date.today().year, date.today().month, date.today().day, 00, 00)


    client = tweepy.Client(bearer_token=user_data['bearer_token'])


    logging.info("**********tweets for the hashtag/keyword "+hash_tag+" for the date "+str(date.today())+" are loading **************")

    query = hash_tag+' -is:retweet lang:en'
    # query = '#IKEA -is:retweet lang:en'
    fields = ['id','text','created_at','public_metrics']
    sub_fields = ['retweet_count','reply_count','like_count','quote_count']
    tweets = client.search_recent_tweets(query=query,
    tweet_fields=fields,start_time=today_timestamp , max_results=100)

    tweets_list = []
    try:
        for t in tweets.data:
            field_dict = {}
            for f in fields:
                if f == 'public_metrics':
                    field_dict['retweet_count'] = t[f]['retweet_count']
                    field_dict['reply_count'] = t[f]['reply_count']
                    field_dict['like_count'] = t[f]['like_count']
                    field_dict['quote_count'] = t[f]['quote_count']
                elif f == 'text':
                    field_dict[f] = t[f].replace('\n','')
                else:
                    field_dict[f] = t[f]
            tweets_list.append(field_dict)
    except Exception as e:
        print(e)
        return 1


    df = pd.DataFrame(tweets_list)

    df.to_csv("ikea_analytics\\batch_processing\\data\\raw_data\\"+str(date.today())+".csv", sep ='\t')
    logging.info("********** Loaded tweets into ikea_analytics\\batch_processing\\data\\raw_data\\"+str(date.today())+".csv **************")

    return 0
        




