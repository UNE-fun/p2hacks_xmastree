import unittest
import wordcloud

class Test_Wordcloud(unittest.TestCase):    
    def Test_save_image(self):
        # 生成した画像の名前は制約を満たしているか
        self.assertEqual()
        # /static/images/の下に画像は存在しているか
        self.assertTrue()
    
    """
    ASK: この辺のテストとか必要？足りてないテストとかあれば指摘求む
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