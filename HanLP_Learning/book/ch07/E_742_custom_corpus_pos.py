# 《自然语言处理入门》7.4.2 标注语料
import sys
import os
# 得到当前根目录
o_path = os.getcwd() # 返回当前工作目录
sys.path.append(o_path) # 添加自己指定的搜索路径
from tests.book.ch07.demo_hmm_pos import AbstractLexicalAnalyzer, PerceptronSegmenter
from tests.book.ch07.demo_perceptron_pos import train_perceptron_pos
from test_utility import ensure_data

ZHUXIAN = ensure_data("zhuxian", "http://file.hankcs.com/corpus/zhuxian.zip") + "/train.txt"
posTagger = train_perceptron_pos(ZHUXIAN)  # 训练
analyzer = AbstractLexicalAnalyzer(PerceptronSegmenter(), posTagger)  # 包装
print(analyzer.analyze("陆雪琪的天琊神剑不做丝毫退避，直冲而上，瞬间，这两道奇光异宝撞到了一起。"))  # 分词+标注
