import jieba


def my_cut(mystr):
    mylist = jieba.lcut(mystr)
    return mylist
