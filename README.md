# blockChain
  NLP自然语言处理
  ====                                                  
# 一、功能
实现根据词性进行分词，短文本分类，命名体识别，自动摘要等功能
# 二、运行环境
代码对 Python 2/3 均兼容
全自动安装：easy_install jieba 或者 pip install jieba / pip3 install jieba
半自动安装：先下载 http://pypi.python.org/pypi/jieba/ ，解压后运行 python setup.py install
手动安装：将 jieba 目录放置于当前目录或者 site-packages 目录
通过 import jieba 来引用
# 三、项目进程
###
- 1.第一阶段
    - 1.分词 + 词性
    - 2.词频（关键词提取）
    - 3.词向量
- 2.第二阶段
    - 1.短文本分类
- 3.第三阶段
    - 1.命名体识别
- 4 .第四阶段
    - 1.自动摘要
    - 2.展示平台搭建
    - 3.数据集准备
------------------------------------------------------------------------------------------------------------------------------------------
## 第一阶段
我们基于TextRank算法对关键词抽取.
原理：TextRank是一种用于自然语言处理的通用基于图的排序算法，对于关键词提取，它使用一些文本单元集作为顶点来构建图。边是基于文本单元顶点之间的语义或词汇相似度的度量。并且，边缘通常是无向的，可以加权以反馈相似程度。一旦图形被构建，它就被用来形成一个随机矩阵，结合一个阻尼因子(如在“随机冲浪模型”中)，并且通过找到对应于特征值1的特征向量来获得顶点的排名(即在图上随机游走的平稳分布)。
