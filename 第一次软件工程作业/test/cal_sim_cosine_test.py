import unittest

import sys

sys.path.append("..")

import cal_sim_cosine as cal


class CalSimCosineTest(unittest.TestCase):
    def setUp(self):
        print("单元测试开始：")

    def tearDown(self):
        print("单元测试结束.\n")

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

    def test_get_vector(self):
        self.assertEqual([2, 0], cal.get_vector([1, 1], [1, 0]))
        self.assertEqual([3, 0], cal.get_vector([1, 1, 1], [1, 0]))
        self.assertEqual([1, 2, 0], cal.get_vector([0, 1, 1], [0, 1, 2]))

    def test_cal_vector_cos(self):
        self.assertEqual(1, round(cal.cal_vector_cos([1, 1, 1], [1, 1, 1]), 2))
        self.assertEqual(0, cal.cal_vector_cos([0, 1, 9], [3, 0, 0]))

    def test_cal_sim_cosine(self):
        self.assertEqual(1.0, cal.cal_sim_cosine("测试文本//orig.txt", "测试文本//orig.txt"))
        self.assertGreater(1.0, cal.cal_sim_cosine("测试文本//orig.txt", "测试文本//orig_0.8_add.txt"))


if __name__ == "__main__":
    unittest.main()
