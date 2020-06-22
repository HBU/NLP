# -*- coding:utf-8 -*-# Author：hankcs# Date: 2018-06-19 14:33
# 《自然语言处理入门》4.6 隐马尔可夫模型应用于中文分词
import sys
import os
# 得到当前根目录
o_path = os.getcwd() # 返回当前工作目录
sys.path.append(o_path) # 添加自己指定的搜索路径

from pyhanlp import *
from book.ch03.E_351_eval_bigram_cws import CWSEvaluator
from book.ch03.E_322_msr import msr_dict, msr_train, msr_model, msr_test, msr_output, msr_gold

FirstOrderHiddenMarkovModel = JClass('com.hankcs.hanlp.model.hmm.FirstOrderHiddenMarkovModel')
SecondOrderHiddenMarkovModel = JClass('com.hankcs.hanlp.model.hmm.SecondOrderHiddenMarkovModel')
HMMSegmenter = JClass('com.hankcs.hanlp.model.hmm.HMMSegmenter')


def train(corpus, model):
    segmenter = HMMSegmenter(model)
    segmenter.train(corpus)
    print(segmenter.segment('商品和服务'))
    return segmenter.toSegment()


def evaluate(segment):
    result = CWSEvaluator.evaluate(segment, msr_test, msr_output, msr_gold, msr_dict)
    print(result)


if __name__ == '__main__':
    segment = train(msr_train, FirstOrderHiddenMarkovModel())
    evaluate(segment)
    segment = train(msr_train, SecondOrderHiddenMarkovModel())
    evaluate(segment)
