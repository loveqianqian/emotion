from __future__ import print_function, unicode_literals
import json
import requests


def analysis_list(param):
    emotion_url = 'http://api.bosonnlp.com/sentiment/analysis?weibo'
    data = json.dumps(param)
    headers = {'X-Token': 'RqBUPoNy.10163.eX-oJkt9S0sA', 'content-type': 'application/json'}
    resp = requests.post(emotion_url, headers=headers, data=data.encode('utf-8'))

    return resp.text


def weights_list(param):
    emotion_url = 'http://api.bosonnlp.com/keywords/analysis'
    my_params = {'top_k': 10}
    data = json.dumps(param)
    headers = {'X-Token': 'RqBUPoNy.10163.eX-oJkt9S0sA', 'content-type': 'application/json'}
    resp = requests.post(emotion_url, headers=headers, params=my_params, data=data.encode('utf-8'))

    return resp


def association_list():
    emotion_url = 'http://api.bosonnlp.com/suggest/analysis'
    term = '喜爱'
    my_params = {'top_k': 10}
    data = json.dumps(term)
    headers = {'X-Token': 'RqBUPoNy.10163.eX-oJkt9S0sA'}
    resp = requests.post(emotion_url, headers=headers, params=my_params, data=data.encode('utf-8'))
    resp.raise_for_status()

    return resp


if __name__ == '__main__':
    # params = ['电影太差了，电影还不错,这是一个不错，一般吧']
    # print(analysis_list(params))
    # params = ['电影太差了', '电影还不错', '这是一个不错', '一般吧']
    # result = analysis_list(params)
    # print(result)
    # text = 'Old chicken，王志勇，EHOME现中单选手，擅长米拉娜、剑圣、伐木机，常常被玩家称为“老鸡”。2014年6月份老鸡加入U5战队担任一号位。一年之后由于其优秀的表现转会至EP俱乐部，在EP期间，从1号位开始转型2号位，并且和队友FaN、lt、2Lei、le一起打到了TI5中国区第三名，距离西雅图仅一步之遥。'
    # my_result = weights_list(text)
    # for weight, word in my_result.json():
    #     print(weight, word)
    my_result = association_list()
    for score, word in my_result.json():
        print(score, word)
