import random

QQ = []
BUYt = [0]
n = len(QQ)

print('运行中，请等待...')

# 前区选号，且不重复
while n < 5:
    a1 = random.sample(range(36),1)
    b1 = random.sample(range(36),1)
    c1 = random.sample(range(36),1)
    d1 = random.sample(range(36),1)
    e1 = random.sample(range(36),1)
    # 求两个list中的共同元素,且不在BUYt这个list中
    if 0 in a1:
        a1.remove(0)
    if 0 in b1:
        b1.remove(0)
    if 0 in c1:
        c1.remove(0)
    if 0 in d1:
        d1.remove(0)
    if 0 in e1:
        e1.remove(0)
    if 0 in BUYt:
        BUYt.remove(0)
    else:
        for x in a1:
            if x in b1:
                if x in c1:
                    if x in d1:
                        if x in e1:
                            BUYt.append(x)
                            break
                        break
                    break
                break        
            break
    # 将不会重复的值加入前区值中（前区除重）
    for t in BUYt:
        if t not in QQ:
            QQ.append(t)
            n = len(QQ)
            print('已生成%d个数' % (n))


# 后区选号，且不重复
HQ = []
HQt = []

h = len(HQ)
Hlist = [1,2,3,4,5,6,7,8,9,10,11,12]

while h < 2:
    a2 = random.sample(Hlist,1)
    b2 = random.sample(Hlist,1)
    for y in a2:
        if y in b2:
            HQt.append(y)
        break
    #后区除重
    for z in HQt:
        if z not in HQ:
            HQ.append(z)
    h = len(HQ)
    

QQ.sort()
HQ.sort()
JS = (QQ,HQ)

# print('前区：',QQ)
# print('后区：',HQ)
print('\n')
print('机选号码：',JS)
print('\n')
print('亲，请在记下号数后，按 ENTER 以退出')
input()
