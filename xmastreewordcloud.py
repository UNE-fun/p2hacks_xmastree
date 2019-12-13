# wordlcoud作成モジュール

# 必要なライブラリの導入
from PIL import Image
import numpy as np
from MeCab import Tagger
import wordcloud
import datetime

# wordcloudを作成する関数
"""
TODO: 文字列から成るtweetsを元に、wordcloudの画像を生成し、`/static/images/`内に保存、その画像のパス(ファイル名だけで良い)を返す。
画像のファイル名は、`2019-12-13T12:00:00`とし、これは日本時間によるものとする。
TODO: stringが引数だと想定して開発をしていた。arrで動作するように修正をする。
引数：tweets 型：arr
出力：YYYY-MM-DDTHH:MM:SS.png
"""
def gen_wordcloud(tweets):
    texts = sentences_to_texts(tweets)
    # 日本語をスペース区切りのテキストにし、splittextに格納する
    splitedtext = text_split(texts).replace("クリスマス", "").replace("\n", "")

    # maskを作成する
    #mask = make_maskarr(maskimage_path)

    # wordcloudを作成する
    # WordCloud中の引数について
        # background_color: 背景色
        # mask: マスクする境界線の配列情報
        # countour_width: 境界線の太さ
        # countour_color: 境界線の色
        # width: 出力画像の幅
        # height: 出力画像の高さ
    # wc = wordcloud.WordCloud(regexp="[\w']+", background_color='white', mask=mask, countour_width=3, contour_color='green', width=800, height=600).generate(splitedtext)
    wc = wordcloud.WordCloud(font_path="fonts/NotoSansCJKjp-Regular.otf", regexp="[\w']+", background_color='white', width=800, height=600).generate(splitedtext)

    # 画像として保存を行う
    nowtime = datetime.datetime.now()
    wcimage_path = save_wcimage(wc, nowtime)
    return wcimage_path

# 配列を受け取ったときに文字列へと格納し直す関数
"""
引数：sentences 型：arr
出力：texts 型：string
"""
def sentences_to_texts(sentencearr):
    return " ".join(sentencearr)

# 文字列をスペース区切りのテキストにし、助詞助動詞を取り除く関数
"""
引数：texts 型：string
出力： 型：
"""
def text_split(texts):
    t = Tagger()
    return  " ".join([x.split("\t")[0] for x in t.parse(texts).splitlines()[:-1] if x.split("\t")[1].split(",")[0] not in ["助詞", "助動詞"]])

# mask画像の配列を作成する関数
"""
# TODO: mask画像を用意する
引数：maskimage_path 型：string
出力：maskarr 型：arr
"""
def make_maskarr(maskimage_path):
    maskarr = np.array(Image.open(maskimage_path))
    return maskarr

# wc画像を保存、保存先のパスを返す関数
"""
引数1：wc
引数2：nowtime 型：datetimeオブジェクト
出力：wcimage_path 型：string
"""
def save_wcimage(wc, nowtime):
    wcimage_path = "static/images/" + nowtime.strftime("%Y-%m-%d") + "T" + nowtime.strftime("%H:%M:00") + ".png"
    wc.to_file(wcimage_path)
    return wcimage_path