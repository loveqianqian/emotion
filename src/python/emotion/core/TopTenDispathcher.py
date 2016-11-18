# encoding: utf-8
from emotion.utils.FileUtil import get_single_msg
from emotion.core.Dispatcher import local_file_control_sample


def get_comment(dir_path):
    comment_list = []
    local_file_control_sample(comment_list, dir_path)
    return comment_list


def get_ten(path, comment_list):
    result_list = []
    msg_list = get_single_msg(path)
    params = ""
    for comment in comment_list:
        params += comment
    for singleKeys in msg_list:
        dict_org = {}
        item = params.count(singleKeys)
        dict_org['name'] = singleKeys
        dict_org['count'] = item
        result_list.append(dict_org)
    result_list_new = sorted(result_list, key=get_count, reverse=True)
    print(result_list_new[0:10])
    return get_name(result_list_new[0:10])


def get_count(dict_my):
    return dict_my['count']


def get_name(list_my):
    list_new = []
    for item_my in list_my:
        name = item_my['name']
        list_new.append(name)
    return list_new


def file_change(list_keys, comment_list):
    result_list = []
    for key in list_keys:
        item_list = []
        for comment in comment_list:
            count = comment.count(key)
            if count > 0:
                item_list.append(comment)
        result_list.append(item_list)
    return result_list


if __name__ == '__main__':
    print(get_ten('G:/pyhonProject/src/resources/keywords.txt', 'C:/emotion3'))
