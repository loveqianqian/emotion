# coding: utf-8
from xml.dom.minidom import parseString


# 解析xml文件,获取评论
def parse_local(path, params):
    # print('current file:' + path)
    my_file = open(path, "r+", encoding="utf8")
    my_text = my_file.read()
    byte_text = my_text.encode('utf8', 'ignore')
    new_file = byte_text.decode('utf8').replace("", "").replace("", "")
    my_file.close()
    domTree = parseString(new_file)
    rootElement = domTree.documentElement

    items = rootElement.getElementsByTagName("列表")

    for item in items:
        subItems = item.getElementsByTagName("item")

        for subItem in subItems:
            comment = subItem.getElementsByTagName("评论")[0]
            score = subItem.getElementsByTagName("评分")[0]
            helpful = subItem.getElementsByTagName("有用")[0]
            # key = comment.nodeName
            value_comment = comment.childNodes[0].nodeValue
            value_score = score.childNodes[0].nodeValue
            value_helpful = helpful.childNodes[0].nodeValue
            # print(key + ":" + value)
            params.append(value_comment.strip() + "," + value_score.strip()*int(value_helpful.strip()))


if __name__ == '__main__':
    resultList = []
    # parse_local("C:\\emotion\\大圣归来_74563858_2876889383.xml", resultList)
    # parse_local("大圣归来_74563858_2908998282.xml", resultList)
    # print(resultList)
    num = [[0.9999998911683837, 1.0883161625047639e-07]]
    print(num[0][0] + num[0][1])
    print(str([[0.9999998911683837, 1.0883161625047639e-07]]))
    num = str([[0.9999998911683837, 1.0883161625047639e-07]])
    num1 = num.replace('[[', '').replace(']]', '')
    num2 = num1.split(",")
    print(num2[0])
    my_dict = {'test': '123', 'test1': '321'}
    print(my_dict['test'])
