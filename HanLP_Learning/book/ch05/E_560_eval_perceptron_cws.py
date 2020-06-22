# -*- coding:utf-8 -*-# Author: hankcs# Date: 2019-06-01 11:07
# 《自然语言处理入门》5.6 基于结构化感知机的中文分词
import sys
import os
# 得到当前根目录
o_path = os.getcwd() # 返回当前工作目录
sys.path.append(o_path) # 添加自己指定的搜索路径
from pyhanlp import *
from book.ch03.E_322_msr import msr_train, msr_model, msr_test, msr_gold, msr_output, msr_dict

CWSTrainer = JClass('com.hankcs.hanlp.model.perceptron.CWSTrainer')
PerceptronLexicalAnalyzer = JClass('com.hankcs.hanlp.model.perceptron.PerceptronLexicalAnalyzer')
LinearModel = JClass('com.hankcs.hanlp.model.perceptron.model.LinearModel')
Segment = JClass('com.hankcs.hanlp.seg.Segment')
CWSEvaluator = JClass('com.hankcs.hanlp.seg.common.CWSEvaluator')


def trainStructuredPerceptron():
    model = CWSTrainer().train(msr_train, msr_train, msr_model, 0., 10, 8).getModel()
    return PerceptronLexicalAnalyzer(model).enableCustomDictionary(False)


def trainAveragedPerceptron():
    model = CWSTrainer().train(msr_train, msr_train, msr_model, 0., 10, 1).getModel()
    return PerceptronLexicalAnalyzer(model).enableCustomDictionary(False)


print("结构化感知机")
print(CWSEvaluator.evaluate(trainStructuredPerceptron(), msr_test, msr_output, msr_gold, msr_dict))
print("平均感知机")
print(CWSEvaluator.evaluate(trainAveragedPerceptron(), msr_test, msr_output, msr_gold, msr_dict))
