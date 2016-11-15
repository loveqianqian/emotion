# encoding: utf-8
from emotion.core.Classification import classification_emotion
from emotion.core.Dispatcher import local_file_control
from emotion.core.FeellDispatcher import any_feeling
from emotion.utils.DependUtil import weights_list

key = ['力荐', '推荐', '还行', '较差', '很差']  # 评论的种类,算法对于差评的认知水平较差.
weight_score = [1, 1, 1, 1, 1]


# weight_score = [0.74, 0.64, 0.4, 1.26, 1.96]

# feeling
# like = ['喜欢', '高兴', '喜悦', '兴奋', '幸福', '热情', '乐趣', '满足', '喜爱', '感动', '激动', '惊喜', '珍惜', '接纳', '包容']
# miss = ['怀念', '思念', '想念', '怀念', '回忆']
# expect = ['好奇', '惊奇', '渴望', '盼望', '希望', '期盼', '期待']
# worship = ['虔诚', '恭敬', '尊敬', '崇拜', '羡慕']
#
# angry = ['愤怒', '愤怒', '生气', '失望', '绝望', '后悔']
# sorrow = ['悲哀', '悲伤', '孤独', '悲痛', '凄凉', '悲惨', '悲哀', '哀伤']
# fear = ['恐惧', '惊吓', '恐惧', '害怕', '自卑', '负罪', '惊骇']
# disgust = ['厌恶', '羞耻', '尴尬', '羞愧', '侮辱', '耻辱', '惭愧', '厌恶', '烦恼', '厌烦', '讨厌', '憎恨', '反感', '鄙视', '恶心']


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


def show_feeling(path, feel_path):
    result_list = any_feeling(path, feel_path)
    print(result_list)


# 主函数
if __name__ == '__main__':
    # 极性分析(需要看极性分析的结果，去掉下面一行的注释就可以)
    # print('result:' + str(show_result('C:/emotion')))
    # 权重分析(需要看权重分析的结果，去掉下面两行的注释就可以)
    # my_result = show_weights('C:/emotion')
    # print(my_result[0:9])
    # 情感分析(需要看情感分析的结果，去掉下面一行的注释就可以)
    print(any_feeling('C:/emotion3', 'C:/feel'))
