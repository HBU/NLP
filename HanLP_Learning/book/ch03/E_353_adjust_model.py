# -*- coding:utf-8 -*-# Author：hankcs# Date: 2018-06-08 15:34
# 《自然语言处理入门》3.5.3 调整模型
import sys
import os
# 得到当前根目录
o_path = os.getcwd() # 返回当前工作目录
sys.path.append(o_path) # 添加自己指定的搜索路径

from pyhanlp import HanLP
from E_322_msr import msr_model
from E_330_ngram_segment import load_bigram, CoreDictionary

segment = load_bigram(model_path=msr_model, verbose=False, ret_viterbi=False)
assert CoreDictionary.contains("管道")
text = "北京输气管道工程"
HanLP.Config.enableDebug()
print(segment.seg(text))