"""
This module analyses tweets and get descriptive analysis out of it.
returns top 10 tweets of given hastag with top like and retweet count.
"""

import pandas as pd
import logging

import psycopg2
import pandas as pds
from sqlalchemy import create_engine,text
from .utilities import alchemyEngine,get_tweets

def analyze_tweets():
    logging.basicConfig(level=logging.INFO)
    logging.info("********** Loading tweets for analysis **************")
    df = get_tweets()
    print(df.sort_values(by=['like_count','retweet_count'],ascending=False)[:10])
    logging.info("********** tweets analysis end **************")