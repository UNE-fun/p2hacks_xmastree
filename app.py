from flask import Flask, redirect, jsonify
from datetime import datetime
from tweets import Tweets
from xmastreewordcloud import gen_wordcloud

app = Flask(__name__, static_folder='view/build', static_url_path='/')

@app.route('/')
def index():
    return redirect('/index.html')

@app.route('/tweets_at/<date_str>')
def tweets_at(date_str):
    # TODO: 一度生成された画像があれば、そちらを使うようにしたい
    date = datetime.fromisoformat(date_str)
    tweets = Tweets(date).get_tweets()
    wordcloud_path = gen_wordcloud(tweets, date)
    return wordcloud_path
