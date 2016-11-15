# coding: utf-8
import os


# 遍历文件
def get_file(root_dir, r_list):
    for myDir in os.listdir(root_dir):
        path = os.path.join(root_dir, myDir)
        if os.path.isdir(path):
            get_file(path, r_list)
        if os.path.isfile(path):
            r_list.append(path)


def get_file_path(root_dir):
    result_list_temp = []
    for myDir in os.listdir(root_dir):
        path = os.path.join(root_dir, myDir)
        result_list_temp.append(path)
    return result_list_temp


def get_file_name(root_dir):
    result_list_temp = []
    result_list = []
    for root, dirs, files in os.walk(root_dir):
        for file_name in files:
            result_list_temp.append(file_name)
    for temp in result_list_temp:
        result_list.append(temp.split(".")[0])
    return result_list


if __name__ == '__main__':
    # result_list = []
    # get_file("C:\emotion", result_list)
    # print(result_list)
    print(get_file_name('C:/feel'))
    print(get_file_path('C:/feel'))
