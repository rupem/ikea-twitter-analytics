import pandas as pd
import logging

import psycopg2

import pandas as pds

from sqlalchemy import create_engine,text

# Create an engine instance

alchemyEngine   = create_engine('postgresql+psycopg2://postgres:docker@127.0.0.1:5432/ikea_db', pool_recycle=3600);

def analyze_tweets():
    logging.basicConfig(level=logging.INFO)
    logging.info("********** Loading tweets for analysis **************")
    sql = '''
    SELECT * FROM tweets;
    '''
    with alchemyEngine.connect().execution_options(autocommit=True) as conn:
        query = conn.execute(text(sql))         
    df = pd.DataFrame(query.fetchall())
    print(df.sort_values(by=['like_count','retweet_count'],ascending=False)[:10])
    logging.info("********** tweets analysis end **************")