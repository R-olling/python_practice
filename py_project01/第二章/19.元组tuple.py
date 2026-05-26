# # 元组的基本操作
# # 定义（）
# t1 = (80,95,78,50,76,80,85,20)
# print(t1)
# print(type(t1))
# # 索引访问，不支持修改
# print(t1[0])
# print(t1[-1])
# # 切片
# print(t1[0:5])
# # count()统计元素的个数
# # index()统计元素的索引（输出第一个位置）
# print(t1.count(80))
# print(t1.index(80))
# # 注意：如果定义单元素的元组，单个元素之后需要加逗号
# t2 = ()
# print(t2)
# print(type(t2))
#
# t3 = (100)
# print(t3)
# print(type(t3))#<class 'int'>
#
# t3 = (100,)
# print(t3)
# print(type(t3))#<class 'tuple'>


# ——————————————————————————————————元组tuple的组包与解包————————————————————————————————————————
# 组包操作
t1 = (5,7,9,10,2,23,12)
t2 = 5,7,9,10,2,23,12#第二种方式也可以，不推荐

print(t1)
print(t2)

# 解包操作
# 基础解包（变量数量与容器的元素个数一致）
a,b,c,d,e,f,g = t1
print(a,b,c,d,e,f,g)
# 扩展解包，*a可以收集剩余的元素
first,second,*other,last = t1
print(first,second,other,last)
print(first)
print(second)
print(other)
print(type(other))
print(last)

*other,last1,last2 = t1
print(other)
print(last1)
print(last2)


# 案例 1：交换两个变量 a=10 和 b=20
# 利用元组解包，Python 可以一行代码完成交换，不需要额外定义临时变量。
# 初始值
a = 10
b = 20
print("交换前：a =", a, ", b =", b)

# 利用元组交换变量
a, b = b, a

print("交换后：a =", a, ", b =", b)

# 案例 2：循环交换三个变量 a=100, b=200, c=300
# 题目要求：a 原来的值给 c，b 原来的值给 a，c 原来的值给 b，也就是实现一个 “循环移位”。
# 初始值
a = 100
b = 200
c = 300
print("交换前：a =", a, ", b =", b, ", c =", c)

# 利用元组实现 a→c, b→a, c→b 的循环交换
a, b, c = b, c, a

print("交换后：a =", a, ", b =", b, ", c =", c)



