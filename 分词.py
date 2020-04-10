import jieba

import jieba

text = "高血压是最常见的慢性病，也是心脑血管病最主要的危险因素。"
# jieba.cut直接得到generator形式的分词结果
seg = jieba.cut(text)
print(' '.join(seg))

# 也可以使用jieba.lcut得到list的分词结果
seg = jieba.lcut(text)
print(seg)