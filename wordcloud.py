# wordlcoud作成モジュール

# 必要なライブラリの導入
import matplotlib.pyplot as plt
import Image
import numpy as np
from MeCab import Tagger
from wordcloud import WordCloud

# wordcloudを作成する関数
"""
TODO: 文字列から成るtweetsを元に、wordcloudの画像を生成し、`/static/images/`内に保存、その画像のパス(ファイル名だけで良い)を返す。
画像のファイル名は、`2019-12-13T12:00:00`とし、これは日本時間によるものとする。
引数：tweets 型：文字列
出力：YYYY-MM-DDTHH:MM:SS.png
"""

def gen_wordcloud(tweets):
    t = Tagger()
    # 日本語をスペース区切りのテキストにし、splittextに格納する
    splittext = " ".join([x.split("\t")[0] for x in t.parse(tweets).splitlines()[:-1] not in ["助詞", "助動詞"]])
    # 一文字以上の語全てを抽出する
    wc = Wordcloud(regexp="[\w']+")

    """
    # TODO: mask画像を用意する
    mask = np.array(Image.open('mask.png'))
    # WordCloud中の引数について
        # background_color: 背景色
        # mask: マスクする境界線の配列情報
        # countour_width: 境界線の太さ
        # countour_color: 境界線の色
        # width: 出力画像の幅
        # height: 出力画像の高さ
    # wordcloudを作成する
    wc.wordcloud.WordCloud(background_color='white', mask=mask, countour_width=3, contour_color='green', width=800, height=600).generate(splittext)
    """
    # wordcloudを作成する
    wc.wordcloud.WordCloud(background_color='white', width=800, height=600).generate(splittext)

    # テスト的にmatplotlibを用いて表示を行う
    plt.imshow(wc)
    plt.show()

    # TODO: 画像をパス名指定して出力する
    # imagename = nowtime + "png"
    # wc.to_file(imagename)

    # TODO: 画像のパス名を返す
    return 0
