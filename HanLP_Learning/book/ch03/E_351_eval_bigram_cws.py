# -*- coding:utf-8 -*-# Author：hankcs# Date: 2018-06-07 15:25
# 《自然语言处理入门》3.5.1 标准化评测
import sys
import os
# 得到当前根目录
o_path = os.getcwd() # 返回当前工作目录
sys.path.append(o_path) # 添加自己指定的搜索路径

from pyhanlp import *
from book.ch03.E_322_msr import msr_dict, msr_train, msr_model, msr_test, msr_output, msr_gold
from book.ch03.E_330_ngram_segment import train_bigram, load_bigram

CWSEvaluator = SafeJClass('com.hankcs.hanlp.seg.common.CWSEvaluator')

if __name__ == '__main__':
    train_bigram(msr_train, msr_model)  # 训练
    segment = load_bigram(msr_model)  # 加载
    result = CWSEvaluator.evaluate(segment, msr_test, msr_output, msr_gold, msr_dict)  # 预测打分
    print(result)
