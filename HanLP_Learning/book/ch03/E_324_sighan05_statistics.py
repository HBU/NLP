# -*- coding:utf-8 -*-# Author：hankcs# Date: 2018-06-05 18:03
# 《自然语言处理入门》3.2.4 语料库统计
from collections import Counter

import sys
import os
# 得到当前根目录
o_path = os.getcwd() # 返回当前工作目录
sys.path.append(o_path) # 添加自己指定的搜索路径

from test_utility import ensure_data
import re # Add by David 2020.6.18

def count_corpus(train_path: str, test_path: str):
    train_counter, train_freq, train_chars = count_word_freq(train_path)
    test_counter, test_freq, test_chars = count_word_freq(test_path)
    test_oov = sum(test_counter[w] for w in (test_counter.keys() - train_counter.keys()))
    return train_chars / 10000, len(
        train_counter) / 10000, train_freq / 10000, train_chars / train_freq, test_chars / 10000, len(
        test_counter) / 10000, test_freq / 10000, test_chars / test_freq, test_oov / test_freq * 100


def count_word_freq(train_path):
    f = Counter()
    with open(train_path,'r', encoding='UTF-8') as src:
        for line in src:
            for word in re.compile("\\s+").split(line.strip()):
                f[word] += 1
    return f, sum(f.values()), sum(len(w) * f[w] for w in f.keys())


if __name__ == '__main__':
    sighan05 = ensure_data('icwb2-data', 'http://sighan.cs.uchicago.edu/bakeoff2005/data/icwb2-data.zip')
    print('|语料库|字符数|词语种数|总词频|平均词长|字符数|词语种数|总词频|平均词长|OOV|')
    for data in 'pku', 'msr', 'as', 'cityu':
        train_path = os.path.join(sighan05, 'training', '{}_training.utf8'.format(data))
        test_path = os.path.join(sighan05, 'gold',
                                 ('{}_testing_gold.utf8' if data == 'as' else '{}_test_gold.utf8').format(data))
        print(
            '|%s|%.0f万|%.0f万|%.0f万|%.1f|%.0f万|%.0f万|%.0f万|%.1f|%.2f%%|' % (
                (data.upper(),) + count_corpus(train_path, test_path)))
