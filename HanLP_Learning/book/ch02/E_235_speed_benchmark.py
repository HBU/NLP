# -*- coding:utf-8 -*-# Author：hankcs# Date: 2018-05-25 10:21
# 《自然语言处理入门》2.3.5 速度评测
import sys
import os
# 得到当前根目录
o_path = os.getcwd() # 返回当前工作目录
sys.path.append(o_path) # 添加自己指定的搜索路径
import time

from E_233_backward_segment import backward_segment
from E_234_bidirectional_segment import bidirectional_segment
from E_232_forward_segment import forward_segment
from E_222_utility import load_dictionary


def evaluate_speed(segment, text, dic):
    start_time = time.time()
    for i in range(pressure):
        segment(text, dic)
    elapsed_time = time.time() - start_time
    print('%.2f 万字/秒' % (len(text) * pressure / 10000 / elapsed_time))


if __name__ == '__main__':
    text = "江西鄱阳湖干枯，中国最大淡水湖变成大草原"
    pressure = 10000
    dic = load_dictionary()

    print('由于JPype调用开销巨大，以下速度显著慢于原生Java')
    evaluate_speed(forward_segment, text, dic)
    evaluate_speed(backward_segment, text, dic)
    evaluate_speed(bidirectional_segment, text, dic)
