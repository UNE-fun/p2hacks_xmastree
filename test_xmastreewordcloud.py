import unittest
import xmastreewordcloud
import os
import datetime

class Test_Wordcloud(unittest.TestCase): 
    def setUp(self):
        # 初期化処理　各テスト前に実行される 
        self.tweets = ['クリスマスになると毎年理解のできん依頼が届くのは何故だ…', '【ピンクの謎】\nTwitterへ何をシェアすればいいのだろう……\nピンクの謎のヒントをお願いします！\n\n283プロ 謎解きクリスマス\n\n#ピンクの謎 #283プロ謎解きクリスマス #シャニマス', 'カレーか蕎麦で迷ってカレーにしたしクリスマスセット気になって注文した ', 'サンタがゲストのクリスマス前配信', '今年のクリスマス・イブ又クリスマスはゴスカフェ梅田で貢いでくるwww←\n(💰余裕あればシャンパンボトル欲しい……)', 'フォロワーーー！！！！！ Vroid mobileがクリスマス仕様だよ！！！！ うちの子作ってパーティーしよ！！！！ あと寝室が夜だよ！！！ 夜だよ！！！！ うちよそ！！！！！！！！（シャウト） ', '#柚と歩く12月\n15年師走のドリフェスより\n「すのーまんず｣\n\nフリータイム☆クリスマス引けなかった奴は応えてみろ\n私「ここにいるぞー(泣)｣\n\n限定引けなきゃ担当じゃない？ プロデュースはPそれぞれですよ♪\n\nこの面子は私のツ… ', '本日もご来店ありがとうございました🐶\n\nもうすぐクリスマスなので、ギャラリーではギフトセットを販売しております🎁\n\nもちかわクッション送料無料サービスがございますので、プレゼントに送るのもおすすめです✨\n\nそして\n『オリジナルまる… ', '今日のメルマガより🍎\n箱に入ってる場合じゃない(笑)\n残り5時間よ～😱\n#鬼鬼鬼鬼可愛愛いいい斬りキャンペーン\nクリスマスはRadyを着て素敵なクリスマス🎄🎅🎁✨を過ごしましょ❤️\n@xxsmsmsmxx… ', 'みんなやってるから\nいいねでやります\n\n🎅🏼名前⋮ \n🎄今の印象⋮ \n🦌好きor嫌い⋮\n🎂絡みたい ？⋮ \n⭐LINE交換できる？⋮ \n🍷通話できる？⋮ \n⛄️クリスマス何あげたい？⋮ \n❄最後に一言⋮', 'よし、今年のクリスマスの予定決まった！（インターンシップ）', '福祉が嫌われてるなら嫌われてるでそれでいいけどうちが作った制作物たちに罪はない･･･うちひとつひとつ大切に作 ってたんやけど･･･クリスマスは去年も無くなったから2年分･･･もう作らんけどさひとつひとつ に思い出があったのになぁ･･･', '#クリスマスにみんながくれるもの2019\n@kuramotokun：インフル\n@t_tck_：現金\n@benkisan8426：絶対零度の視線\n@sasanoha_taso：笑顔\n@yapiyapi_：クリスマスだけのデート券… ', '今日は吹奏楽のクリスマスマス演奏会の練習してきました\nトロンボーンたまに吹いてます', '今ちょっと本当にアレだから、楽しいことを考えることにしようそうしよう。\n\nさて、今年のクリスマスはお菓子の家をどう進化させようかな(*´ω｀*)\n違法建築祭り〜！\n\n#お菓子の家 ']
        self.testtime = datetime.datetime.now()
        xmastreewordcloud.gen_wordcloud(self.tweets, self.testtime)
        pass
    
    def tearDown(self):
        # 終了処理　各テスト後に実行される
        os.remove("view/build/static/media/" + self.testtime.isoformat(timespec="seconds") + ".png")
        pass


    def test_save_image(self):
        # 指定ディレクトリに画像は存在しているか
        self.assertTrue( os.path.exists("view/build/static/media/" + self.testtime.isoformat(timespec="seconds") + ".png") )
    
    """
    TODO:余裕があればこの辺のテストも作れたらいいよね
    # 単語リストに助詞、助動詞は含まれていないか
    def Test_word_split(self):
        self.assertEqual()

    # mask画像を作成できているか
    def Test_make_maskarr(self):

    # wordcloudは生成できているか
    def Test_gen_wordclod(self):
    """

if __name__ == "__main__":
    unittest.main()