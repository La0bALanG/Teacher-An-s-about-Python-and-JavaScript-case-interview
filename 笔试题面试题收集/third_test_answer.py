# AID1803第二次周考
# 1.编程实现功能：动态生成一个列表，然后将生成的列表进行排序，最后将排序后的列表进行去重（去掉重复的元素）。
# 要求：
#        	1.编写两种代码，第一种，用函数封装所有的功能；第二种：采用面向对象的编程思想，将完整功能分为三部分，每部分功能封装在一个类中，通过类与类之间的继承完成功能的整合；（提示：单继承？or多继承？自己想咯……）
# 			2.特殊情况的处理，比如：动态输入的列表的元素如果输入的不是整型数据而是字符串？该如何处理？
# 			3.排序功能不允许使用列表的常用方法及高阶函数，手写排序算法，任何一种排序算法都可以
# 			4.加分项：我们知道，几乎所有的递归都可以用循环来实现，那循环能否也可以用递归来实现呢？此问题部分使用到循环的功能如果能够用递归同样实现，加10分。
#  



#导入sys模块
# import sys as s

# #动态生成列表的类

# class Make_List:
#     def __init__(self):
#         self.L = []

#     def make_list(self):
#         while True:
#             try:
#                 num = int(input("请输入列表的元素，元素值类型为整型："))
#             except ValueError:
#                 print("您输入的元素的值类型不是整型！请重新输入！")
#                 s.exit()
#             if num == 0:
#                 break
#             self.L.append(num)

#         return self.L

# # a = Make_List()
# # print(a.make_list())

# #写一个排序类，先继承列表生成类，然后实现对列表的排序

# class List_sort(Make_List):
#     def __init__(self):
#         self.L = []
#     def list_sort(self):
#         super(List_sort,self).make_list()
#         for i in range(len(self.L)-1):
#             for j in range(len(self.L)-i-1-1):
#                 if self.L[j] > self.L[j+1]:
#                     self.L[j],self.L[j+1] = self.L[j+1],self.L[j]
#         return self.L

# # a = List_sort()
# # print(a.list_sort())

# #数组去重方法：排序法
# # l = [4,5,6,5,8,5,4,5,6,3,2,1,4,5,6,3,2,5,9,8,7,4,5,2]
# # l1 = []
# # L = sorted(l)
# # for i in L:
# #     if l[i] not in l1:
# #         l1.append(l[i])
# # print(l1)

# #写一个数组去重类，继承列表生成类及排序类，并完成数组去重功能

# class Delete_Repeat(List_sort):
#     def __init__(self):
#         self.newList = []
#         self.L = []
#     def delete_repeat(self):
#         super(Delete_Repeat,self).list_sort()
#         for y in self.L:
#             if y not in self.newList:
#                 self.newList.append(y)
#         return self.newList

# a = Delete_Repeat()
# print(a.delete_repeat())




#  
# 2.编写一个闹钟程序，启动时设置定时时间，到时间后打印“到点了，该起床啦！”
# 要求：
#        1.编写两种代码：第一种，用闭包封装其功能；第二种，采用面向对象封装其功能
#        2.特殊情况的处理：是否有异常情况出现？如果有，该怎么处理？
#  
#  



#原始方法
# import time
# h = int(input("请输入小时："))
# m = int(input("请输入分钟："))
# while True:
#     local_time = time.localtime()
# # print(local_time)
#     if(h,m) == local_time[3:5]:
#         print("时间到....")
#         break
#     print('\r%d:%d:%d'%local_time[3:6],end=' ')
#     time.sleep(1)



#改为闭包

# import time

# def alert():
#     hour = int(input("你想把闹钟定到几点："))
#     minute = int(input("你想把闹钟定到几分："))
#     def alert_ready():
#         nonlocal hour,minute
#         print("当前时间：")
#         while True:
#             local_time = time.localtime()
#             if (hour,minute) == local_time[3:5]:
#                 print("时间到,您该起床啦！！！")
#                 break
#             print('\r%d:%d:%d'%local_time[3:6],end=" ")
#             time.sleep(1)
#     return alert_ready
# alert_begin = alert()
# alert_begin()



#改为面向对象
# import time
# class Alert:
#     def __init__(self):
#         self.hour = int(input("你想把闹钟定到几点："))
#         self.minute = int(input("你想把闹钟定到几分："))
#     def alert_begin(self):
#         print("当前时间为：")
#         while True:
#             local_time = time.localtime()
#             if (self.hour,self.minute) == local_time[3:5]:
#                 print("时间到，你该起床啦！")
#                 break
#             print("\r%d:%d:%d"%local_time[3:6],end=' ')
#             time.sleep(1)

# alert = Alert()
# alert.alert_begin()




# 3.编程实现：一元运算符重载
# 要求：分类讨论，针对不同数据类型分别实现一元运算符的重载功能，即：整型数据如何进行重载，布尔型如何重载，列表如何重载

# 针对具体情况而言，比如对于整型，浮点型等数值型数据，取反即前面加上-号（布尔值除外，布尔值如果是True，取反后的值为False）

# 比如列表等数据类型，取反就是反转列表，负号就是对每一个元素取负值

# class My_Number:
# 	def __init__(self,value):
# 		self.data = value

# 	def __repr__(self):
# 		print("__repr__()方法被调用")
# 		return 'My_Number(%d)'%self.data

# 	#负号运算符重载
# 	def __neg__(self):
# 		print("__neg__()方法被调用")
# 		return -self.data

# 	#取反运算符重载
# 	def __invert__(self):
# 		print("__invert__()方法被调用")
# 		if type(self.data) is bool:
# 			if self.data == True:
# 				return False
# 			elif self.data == False:
# 				return True
# 		elif type(self.data) is int or type(self.data) is float:
# 			return -self.data

# num = My_Number(1)
# print(-num)

# 列表等数据类型的一元运算符重载

# class Mylist:
# 	def __init__(self,it):
# 		self.data = [x for x in it]

# 	def __repr__(self):
# 		print("__repr__()方法被调用")
# 		return 'Mylist(%r)'%self.data

# 	def __neg__(self):
# 		print("__neg__()方法被调用")
# 		return Mylist((-x for x in self.data))

# 	def __invert__(self):
# 		print("__invert__()方法被调用")
# 		return Mylist(reversed(self.data))

# l1 = Mylist([1,2,3,4,5,6])
# print(l1)
# l2 = -l1
# print(l2)



#  
# 4.双色球彩票游戏实现。需求如下：（降低随机度，我们只设定四个球的彩票，且每个数的随机范围在1-30之间）
#        1.假定现在已经有一组随机生成的彩票数
#        2.买家买一注彩票，如果有一个数字匹配，奖励50元；如果有两个匹配，奖励500元，如果有三个匹配，奖励5000元，如果全猜中，奖励50000元
# 要求：采用面向对象的编程思想，分析功能需求，分离功能，将每个功能封装在一个类中，通过类与类之间的继承实现功能的整合。
#  
#  
# 四道编程题，上机编码实现。以最终能够运行出代码结果为准，如果代码无法运行，根据代码逻辑酌情给分。
# import sys as s
# import random as r
# import math as m
# l = [m.floor(r.random()*30+1),m.floor(r.random()*30+1),m.floor(r.random()*30+1),m.floor(r.random()*30+1)]
# print(l)
# l_complete = []
# l_user = []
# while True:
# 	num = m.floor(r.random()*30+1)
# 	l_complete.append(num)
# 	if len(l_complete) == 4:
# 		break
# # print(l_complete)
# while True:
# 	try:
# 		num2 = int(input("请输入您要买一组彩票数："))
# 	except ValueError:
# 		print("请输入数字而不是字符！")
# 		s.exit()
# 	else:
# 		if num2 >30 or num2 < 1:
# 			print("范围错误啦!")
# 			s.exit()
# 	l_user.append(num2)
# 	if len(l_user) == 4:
# 		break
# # print(l_user)
# k = 0

# for j in l_user:
# 	if j in l_complete:
# 		k+=1
# # print(k)
# if k == 1:
# 	print("奖励50")
# elif k == 2:
# 	print("奖励500")
# elif k == 3:
# 	print("奖励5000")
# elif k == 4:
# 	print("奖励50000")
# else:
# 	print("真抱歉，没中一个！")


# 面向对象编程思想实现
# import sys as s
# import random as r
# import math as m


# #生成随机数类
# class Make_Random:
# 	def __init__(self):
# 		self.l_complete = []

# 	def make_random(self):
# 		while True:
# 			num_r = m.floor(r.random()*30+1)
# 			self.l_complete.append(num_r)
# 			if len(self.l_complete) == 4:
# 				break
# 		return self.l_complete

# #用户购买一注彩票类
# class Buy_CaiPiao:
#  	def __init__(self):
#  		self.l_user = []

#  	def buy_caipiao(self):
#  		while True:
#  			try:
#  				num_b = int(input("请输入您要买一组彩票数："))
#  			except ValueError:
#  				print("要输入的是数字而不是字符啊兄dei！！！")
#  				s.exit()
#  			else:
#  				if num_b >30 or num_b < 1:
#  					print("输入的值的范围不在1到30之间啊兄dei!!!!")
#  					s.exit()
#  			self.l_user.append(num_b)
#  			if len(self.l_user) == 4:
#  				break
#  		return self.l_user


# #核心功能：验证有几个数字中奖类
# class Check_Number(Make_Random,Buy_CaiPiao):
# 	def __init__(self):
# 		self.count = 0
# 		self.l_complete = []
# 		self.l_user = []

# 	def check_number(self):
# 		super(Check_Number,self).make_random()
# 		super(Check_Number,self).buy_caipiao()
# 		for i in self.l_user:
# 			if i in self.l_complete:
# 				self.count+=1
# 		return self.count

# #验证之后的结果，最终子类

# class Result(Check_Number):
# 	def __init__(self):
# 		self.count = 0
# 		self.l_complete = []
# 		self.l_user = []
# 	def result_user(self):
# 		super(Result,self).check_number()
# 		if self.count == 1:
# 			print("猜中一个数字！奖励50!")
# 		elif self.count == 2:
# 			print("猜中两个数字！奖励500!")
# 		elif self.count == 3:
# 			print("猜中三个数字！奖励5000!")
# 		elif self.count == 4:
# 			print("猜中四个数字！奖励50000!")
# 		else:
# 			print("真可惜，您一个都没猜中！再买一注吧？")

# result = Result()
# print(Result.__mro__)
# result.result_user()