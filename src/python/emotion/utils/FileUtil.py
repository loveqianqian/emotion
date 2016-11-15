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


if __name__ == '__main__':
    result_list = []
    get_file("C:\emotion", result_list)
    print(result_list)
