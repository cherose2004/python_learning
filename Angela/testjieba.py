import jieba
# 中文分词库
a = "太上皇打天下到一半挂了"
b = "我想听幸福的一家"

jieba.add_word("我想听")
jieba.add_word("想听")
jieba.add_word("我想")
res = list(jieba.cut(b))
print(res)
res2 = list(jieba.cut_for_search(b))
print(res2)