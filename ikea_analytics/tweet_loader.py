import tweepy
# import pyyaml module
import yaml
from yaml.loader import SafeLoader

# Open the file and load the file
with open('User_details.yaml') as f:
    user_data = yaml.load(f, Loader=SafeLoader)
    


client = tweepy.Client(bearer_token=user_data['bearer_token'])

query = '#IKEA -is:retweet lang:en'
tweets = client.search_recent_tweets(query=query, tweet_fields=['id,text,created_at,public_metrics'], max_results=100)

for t in tweets:
    print(t)