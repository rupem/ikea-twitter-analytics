from sqlalchemy import create_engine,text
import pandas as pd
from textblob import TextBlob
import re

alchemyEngine   = create_engine('postgresql+psycopg2://postgres:docker@127.0.0.1:5432/ikea_db', pool_recycle=3600)

def get_tweets():
    sql = '''
    SELECT * FROM tweets;
    '''
    with alchemyEngine.connect().execution_options(autocommit=True) as conn:
        query = conn.execute(text(sql))         
    df = pd.DataFrame(query.fetchall())
    return df

def clean_tweet(tweet):
        '''
        Utility function to clean tweet text by removing links, special characters
        using simple regex statements.
        '''
        return ' '.join(re.sub("(@[A-Za-z0-9]+)|([^0-9A-Za-z \t])|(\w+:\/\/\S+)", " ", tweet).split())


def get_tweet_sentiment(tweet):
        '''
        Utility function to classify sentiment of passed tweet
        using textblob's sentiment method
        '''
        # create TextBlob object of passed tweet text
        analysis = TextBlob(clean_tweet(tweet))
        # set sentiment
        if analysis.sentiment.polarity > 0:
            return 'positive'
        elif analysis.sentiment.polarity == 0:
            return 'neutral'
        else:
            return 'negative'