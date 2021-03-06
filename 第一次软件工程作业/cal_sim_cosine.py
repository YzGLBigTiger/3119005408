import jieba


def import_file(file_name):
    """输入一个文件名，将其内容以字符串形式返回"""
    try:
        file = open(file_name, "r", encoding="utf-8")
        file_text = file.read()
        file.close()

        if len(file_text) == 0:
            print(file_name + " 文件为空")

        # print(file_name + ":\n" + file_text)

        return file_text
    except IOError as e:
        print(e)


# 无效字符，这些字符不应该被记入查重的范围内
invalid_words_list = [',', ' ', '.', '。', '，', '(', '"', ')',
                      '\'', '_', ':', '：', '“', '‘', '\n', '、']


def jieba_cut(mystr):
    """用jieba分词模块的lcut函数将字符串分词，返回一个列表"""
    jieba_list = jieba.lcut(mystr)
    # print("mylist = " + str(mylist))

    my_list = list(set(jieba_list) - set(invalid_words_list))
    print("cut_list = " + str(my_list))
    return my_list


def merge_words(list1, list2):
    """将两个分词后得到的列表不重复地合并成一个列表"""
    new_list = []
    for i in range(len(list1)):
        if list1[i] not in new_list and list1[i] not in invalid_words_list:
            new_list.append(list1[i])

    for j in range(len(list2)):
        if list2[j] not in new_list and list2[j] not in invalid_words_list:
            new_list.append(list2[j])
    print("merged_list = " + str(new_list))
    return new_list


def get_vector(file_words_list, merged_list):
    """将分词后得到的列表根据合并后得到的列表向量化，返回一个向量列表"""
    my_dict = {}
    vector = []

    for i in range(len(merged_list)):
        my_dict[merged_list[i]] = 0

    for j in range(len(file_words_list)):
        if file_words_list[j] not in invalid_words_list:
            my_dict[file_words_list[j]] = my_dict[file_words_list[j]] + 1

    for k in range(len(merged_list)):
        vector.append(my_dict[merged_list[k]])
    print("vector = " + str(vector))
    return vector


def cal_vector_cos(vector1, vector2):
    """计算两个向量的余弦夹角作为相似度，返回一个浮点数"""
    num1 = 0
    for i in range(len(vector1)):
        num1 += vector1[i] * vector2[i]

    num2 = 0
    num3 = 0
    for i in range(len(vector1)):
        num2 += vector1[i] * vector1[i]
        num3 += vector2[i] * vector2[i]

    try:
        result = num1 / (num2 ** 0.5 * num3 ** 0.5)
        return result
    except ZeroDivisionError as e:
        print(e)


def cal_sim_cosine(file, origin_file):
    """将file的文本内容与origin_file的文本内容作比较，计算他们的余弦相似度，
    返回一个保留两位小数的浮点数"""
    text1 = import_file(file)
    text2 = import_file(origin_file)

    words_list1 = jieba_cut(text1)
    words_list2 = jieba_cut(text2)

    merged_list = merge_words(words_list1, words_list2)

    vector1 = get_vector(words_list1, merged_list)
    vector2 = get_vector(words_list2, merged_list)

    result = cal_vector_cos(vector1, vector2)

    # print(result)
    # print(float('%.2f' % result))

    return float(result)
