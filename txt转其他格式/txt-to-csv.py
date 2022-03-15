# coding = utf-8

import pandas as pd

# 检验是否含有中文字符
# 函数来自网址页面：https://segmentfault.com/a/1190000017940752
def is_contains_chinese(strs):
    for _char in strs:
        if '\u4e00' <= _char <= '\u9fa5':
            return True
    return False

nameFile = open('New_Recourse.txt', 'r', encoding = 'utf-8')
curLine = ''
cnList = []
enList = []

for lines in nameFile:
    curLine = nameFile.readline()

    if not curLine:
        continue

    curLine = curLine.replace('\n', '')
    lineContent = curLine.split('\t')

    if(len(lineContent) != 2):
        continue
    
    if(is_contains_chinese(lineContent[0]) == True):
        cnList.append(lineContent[0])
        enList.append(lineContent[1])
    else:
        cnList.append(lineContent[1])
        enList.append(lineContent[0])

#dataNames = [enList, cnList]
#print(len(dataNames[0]))
#print(len(dataNames[1]))

df = pd.DataFrame({'enName':enList, 'cnName':cnList})

df.to_csv("Translations.csv", index = False, sep = ',', encoding = 'utf-8-sig')
