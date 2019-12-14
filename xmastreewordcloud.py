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
引数1：tweets 型：arr
引数2：searchtime 型：datetime
出力：YYYY-MM-DDTHH:MM:SS.png
"""
def gen_wordcloud(tweets, searchtime):
    texts = " ".join(tweets)
    t = Tagger()
    # 日本語をスペース区切りのテキストにし、splittextに格納する
    splitedtext = " ".join([x.split("\t")[0] for x in t.parse(texts).splitlines()[:-1] if x.split("\t")[1].split(",")[0] not in ["助詞", "助動詞"]]).replace("クリスマス", "").replace("\n", "")

    # maskを作成する
    maskimage_path = "xmastree.png"
    mask = np.array(Image.open(maskimage_path))

    # wordcloudを作成する
    # WordCloud中の引数について
    #     background_color: 背景色
    #     mask: マスクする境界線の配列情報
    #     countour_width: 境界線の太さ
    #     countour_color: 境界線の色
    wc = wordcloud.WordCloud(font_path = "fonts/NotoSansCJKjp-Regular.otf", regexp = "[\w']+", background_color = 'white', mask = mask, contour_width = 3, contour_color = 'green').generate(splitedtext)

    # 画像として保存を行う
    wcimage_path = save_wcimage(wc, searchtime)
    return wcimage_path

# wc画像を保存、保存先のパスを返す関数
"""
引数1：wc
引数2：searchtime 型：datetime
出力：wcimage_path 型：string
"""
def save_wcimage(wc, searchtime):
    filename = searchtime.strftime("%Y-%m-%d") + "T" + searchtime.strftime("%H:%M:00") + ".png"
    wcimage_path = "view/build/static/media/" + filename
    wc.to_file(wcimage_path)
    return filename