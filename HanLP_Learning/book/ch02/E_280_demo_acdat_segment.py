# -*- coding:utf-8 -*-# Author：hankcs# Date: 2018-05-29 13:51
# 《自然语言处理入门》2.8 HanLP 的词典分词实现

from pyhanlp import *

HanLP.Config.ShowTermNature = False
segment = JClass('com.hankcs.hanlp.seg.Other.AhoCorasickDoubleArrayTrieSegment')()
print(segment.seg("江西鄱阳湖干枯，中国最大淡水湖变成大草原"))