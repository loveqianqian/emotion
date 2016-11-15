# encoding: utf-8
from emotion.core.Dispatcher import local_file_control_sample


def get_feeling(path, myKeys):
    comment_list = []
    result_list = [0, 0, 0, 0, 0, 0, 0, 0]
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
    total_count = 0
    for item in result_list:
        total_count += item
    result_item_count = 0
    for result_item in result_list:
        result_list[result_item_count] = result_item / total_count
        result_item_count += 1

    return result_list


if __name__ == '__main__':
    print(get_feeling('C:\emotion3', [[]]))
