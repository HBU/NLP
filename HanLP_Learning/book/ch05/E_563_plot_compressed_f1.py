# -*- coding:utf-8 -*-# Author：hankcs# Date: 2018-06-22 17:53
# 《自然语言处理入门》5.6.3 特征裁剪与模型压缩
import sys
import os
# 得到当前根目录
o_path = os.getcwd() # 返回当前工作目录
sys.path.append(o_path) # 添加自己指定的搜索路径

from jpype import JClass
from book.ch03.E_351_eval_bigram_cws import CWSEvaluator
from book.ch03.E_322_msr import msr_train, msr_model, msr_gold, msr_dict, msr_output, msr_test
from book.ch05.E_560_perceptron_cws import CWSTrainer, PerceptronLexicalAnalyzer
import matplotlib.pyplot as plt

plt.rcParams['font.sans-serif'] = ['SimHei']  # 用来正常显示中文标签
plt.rcParams['axes.unicode_minus'] = False  # 用来正常显示负号


def train_evaluate(ratios):
    # model = CWSTrainer().train(msr_train, msr_train, msr_model, 0, 1, 8).getModel()  # 训练模型
    model = JClass('com.hankcs.hanlp.model.perceptron.model.LinearModel')(msr_model)
    pre = -1
    scores = []
    for c in ratios:
        if c > 0:
            print('以压缩比{}压缩模型中...'.format(c))
            model.compress(1 - (1 - c) / pre, 0)
        pre = 1 - c
        result = CWSEvaluator.evaluate(PerceptronLexicalAnalyzer(model).enableCustomDictionary(False),
                                       msr_test, msr_output, msr_gold, msr_dict)
        scores.append(result.F1)
    return scores


if __name__ == '__main__':
    x = [c / 10 for c in range(0, 10)]
    y = train_evaluate(x)
    plt.title("压缩率对准确率的影响")
    plt.xlabel("压缩率")
    plt.ylabel("准确率")
    plt.xticks([c / 10 for c in range(0, 11)])
    # plt.ylim(min(y), max(y))
    plt.plot(x, y, color='b')
    plt.grid()
    plt.show()
