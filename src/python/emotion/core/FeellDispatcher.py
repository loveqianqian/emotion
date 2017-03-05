# encoding: utf-8
from emotion.core.Dispatcher import local_file_control_sample
from emotion.utils.FileUtil import get_file_name
from emotion.utils.FileUtil import get_file_path


def get_feeling(path, myKeys):
    comment_list = []
    result_list = [0, 0, 0, 0, 0, 0, 0, 0, 0]
    local_file_control_sample(comment_list, path)
    params = ""
    for comment in comment_list:
        params += comment
    # print(params)
    if params != "":
        x_item = 0
        for singleKeys in myKeys:
            total_item = 0
            for key in singleKeys:
                item = params.count(key)
                total_item += item
            result_list[x_item] = total_item
            x_item += 1
    # total_count = 0
    # for item in result_list:
    #     total_count += item
    result_item_count = 0
    for result_item in result_list:
        # result_list[result_item_count] = result_item / total_count
        result_list[result_item_count] = result_item
        result_item_count += 1

    return result_list


def any_feeling(path, feel_path):
    name_list = get_file_name(feel_path)
    path_list = get_file_path(feel_path)
    params_list = []
    for my_path in path_list:
        # print(my_path)
        my_file = open(my_path, "r+", encoding="utf8")
        my_text = my_file.read()
        params_list.append(my_text.splitlines())
        my_file.close()
    count_list = get_feeling(path, params_list)
    result_list = []
    for i in range(len(path_list)):
        result_list.append(name_list[i] + ':' + str(count_list[i]))
    return result_list


def any_feeling_other(msg, feel_path):
    name_list = get_file_name(feel_path)
    path_list = get_file_path(feel_path)
    params_list = []
    for my_path in path_list:
        # print(my_path)
        my_file = open(my_path, "r+", encoding="utf8")
        my_text = my_file.read()
        params_list.append(my_text.splitlines())
        my_file.close()
    count_list = get_feeling(msg, params_list)
    result_list = []
    for i in range(len(path_list)):
        result_list.append(name_list[i] + ':' + str(count_list[i]))
    return result_list


def get_feeling(msg, myKeys):
    result_list = [0, 0, 0, 0, 0, 0, 0, 0, 0]
    params = ""
    for comment in msg:
        params += comment
    # print(params)
    if params != "":
        x_item = 0
        for singleKeys in myKeys:
            total_item = 0
            for key in singleKeys:
                item = params.count(key)
                if item > 0:
                    print(str(x_item + 1) + ":" + key)
                total_item += item
            result_list[x_item] = total_item
            x_item += 1
    # total_count = 0
    # for item in result_list:
    #     total_count += item
    result_item_count = 0
    for result_item in result_list:
        # result_list[result_item_count] = result_item / total_count
        result_list[result_item_count] = result_item
        result_item_count += 1

    return result_list


if __name__ == '__main__':
    print(get_feeling('C:\emotion3', [[]]))
