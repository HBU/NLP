# -*- coding:utf-8 -*-# Author：hankcs# Date: 2018-06-22 17:53
# 《自然语言处理入门》5.6.3 特征裁剪与模型压缩
import sys
import os
# 得到当前根目录
o_path = os.getcwd() # 返回当前工作目录
sys.path.append(o_path) # 添加自己指定的搜索路径

from tempfile import NamedTemporaryFile

import numpy as np

__doc__ = '试验语料库规模对准确率的影响'

from book.ch03.E_351_eval_bigram_cws import CWSEvaluator
from book.ch03.E_322_msr import msr_train, msr_model, msr_gold, msr_dict, msr_output, msr_test
from book.ch05.E_560_perceptron_cws import CWSTrainer, PerceptronLexicalAnalyzer
import matplotlib.pyplot as plt

plt.rcParams['font.sans-serif'] = ['SimHei']  # 用来正常显示中文标签
plt.rcParams['axes.unicode_minus'] = False  # 用来正常显示负号


def train_evaluate(ratio):
    partial_corpus = NamedTemporaryFile(delete=False).name
    with open(msr_train,'r', encoding='UTF-8') as src, open(partial_corpus, 'w') as dst:
        all_lines = src.readlines()
        dst.writelines(all_lines[:int(ratio * len(all_lines))])

    model = CWSTrainer().train(partial_corpus, partial_corpus, msr_model, 0, 50, 8).getModel()  # 训练模型
    result = CWSEvaluator.evaluate(PerceptronLexicalAnalyzer(model).enableCustomDictionary(False),
                                   msr_test, msr_output, msr_gold, msr_dict)
    return result.F1


if __name__ == '__main__':
    x = [r / 10 for r in range(1, 11)]
    y = [train_evaluate(r) for r in x]
    plt.title("语料库规模对准确率的影响")
    plt.xlabel("语料库规模（万字符）")
    plt.ylabel("准确率")
    plt.xticks([int(r / 10 * 405) for r in range(1, 11)])
    plt.yticks(np.arange(91, 97.5, 0.5))
    plt.plot([int(r / 10 * 405) for r in range(1, 11)], y, color='b')
    plt.grid()
    plt.show()
