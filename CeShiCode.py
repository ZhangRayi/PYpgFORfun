import requests
from lxml import etree

Page = 2
GetPage = eval(input('要几页(输入数字n(2<n<100),之后按下回车)：'))
header = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.100 Safari/537.36'}

Get_url1 = requests.get('http://www.lottery.gov.cn/historykj/history.jspx?_ltype=plw',headers = header)
while Page < GetPage:
    Get_urln = requests.get('http://www.lottery.gov.cn/historykj/history_%d.jspx?_ltype=plw',Page,headers = header)
    
    
    
    Page += 1


print('尝试重新输入页数，并重试')
    



