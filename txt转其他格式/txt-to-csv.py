# coding = utf-8

import pandas as pd

# 检验是否含有中文字符
# 函数来自网址页面：https://segmentfault.com/a/1190000017940752
def is_contains_chinese(strs):
    for _char in strs:
        if '\u4e00' <= _char <= '\u9fa5':
            return True
    return False

nameFile = open('New_Recourse.txt', 'r', encoding = 'utf-8')        # 以UTF-8格式打开txt
skippedLines = open('skipped_lines.txt', 'w', encoding = 'utf-8')   # 新建一个txt保存跳过的行

curLine = ''
cnList = []
enList = []

for lines in nameFile:                      # 读取行
    curLine = nameFile.readline()

    if not curLine:                         # 若为空行，则直接跳转到下一行
        continue

    curLine = curLine.replace('\n', '')     # 去除换行符
    lineContent = curLine.split('\t')       # 以制表符为分隔符分割每行并转为list

    if(len(lineContent) != 2):              # 若当前行的列表长度不为2（明显不是中文-英文或英文-中文格式）则输出当前行到文件并跳到下一行
        skippedLines.write(curLine + '\n')  
        continue
    
    # 检测每行两个元素是否包含中文，并用flags列表标记
    flags = [is_contains_chinese(lineContent[0]), is_contains_chinese(lineContent[1])]

    if(flags == [True, False]):         # 第一个元素有中文，第二个没有
        cnList.append(lineContent[0])
        enList.append(lineContent[1])
    elif(flags == [False, True]):       # 第二个元素有中文，第一个没有
        cnList.append(lineContent[1])
        enList.append(lineContent[0])
    else:                               # 其他情况，输出当前行到文件并跳到下一行
        skippedLines.write(curLine + '\n')
        continue

df = pd.DataFrame({'enName':enList, 'cnName':cnList})   # 转为pandas库的DataFrame

df.to_csv("Translations.csv", index = False, sep = ',', encoding = 'utf-8-sig') # 按utf-8-sig编码写入csv，用Excel打开不乱码

# 关闭两个文件
nameFile.close()
skippedLines.close()
