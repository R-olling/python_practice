# #字符串的基本操作——————>不可变性、有序性、可迭代性
s = "Hello-Python"
print(s[4])
print(s[-8])
# #s[4] = "X"——————"字符串是不可变的"
# #TypeError: 'str' object does not support item assignment——————"字符串是不可变的"
for num in s:#遍历操作
    print(num)
# 切片
print(s[0:5:1])
print(s[:5:])
print(s[:5])
print(s[-1:-7:-1])
print(len(s))#中间的-没算在字符串里
"""
关键知识点：
Python 切片语法：
字符串[起始索引 : 结束索引 : 步长]
步长不写，默认是 1（正向切片）
你写的是：s[-1:-6:]
起始：-1 → 字符串最后一个字符（n）
结束：-6 → 在最后一个字符的左边
步长：1 → 从左往右切
结果：
起点在右边，终点在左边，还要求从左往右切 → 根本切不到任何字符！
所以打印出来是空字符串。
"""
