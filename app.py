from flask import Flask, render_template, jsonify
from tweets import Tweets
from wordcloud import gen_wordcloud

app = Flask(__name__, static_folder='./view/build/static', template_folder='./view/build')

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/tweets_at/<date>')
def tweets_at(date):
    # TODO: 一度生成された画像があれば、そちらを使うようにしたい
    tweets = Tweets(date).get_tweets()
    wordcloud_path = gen_wordcloud(tweets)
    return wordcloud_path
