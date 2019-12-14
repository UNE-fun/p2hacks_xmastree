import os
from datetime import timedelta
import urllib
import re
import twitter

class Tweets():
    def __init__(self, date):
        self.api = twitter.Api(
            consumer_key=os.environ['TWITTER_CONSUMER_KEY'],
            consumer_secret=os.environ['TWITTER_CONSUMER_SECRET'],
            access_token_key=os.environ['TWITTER_ACCESS_TOKEN_KEY'],
            access_token_secret=os.environ['TWITTER_ACCESS_TOKEN_SECRET'],
        )
        since = date.strftime('%Y-%m-%d')
        until = (date + timedelta(days=1)).strftime('%Y-%m-%d')
        self.query = f"q={urllib.parse.quote('クリスマス -filter:replies -filter:retweets')}&since={since}&until={until}&count=100"

    def get_tweets(self):
        response = self.api.GetSearch(raw_query=self.query)
        tweets = [self.__remove_url(res.text) for res in response]
        return tweets

    def __remove_url(self, text):
        text = re.sub(r"https?://\S+", "", text, flags=re.MULTILINE)
        return text
