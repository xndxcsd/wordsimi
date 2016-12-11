# -*- coding: utf-8 -*-
import xlrd
import xlwt

from VecDispatcher import VecDispatcher


def strToFloat(num):
    try:
        f = float(num)
    except:
        f = 0.0
    return f


def computeCosine(vec1, vec2):
    if len(vec1) != len(vec2):
        print('error input,vec1 and vec2 is not in the same space')
        return
    result1 = 0.0
    result2 = 0.0
    result3 = 0.0
    for i in range(len(vec1)):
        result1 += vec1[i] * vec2[i]  # sum(vec1*vec2)
        result2 += vec1[i] ** 2  # sum(vec1*vec1)
        result3 += vec2[i] ** 2  # sum(vec2*vec2)
    return str(result1 / ((result2 * result3) ** 0.5) *10)  # 结果显示


vecdispatcher = VecDispatcher()  # vecdispatcher对象负责获取词向量

dataBook = xlrd.open_workbook('evatestdata3.xls')  # 打开testdata
table = dataBook.sheets()[0]  # 打开第一张表
nrows = table.nrows  # 获取表的行数

newBook = xlwt.Workbook(encoding='utf-8')
answerSheet = newBook.add_sheet('answer sheet')
for i in range(nrows):  # 循环逐行打印
    # if i == 10:
    #     break

    if i == 0:  # 跳过第一行
        continue
    word1 = table.row_values(i)[1].encode('utf-8')  # 取第一个词
    word2 = table.row_values(i)[2].encode('utf-8')  # 取第二个词

    vec1 = vecdispatcher.getVector(word1)
    if vec1 is None:  # 语料库中没有该词，则跳过该词
        cosine=str(0.0)
    else:
        vec2 = vecdispatcher.getVector(word2)
        if vec2 is None:  # 语料库中没有该词，则跳过该词
            cosine=str(0.0)
        else:
            cosine = computeCosine(vec1, vec2)

    if cosine is None:
        cosine = -1.0  # 鲁棒性考虑
    else:
        pass
    print("process: %.2f%%" % (1.0 * i / nrows * 100))  # 打印一下进度

    answerSheet.write(i, 0, word1)
    answerSheet.write(i, 1, word2)
    answerSheet.write(i, 2, cosine)

newBook.save('answer.xls')
