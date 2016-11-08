# encoding: utf-8
from emotion.Dispatcher import local_file_control
from emotion.NoUseSdkCore import weights_list
from emotion.Classification import classification_emotion

key = ['力荐', '推荐', '还行', '较差', '很差']  # 评论的种类,算法对于差评的认知水平较差.
weight_score = [1, 1, 1, 1, 1]
# weight_score = [0.74, 0.64, 0.4, 1.26, 1.96]


def show_result(path):
    my_array = classification_emotion(path, key, weight_score)
    return my_array


def show_weights(path):
    comment_list = []
    this_result = {}
    local_file_control(comment_list, path)
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
    print('result:' + str(show_result('C:\emotion3')))
    # 权重分析
    # my_result = show_weights('C:\emotion')
    # print(my_result[0:9])
