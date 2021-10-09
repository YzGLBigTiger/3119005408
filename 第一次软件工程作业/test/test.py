import sys
sys.path.append("..")
import cal_sim_cosine as cal


def test():
    result_file = open("test_result", "w", encoding="utf-8")

    result = [cal.cal_sim_cosine("测试文本\\orig.txt", "测试文本\\orig_0.8_add.txt"),
              cal.cal_sim_cosine("测试文本\\orig.txt", "测试文本\\orig_0.8_del.txt"),
              cal.cal_sim_cosine("测试文本\\orig.txt", "测试文本\\orig_0.8_dis_1.txt"),
              cal.cal_sim_cosine("测试文本\\orig.txt", "测试文本\\orig_0.8_dis_10.txt"),
              cal.cal_sim_cosine("测试文本\\orig.txt", "测试文本\\orig_0.8_dis_15.txt")
              ]

    result_file.write("测试结果接近，不保留两位小数\n")
    for i in range(len(result)):
        result_file.write(str(result[i]) + "\n")

    result_file.close()


test()
