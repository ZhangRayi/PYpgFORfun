# 究极简单版本

import random
while True:
    n = int(input('大乐透: 1, 排列3: 3, 排列5: 5, 七星彩: 7。'))
    # 大乐透
    if n == 1:
        listQ = range(1,36)
        listH = range(1,13)
        qianqu = random.sample(listQ,5)
        houqu = random.sample(listH,2)
        qianqu.sort()
        houqu.sort()
        print('机选号码：',end = '')
        for qq in qianqu:
            print(qq,end = '  ')
        print('+',end = ' ')
        for hq in houqu:
            print(hq,end = '  ') 
        print()
    
    # 排列三
    elif n == 3:
        pl3 = []
        for i in range(3):
            a = random.randint(0,9)
            pl3.append(a)
        print('机选排三：',end = '')
        for p in pl3:
            print(p,end = '  ')
        print()
    
    # 排列五
    elif n == 5:    # 排列5
        pl5 = []
        for x in range(5):
            b = random.randint(0,9)
            pl5.append(b)
        print('机选排五：',end = '')
        for l in pl5:
            print(l,end = '  ')
        print()
    
    # 七星彩
    elif n == 7:    # 七星彩
        qxc = []
        for y in range(7):
            c = random.randint(0,9)
            qxc.append(c)
        print('机选七星彩：',end = '')
        for qx in qxc:
            print('{:2}'.format(qx),end = ' ')
        print()
        
    else:
        print('{:X^21}'.format(' 输错了，告辞！'))
        break
    print('{:$^20}'.format(' 请记下数字哦 '))
print('{:-^18}'.format('这次输入什么都会退出'))
input()