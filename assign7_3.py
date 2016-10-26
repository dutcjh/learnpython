"""
1）	读入该文件，统计并输出单词的个数
2）	返回单词列表（注意：指返回单词列表即可，不要在屏幕上显示）
"""
import re

def loadWords(path):
    words = []
    rule = re.compile(r"[^a-z'-]|-{2,}")  # 匹配所有的非小写字母,’和连字符
    with open(path, 'r') as fp:
        for line in fp.readlines():
            line = line.lower()  # 将字符串变成小写
            line = rule.sub(' ', line)  # 去除字符串中所有的非字母符号
            words += line[:-1].split()  # 按空格或换行符拆成单词
        words = sorted(list(set(words)))  # 去重，并排序
        if 'i' in words:  # 对单词I进行特殊处理
            words[words.index('i')] = 'I'
    return len(words), words   # 返回单词个数和单词列表

path = 'words.txt'
n, w_lst = loadWords(path)
print(n)
with open('Word_list.txt', 'w') as fw:
    fw.writelines([line+'\n' for line in w_lst])
