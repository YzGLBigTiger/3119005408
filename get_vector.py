def get_vector(file_words_list, merged_list):
    my_dict = {}
    vector = []

    for i in range(len(merged_list)):
        my_dict[merged_list[i]] = 0

    for j in range(len(file_words_list)):
        my_dict[file_words_list[j]] = my_dict[file_words_list[j]] + 1

    for k in range(len(merged_list)):
        vector.append(my_dict[merged_list[k]])

    return vector

