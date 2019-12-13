from flask import Flask, jsonify
from tweets import get_tweets
from wordcloud import gen_wordcloud

app = Flask(__name__)

@app.route('/')
def index():
    return { 'status': 200 }

@app.route('/tweets_at/<date>')
def tweets_at(date):
    # TODO: 一度生成された画像があれば、そちらを使うようにしたい
    tweets = get_tweets(date)
    wordcloud_path = gen_wordcloud(tweets)
    return wordcloud_path
