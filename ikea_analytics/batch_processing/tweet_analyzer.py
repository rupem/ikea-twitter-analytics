import pandas as pd
import logging

def analyze_tweets():
    logging.basicConfig(level=logging.INFO)
    logging.info("********** Loading tweets analysis **************")
    

    logging.info("********** Loading processed tweets **************")
    

def get_tweet_sentiment(self, tweet):
        '''
        Utility function to classify sentiment of passed tweet
        using textblob's sentiment method
        '''
        # create TextBlob object of passed tweet text
        analysis = TextBlob(self.clean_tweet(tweet))
        # set sentiment
        if analysis.sentiment.polarity > 0:
            return 'positive'
        elif analysis.sentiment.polarity == 0:
            return 'neutral'
        else:
            return 'negative'