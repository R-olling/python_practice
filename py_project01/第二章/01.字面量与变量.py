# # 字面量的写法
# print(100)#整数(int)
# print(3.14)#浮点数/小数(float)
# print(True)#布尔(bool)
# print(False)#布尔(bool)
# print("Hello Python")#字符串(str)
# print("------------------")#字符串(str)
# print(None)#空值(None Type)
#
# # 布尔类型本质也是整数类型(True-1;false-0)
# print(True + 1)#2
# print(False - 1)#-1

# # 变量------>Python是动态类型语言，一个变量可以存储不同的数据类型（但是在项目开发中，推荐一个变量只存储一种类型的数据）
# num = 1114.1
# print(num)
#
# num = num + 1
# print(num)
#
# num = "OK"
# print(num)
#
# num = True
# print(num)
# num = False
# print(num)
#
# a = True
# print(a)
# a = False
# print(a)

# # 案例，课程基础播放量为20.7万，每月新增播放量为50万，请输出未来两个月每个月的播放总量？
# #我的解法
# a = 20.7
# print(a)
# a = a + 50
# print(a)
# a = a + 50
# print(a)
# # 老师的标准解法
# base = 20.7#基础播放量
# incr = 50#每月新增播放量
# print("未来第一个月的播放量为：", base + incr)#ctrl+d可以快速复制当前行并粘贴到下一行
# print("未来第二个月的播放量为：", base + incr + incr)
# 老师的标准解法 案例-升级，一次性定义多个变量
# base,incr = 20.7,50
# print("未来第一个月的播放量为：", base + incr)#ctrl+d可以快速复制当前行并粘贴到下一行
# print("未来第二个月的播放量为：", base + incr + incr)

# # 标识符
# true = 1
# print(true)

# 案例，现有两个变量，a=10，b=20，现需将这两个变量值交换，再输出道控制台
a = 10
b = 20
change = a#将a的值记录了下来，临时变量，只用来记录a的值
a = b#把b的值赋予a
b = change#把刚才存起来的a的值赋给b
print("交换后的a，b分别为",a,b)

#小练习，现有三个变量，分别为a=100，b=200，c=300，现需要将这三个变量值进行交换，将a，b，c的值分别赋给c，a，b，并将其输出到控制台
a = 100
b = 200
c = 300
change = a
a = b
b = c
c = change
print("交换后的a,b,c分别为",a,b,c)

#练习题标准答案
a = 100
b = 200
c = 300

temp = a
a = b
b = c
c = temp

print(a)
print(b)
print(c)
