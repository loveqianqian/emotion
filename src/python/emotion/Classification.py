# encoding: utf-8
from emotion.NoUseSdkCore import analysis_list
from emotion.Dispatcher import local_file_control_for_emotion


def classification_emotion(path, key, score):
    positive, negative = 0, 0
    count = 0
    for item in key:
        item_score = score[count]
        my_array = calculation_emotion(path, item)
        positive += float(my_array[0]) * float(item_score)
        negative += float(my_array[1]) * float(item_score)
        count += count
    total_count = 0
    for temp in score:
        total_count += float(temp)
    result_array = [positive / total_count, negative / total_count]
    return result_array


def calculation_emotion(path, item_key):
    comment_list = []
    positive, negative = 0, 0
    local_file_control_for_emotion(comment_list, path, item_key)
    list_num = len(comment_list)
    num = int(list_num / 1500)
    if list_num > 1500:
        for i in range(num):
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
