"""
1）	读入该文件，统计并输出单词的个数
2）	返回单词列表（注意：指返回单词列表即可，不要在屏幕上显示）
"""
def loadWords(path):
    words = []
    with open(path, 'r') as fp:
        for line in fp.readlines():
            words += line[:-1].split()  # 按空格或换行符拆成单词
        words = sorted(list(set(words)))  # 去重，并按字母顺序排序
    return len(words), words   # 返回单词个数和单词列表

path = 'words.txt'
n, w_lst = loadWords(path)
print(n)
with open('Word_list.txt', 'w') as fw:
    fw.writelines([line+'\n' for line in w_lst])
