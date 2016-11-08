# coding: utf-8
from __future__ import print_function, unicode_literals
from bosonnlp import BosonNLP
from emotion.FileHelp import get_file
from emotion.XmlParse import parse_local
from emotion.XmlParse import parse_local_emotion

nlp = BosonNLP('RqBUPoNy.10163.eX-oJkt9S0sA')


# 原来的方法，还需要安装sdk
def analysis_emotion(params):
    return nlp.sentiment(params, model='film')


def local_file_control(params, path):
    local_file_list = []
    get_file(path, local_file_list)
    for file_path in local_file_list:
        parse_local(file_path, params)


def local_file_control_for_emotion(params, path, key):
    local_file_list = []
    get_file(path, local_file_list)
    for file_path in local_file_list:
        parse_local_emotion(file_path, params, key)


def error_rate():
    pass


if __name__ == '__main__':
    comment_list = []
    # local_file_control(comment_list)
    # # print(len(comment_list))
    print(analysis_emotion(comment_list))
