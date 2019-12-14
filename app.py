from flask import Flask, redirect, jsonify
from datetime import datetime
from tweets import Tweets
from xmastreewordcloud import gen_wordcloud
import os

app = Flask(__name__, static_folder='view/build', static_url_path='/')

@app.route('/')
def index():
    return redirect('/index.html')

@app.route('/tweets_at/<date_str>')
def tweets_at(date_str):
    date = datetime.fromisoformat(date_str)
    wordcloudimagename = date.isoformat(timespec="seconds") + ".png"
    if(os.path.exists("view/build/static/media/" + wordcloudimagename)):
        # 生成された画像が存在する場合
        wordcloud_path = wordcloudimagename
    else:
        # 生成された画像が存在しない場合
        tweets = Tweets(date).get_tweets()
        wordcloud_path = gen_wordcloud(tweets, date)
    return wordcloud_path
