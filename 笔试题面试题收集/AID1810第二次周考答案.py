import random
import math
# 1.	有一堆球，白球有4个，黄球有8个，黑球有12个，三种颜色的球放一起。现从中随机取出10个球，且必须有白球。编程实现：输出所有可能的取球方案，并统计总共有多少种方案。要求：
#     a)	使用函数封装功能；
#     b)	使用闭包结构封装功能；

#使用函数封装
def num_search():
    count = 0
    for i in range(1,5):
        for j in range(9):
            for k in range(10):
                if i + j + k == 10:
                    print(i,j,k)
                    count += 1
    return count

result = num_search()
print('总共有%d种取球方案。'%result)

#使用闭包结构封装
def out_():
    count = 0
    def in_():
        nonlocal count
        for i in range(1,5):
            for j in range(8):
                for k in range(10):
                    if i + j + k == 10:
                        print(i,j,k)
                        count += 1
        return count
    return in_
num_search = out_()
result = num_search()
print('总共有%d种取球方案。'%result)



# 2.	生成一个斐波那契数列(生成20个元素即可)。要求
#     a)	使用基本算法进行实现
#     b)	使用递归方式进行实现
#     c)	使用函数封装功能

#基本算法实现

def fib():
    l = [0,1]
    for i in range(2,21):
        l.append(l[i-1] + l[i-2])
    return l
result = fib()
print('生成的斐波那契数列为：%s'%result)

递归方式实现
def fib(n):
    if n == 1:
        return 0
    elif n == 2:
        return 1
    else:
        return fib(n-1) + fib(n-2)

def fib_list():
    l = []
    for i in range(1,21):
        l.append(fib(i))
    return l
result = fib_list()
print('生成的斐波那契数列为:%s'%result)

# 3.	接上题，将生成的斐波那契序列打散为随机序列并重新按照升序进行排序。要求：使用函数封装功能

def make_random(l):
    for i in range(10):
        j = math.floor(random.random()*19 + 1)
        k = math.floor(random.random()*19 + 1)
        l[j],l[k] = l[k],l[j]
    return l
res = make_random(fib_list())
print('斐波那契数列打散后的随机序列为：%s'%res)

def bubble_sort(l):
    for i in range(len(l)-1):
        for j in range(len(l)-1-i):
            if l[j] < l[j+1]:
                l[j],l[j+1] = l[j+1],l[j]
    return l

resu = bubble_sort(make_random(fib_list()))
print('打散后的斐波那契数列重新排序后为：%s'%resu)


# 4.	使用随机模块生成20个元素的随机序列。要求：使用函数封装功能


def random_list():
    l = []
    while True:
        num = math.floor(random.random()*20 + 1)
        l.append(num)
        if len(l) == 20:
            break
    return l

res = random_list()
print('生成的随机序列为：%s'%res)


# 5.	接上题，针对当前随机序列，输出当前序列中出现次数最多的字符，并统计次数。要求：使用函数封装功能

def make_dic(l):
    dic = {}
    for i in l:
        if i not in dic:
            dic[i] = 1
        else:
            dic[i] += 1
    return dic
res_dic = make_dic(random_list())
print('生成的字典为：%s'%res_dic)


def print_result(dic):
    iMax = 0
    iIndex = ''
    for i in dic:
        if dic[i] > iMax:
            iMax = dic[i]
            iIndex = i
    print('出现次数最多的字符是：%s,出现次数为：%d次'%(iIndex,iMax))

print_result(make_dic(random_list()))


# 6.	接第4题，基于当前随机序列，将当前随机序列按照完全二叉树的结构输出。
def make_erchashu(l):
    number_count=1
    row_number=1   
    print("形成的完全二叉树结构为：")
    for i in range(len(l)):
        if i==number_count:
            number_count += 2 ** row_number
            print("\n")
            row_number += 1
        print (l[i],end="  ")
make_erchashu(random_list())
