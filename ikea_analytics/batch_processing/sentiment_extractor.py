"""
This module extracts sentiments of tweets generated.
Uses TextBlod nltk library and pre loaded corpus to predict sentiment.
"""

from .utilities import alchemyEngine,get_tweets,clean_tweet,get_tweet_sentiment

def extract_sentiments():
    df = get_tweets()
    df['clean_text'] = df['text'].apply(lambda x : clean_tweet(x))
    df['sentiment'] = df['text'].apply(lambda x : get_tweet_sentiment(x))
    print(df[['text','retweet_count','like_count','sentiment']].sort_values(by=['like_count','retweet_count'],ascending=False)[:10])





