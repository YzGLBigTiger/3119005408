def merge_words(list1, list2):
    new_list = []
    for i in range(len(list1)):
        new_list.append(list1[i])

    for j in range(len(list2)):
        if list2[j] not in new_list:
            new_list.append(list2[j])

    return new_list
