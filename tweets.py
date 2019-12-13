import os
from datetime import datetime, timedelta
import urllib
import twitter

class Tweets():
    def __init__(self, date):
        self.api = twitter.Api(
            consumer_key=os.environ['TWITTER_CONSUMER_KEY'],
            consumer_secret=os.environ['TWITTER_CONSUMER_SECRET'],
            access_token_key=os.environ['TWITTER_ACCESS_TOKEN_KEY'],
            access_token_secret=os.environ['TWITTER_ACCESS_TOKEN_SECRET'],
        )
        since = datetime.fromisoformat(date).strftime('%Y-%m-%d')
        until = (datetime.fromisoformat(date) + timedelta(days=1)).strftime('%Y-%m-%d')
        self.query = f"q={urllib.parse.quote('クリスマス -filter:replies -filter:retweets')}&since={since}&until={until}"

    def get_tweets(self):
        response = self.api.GetSearch(raw_query=self.query)
        tweets = [res.text for res in response]
        print(tweets)
        return tweets

Tweets('2019-12-13').get_tweets()
