import unittest

import sys
sys.path.append("..")


import cal_sim_cosine as cal

class cal_sim_cosine(unittest.TestCase):
    def setUp(self):
        print("单元测试开始：")


    def tearDown(self):
        print("单元测试结束.")

    def test_import_file(self):
        self.assertIsNotNone(cal.import_file("测试文本//orig.txt"))
        self.assertEqual(cal.import_file("测试文本//None"), '')

    def test_jieba_cut(self):
        self.assertIn("我", cal.jieba_cut("我很帅。"))
        self.assertNotIn("你", cal.jieba_cut("我很帅。"))
        self.assertNotIn("。", cal.jieba_cut("我很帅。"))
        self.assertEqual([], cal.jieba_cut("。."))

    def test_merge_words(self):
        self.assertEqual(['1', '2'], cal.merge_words(['1', '.'], ['2']))
        self.assertEqual(['1'], cal.merge_words(['1', '.'], []))
        self.assertEqual(['1'], cal.merge_words(['1', '.'], ['1']))
