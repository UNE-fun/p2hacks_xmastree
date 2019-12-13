from flask import Flask, redirect, jsonify
from tweets import Tweets
from xmastreewordcloud import gen_wordcloud

app = Flask(__name__, static_folder='view/build', static_url_path='/')

@app.route('/')
def index():
    return redirect('/index.html')

@app.route('/tweets_at/<date>')
def tweets_at(date):
    # TODO: 一度生成された画像があれば、そちらを使うようにしたい
    tweets = Tweets(date).get_tweets()
    wordcloud_path = gen_wordcloud(tweets)
    return wordcloud_path
