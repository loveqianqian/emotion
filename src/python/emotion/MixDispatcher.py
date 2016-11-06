# encoding: utf-8
from emotion.NoUseSdkCore import analysis_list
from emotion.Dispatcher import local_file_control
from emotion.NoUseSdkCore import weights_list

key = ['力荐', '还行', '差评']


# 解析，包装,极性分析
def show_result(path):
    comment_list = []
    positive, negative = 0, 0
    local_file_control(comment_list, path, key)
    list_num = len(comment_list)
    num = int(list_num / 1500)
    if list_num > 1500:
        # print('num:' + str(num))
        for i in range(num):
            # print('i:' + str(i))
            temp_list = comment_list[1500 * i:1500 * i + 1500]
            temp = ','
            result = temp.join(temp_list)
            analysis = analysis_list(result).replace('[[', '').replace(']]', '')
            temp_result = analysis.split(",")
            positive += float(temp_result[0])
            negative += float(temp_result[1])
        temp_list = comment_list[1500 * num:]
        temp = ','
        result = temp.join(temp_list)
        analysis = analysis_list(result).replace('[[', '').replace(']]', '')
        temp_result = analysis.split(",")
        positive += float(temp_result[0])
        negative += float(temp_result[1])
    else:
        temp_list = comment_list[0:]
        temp = ','
        result = temp.join(temp_list)
        analysis = analysis_list(result).replace('[[', '').replace(']]', '')
        temp_result = analysis.split(",")
        positive += float(temp_result[0])
        negative += float(temp_result[1])

    real_positive = positive / (num + 1)
    real_negative = negative / (num + 1)
    my_array = [real_positive, real_negative]
    return my_array


def show_weights(path):
    comment_list = []
    this_result = {}
    local_file_control(comment_list, path,key)
    list_num = len(comment_list)
    num = int(list_num / 1500)
    if list_num > 1500:
        # print('num:' + str(num))
        for i in range(num):
            # print('i:' + str(i))
            temp_list = comment_list[1500 * i:1500 * i + 1500]
            temp = ','
            result = temp.join(temp_list)
            weights = weights_list(result)
            for my_weight, my_word in weights.json():
                if my_word not in this_result:
                    this_result[my_word] = my_weight
                else:
                    org_value = this_result[my_word]
                    temp_value = org_value + my_weight
                    this_result[my_word] = temp_value

        temp_list = comment_list[1500 * num:]
        temp = ','
        result = temp.join(temp_list)
        weights = weights_list(result)
        for my_weight, my_word in weights.json():
            if my_word not in this_result:
                this_result[my_word] = my_weight
            else:
                org_value = this_result[my_word]
                temp_value = org_value + my_weight
                this_result[my_word] = temp_value
    else:
        temp_list = comment_list[0:]
        temp = ','
        result = temp.join(temp_list)
        weights = weights_list(result)
        for my_weight, my_word in weights.json():
            if my_word not in this_result:
                this_result[my_word] = my_weight
            else:
                org_value = this_result[my_word]
                temp_value = org_value + my_weight
                this_result[my_word] = temp_value

    return sorted(this_result.items(), key=lambda d: d[1], reverse=True)


# 主函数
if __name__ == '__main__':
    # 极性分析
    print('result:' + str(show_result('C:\emotion2')))
    # 权重分析
    # my_result = show_weights('C:\emotion')
    # print(my_result[0:9])
