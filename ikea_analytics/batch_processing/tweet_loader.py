import tweepy
import json
import yaml
from datetime import datetime
from datetime import date
from yaml.loader import SafeLoader

# Open the file and load the file
with open('User_details.yaml') as f:
    user_data = yaml.load(f, Loader=SafeLoader)
    
today_timestamp = datetime(date.today().year, date.today().month, date.today().day, 00, 00)


client = tweepy.Client(bearer_token=user_data['bearer_token'])

query = '#IKEA -is:retweet lang:en'
fields = ['id','text','created_at','public_metrics']
tweets = client.search_recent_tweets(query=query,
 tweet_fields=fields,start_time=today_timestamp , max_results=100)

tweets_list = []
for t in tweets.data:
    field_dict = {}
    for f in fields:
        field_dict[f] = t[f]
    tweets_list.append(field_dict)

tweets_json = json.dumps(tweets_list,indent=4,sort_keys=True, default=str)

with open("data\\raw_data\\"+str(date.today())+".json", 'w', encoding='utf-8') as outfile:
    json.dump(tweets_json, outfile)
    




