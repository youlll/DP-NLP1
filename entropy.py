#coding=utf-8
from math import log
import jieba
sign = '“”，。？、|！~·@#￥%…&*（）——+-={}【】；‘’《》「」：'
with open(r'inf.txt') as titlefile:
    titlestr = titlefile.read()
    title = titlestr.split(',')
while True:
    modelcmd = input('请输入信息熵计算方式（1按字算，2按词算）：')
    if modelcmd=='1' or modelcmd=='2':
        break
for i in range(len(title)):
    existword = []
    existwordnum = []
    wordnum = 0
    myEntropy = 0
    with open(title[i]+'.txt',encoding='ANSI') as f:
        fstr = f.read()
        if modelcmd=='1':
            content = list(fstr)
        elif modelcmd=='2':
            content = jieba.lcut(fstr)
        #第i篇的第j个字或词
        for j in range(len(content)):
            if content[j] not in sign:
                try:
                    #之前有这个字或词就计数加1
                    wordindex = existword.index(content[j])
                    existwordnum[wordindex] = existwordnum[wordindex]+1
                except:
                    #之前没这个字或词就添加到列表并初始化计数为1
                    existword.append(content[j])
                    existwordnum.append(1)
                finally:
                    wordnum = wordnum + 1
        for k in range(len(existwordnum)):
            p = existwordnum[k]/wordnum
            myEntropy = myEntropy - p*log(p,2)
        print(title[i]+':',myEntropy)
    