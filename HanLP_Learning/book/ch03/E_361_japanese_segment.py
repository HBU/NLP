# -*- coding:utf-8 -*-# Author：hankcs# Date: 2018-06-07 18:37
# 《自然语言处理入门》3.6.1 日语分词语料
import sys
import os
# 得到当前根目录
o_path = os.getcwd() # 返回当前工作目录
sys.path.append(o_path) # 添加自己指定的搜索路径

from E_330_ngram_segment import train_bigram, load_bigram
from test_utility import ensure_data

jp_corpus = ensure_data('jpcorpus',
                        'http://file.hankcs.com/corpus/jpcorpus.zip')
jp_bigram = os.path.join(jp_corpus, 'jp_bigram')
jp_corpus = os.path.join(jp_corpus, 'ja_gsd-ud-train.txt')

if __name__ == '__main__':
    train_bigram(jp_corpus, jp_bigram)  # 训练
    segment = load_bigram(jp_bigram, verbose=False)  # 加载
    print(segment.seg('自然言語処理入門という本が面白いぞ！'))  # 日语分词
