#-*-coding:utf-8-*-
def isonePrime(num):
    '判断一个数是不是素数'
    num = int(num)
    if num <= 2:
        print('这是一个素数')
    elif num < 0:
        print('请去问你的数学老师，谢谢')
    else:
        for i in range(2,num):
            if num % i == 0:
                print('这不是一个素数')
            else:
                print('这是一个素数')
def saePrime(a,b):
    '求一个数值范围内的素数'
    for num in range(a,b+1):
        if num <= 2 and num > 0 :
            print(num)
        elif num < 0:
            print('请输入正整数的范围')
        else:
            flage = False
            for i in range(2,num):
                if num % i == 0:
                    flage = True
                    break
            if flage :
                continue
            else :
                print(num)

print('='*9+'你可以输入一个正整数的数值范围来求其中所有的素数'+'='*9)
tip_start = input('请输入起始的数值：')
tip_end = input('请输入结束的数值：')
tip_start = int(tip_start)
tip_end = int(tip_end)
saePrime(tip_start,tip_end)
'''
for num in range(tip_start,tip_end):
    if num <= 2 and num > 0 :
        print(num)
    elif num < 0:
        print('请输入正整数的范围')
    else:
        flage = False
        for i in range(2,num):
            if num % i == 0:
                flage = True
                break
        if flage :
            continue
        else :
            print(num)
'''

