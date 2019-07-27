import re
import requests
import pandas
from lxml import etree

PAGE = eval(input('要几页：'))
header = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.100 Safari/537.36'}
get_url1 = requests.get('http://www.lottery.gov.cn/historykj/history.jspx?_ltype=plw',headers = header)
get_urln = requests.get('http://www.lottery.gov.cn/historykj/history_%d.jspx?_ltype=plw',PAGE,headers = header)
NList = []   # 数字集合
DataL = []   # 时间
QShuL = []   # 期数
ResLi = []   # 转换为要保存的7维数组
get_url1.decode = 'UTF-8'
get_urln.decode = 'UTF-8'
html1 = etree.HTML(get_url1.text)
htmln = etree.HTML(get_urln.text)
num = html1.xpath('/html/body/div[3]/div[2]/div[2]/table/tbody/tr/td[2]')
data = html1.xpath('/html/body/div[3]/div[2]/div[2]/table/tbody/tr/td[8]')
qishu = html1.xpath('/html/body/div[3]/div[2]/div[2]/table/tbody/tr/td[1]')


for item1 in num:
    NList.append(item1.text)
for dt1 in data:
    DataL.append(dt1.text)
for qs1 in qishu:
    QShuL.append(qs1.text)
for itemn in num:
    NList.append(itemn.text)
for dtn in data:
    DataL.append(dtn.text)
for qsn in qishu:
    QShuL.append(qsn.text)


# 先把NList整成list合集，再交叉添加列表
NListNEW = []
for i in NList:
    x = i.split(' ')
    NListNEW.append(x)

# 交叉加列表
for i in range(len(DataL)):
    if DataL:
        ResLi.append(DataL.pop())
    if QShuL:
        ResLi.append(QShuL.pop())
    if NListNEW:
        ResLi.extend(NListNEW.pop())

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

