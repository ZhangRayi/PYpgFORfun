# 排列五开奖结果
# 结果绘成图？还是表格
# 后期可能会加上分析
# 估计得先存在.xlsx文件中
# Created by ZR

import requests
import re
import openpyxl
import os
import pandas
from lxml import etree

# 先取得几个网页数据
def GetUrl(page):
    header = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.100 Safari/537.36'}
    get_url1 = requests.get('http://www.lottery.gov.cn/historykj/history.jspx?_ltype=plw',headers = header)
    get_urln = requests.get('http://www.lottery.gov.cn/historykj/history_%d.jspx?_ltype=plw',page,headers = header)
    get_url1.encoding = 'UTF-8'
    get_urln.encoding = 'UTF-8'
    return get_url1,get_urln

# etree解析，Xpath提取
def AnalyzeUrl(get_url1,get_urln):
    # re分析
    '''
        for item in text1:
            num = re.findall(r'[0-9]+</td>',item)
            print(num)
    '''
    # Xpath提取
    NList = []
    DataL = []
    QShuL = []
    get_url1.decode = 'UTF-8'
    get_urln.decode = 'UTF-8'
    html1 = etree.HTML(get_url1.text)
    htmln = etree.HTML(get_urln.text)
    num1 = html1.xpath('/html/body/div[3]/div[2]/div[2]/table/tbody/tr/td[2]')
    data1 = html1.xpath('/html/body/div[3]/div[2]/div[2]/table/tbody/tr/td[8]')
    qshu1 = html1.xpath('/html/body/div[3]/div[2]/div[2]/table/tbody/tr/td[1]')
    numn = htmln.xpath('/html/body/div[3]/div[2]/div[2]/table/tbody/tr/td[2]')
    datan = htmln.xpath('/html/body/div[3]/div[2]/div[2]/table/tbody/tr/td[8]')
    qshun = htmln.xpath('/html/body/div[3]/div[2]/div[2]/table/tbody/tr/td[1]')
    for item1 in num1:
        NList.append(item1.text)
    for itemn in numn:
        NList.append(itemn.text)
    for dt1 in data1:
        DataL.append(dt1.text)
    for dtn in datan:
        DataL.append(dtn.text)
    for qs1 in qshu1:
        QShuL.append(qs1.text)
    for qsn in qshun:
        QShuL.append(qsn.text)
    return NList,DataL,QShuL

# 按照时间保存开奖结果到.xlsx文件
def SaveEX(NList,DataL,QShuL):
    ResLi = []
    DataS = []
    # 交叉列表
    for i in range(len(NList)):
        if DataL:
            ResLi.append(DataL.pop())
        if QShuL:
            ResLi.append(QShuL.pop())
        if NList:
            ResLi.append(NList.pop())
    # 变成7维数组
    NewRes = []
    a = 7
    b = 1
    for item in ResLi:
        while b <= 20:
            NewRes.append(list(ResLi[a*(b-1):a*b]))
            b += 1
    # 保存到文件
    ResNum = pandas.DataFrame(NewRes,columns=['开奖时间','期数','第一位','第二位','第三位','第四位','第五位'])
    ResNum.to_excel('C:\\Users\\ZM\\Desktop\\PL5.xlsx',sheet_name='排列五开奖结果',index=False)
    
    # To Be countinue
    
    return

# 建立训练集

# 使用matplotlib绘制走势图（waiting for）
def DrawPic():
    return

if __name__ == "__main__":
    l1 = list(range(2,10))
    for i in l1:
        GetUrl(i)
    
