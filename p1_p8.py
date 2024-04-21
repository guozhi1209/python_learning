# 转义字符\
# \\->\, \'->', \"->", \a->bel响铃，\b退格符，\n换行符，\t水平制表符，\v垂直制表符，\r回车符，\f换页符
# \ooo(ooo为八进制数)，\xhh(hh为十六进制数)
print('\"Life is short,let\'s learn python.\"')
# 加r原始字符串不再有效
print(r'D:\three\two\one\now')
# 末尾加反斜杠\，代表还没完
print('i love y\
      ou')
# 长字符串用'''内容'''，或者"""内容"""
k='''我家门口有
两棵树
一颗是枣树
另外一棵枣树'''
print(k)
# 字符串相加是拼接，字符串*n,输出n个字符串

# 用python设计第一个游戏 if else, while, random(help python docs帮助文档)
# 获取随机数加工之后，随机数生成器的内部状态random.getstate(),random.setstate
import random
answer = random.randint(1,10)

counts = 3
while counts > 0:
    temp = input("猜一下我心里想的什么")
    guess = int(temp)
    if guess == answer:
        print('猜对了')
        print("猜中了也没奖励")
        break
    else:
        if guess < answer:
            print("小了")
        else:
            print("大啦")
        counts = counts - 1
print('游戏结束，不玩啦')

# 习题：输入一个数5输出12345 
counts = input('请输入一个整数：')
temp = int(counts)
begin = 1
while temp >= begin:
    print(begin)
    begin = begin + 1
    

print('i love you');print('I LOVE U')
# 习题：输入一个数，输出某种排列的*，多一个空格，因为默认（a,b）输出a b中间有空格，可以用‘’去掉
counts = input("请输入一个整数：")
temp = int(counts)
while temp:
    symbol2 = '*'* temp
    symbol1 = ' '* (temp - 1)
    
    print(symbol1,symbol2,sep='')
    temp = temp - 1



# 多行注释快捷键alt+shift+A