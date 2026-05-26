# # 常见数据类型--->type()获取指定的字面量或变量的类型
# print("Hello")
# print(type("Hello"))#字符串str
#
# print(type(10))#整数int
# print(type(3.14))#浮点数float
# print(type(True))#布尔bool
# print(type(False))#布尔bool
# print(type(None))#空值NoneType
#
# num = -100
# print(type(num))#输出的是变量对应的值的类型
#
# # 常见数据类型--->isinstance(数据,类型)判定数据是否是指定的类型，返回的结果是bool,如果是，输出True，否则输出False
# print(isinstance(num,int))#True
# print(isinstance(num,float))#False
# print(isinstance(num,bool))#False

# # 字符串，定义字符串的三种方式
# s1 = "Hello"
# s2 = 'Hello'
# s3 = """
# Hello:
#     欢迎大家进入到Python课程的学习
#     希望大家一键三连
# """#三引号可以定义多行字符串
# print(s1, s2, s3)
# print(type(s1), type(s2), type(s3))


# #转译字符\',\",\n,\t
# msg = 'It\'s very good!'
# print(msg)
# msg1 = "It's very good!"
# print(msg1)
# msg2 = "Hello 的意思是\"您好\""
# print(msg2)
# msg3 = 'Hello 的意思是"你好"'
# print(msg3)
# print("\t欢迎大家进入Python课程的学习！\n记得一键三连哦！")#\n表示换行\t代表缩进

# #字符串的拼接
# s1 = "人生苦短" "我用Python"
# print(s1)
#
# s2 = "人生苦短"+"我用Python"
# print(s2)
#
# s3 = "人生苦短"
# s4 = "我用Python"
#
# print("吉多·范罗苏姆："+s3+","+s4)

# 案例：根据自己的实际情况，输出个人的详细信息，具体结构如下：
# “大家好，我是涛哥，今年18岁，学习的专业是软件工程，爱好Python、Java”
# msg1 = "大家好，"+"我是涛哥"
# msg2 = "今年18岁"
# msg3 = "学习的专业是软件工程"
# msg4 = "爱好Python"
# msg5 = "Java"
# print(msg1+"，"+msg2+"，"+msg3+"，"+msg4+"、"+msg5)

# #案例----->str(int数字)---->转为字符串
# name = "毕哥"
# age = 23
# major = "自动化"
# hobby = "健身"
# print("大家好，我是"+name+"，""今年"+str(age)+"，""学习的专业是"+major+"，""爱好是"+hobby)#将容易改变的量存为变量，方便后续更新数据

# 字符串格式化

# name = "毕哥"
# age = 23
# major = "自动化"
# hobby = "健身"
# print("大家好，我是%s，今年%s岁，学习的专业是%s，爱好是%s"%(name,age,major,hobby))#s会自动的转换内容为str


# name = "毕哥"
# age = 23
# major = "自动化"
# hobby = "健身"
# print(f"大家好，我是{name}，今年{age}岁，学习的专业是{major}，爱好是{hobby}")#"前面要加f,后面用{}括起来变量

#获取键盘上输入的数据----->input
# name = input("请输入您的姓名：")
# print(f"欢迎您,{name}")
# age = input("请输入您的年龄：")
# print(f"您今年{age}岁")

#案例，小智的银行卡中有10000元，现在到ATM进行取钱操作，请根据输入的金额执行取钱操作，取钱完毕后，展示其银行卡余额
#步骤：1.输入密码2.输入取款金额3.计算余额并取出
# total_amount = 10000
# code = input("请输入密码：")
# print("密码正确")
# amount = input("请输入取款金额：")
# surplus = total_amount - int(amount)#str转化为int类型，因为键盘的输入都是str类型不能直接和int加减
# print(f"取款成功，您的余额是{surplus}")

# # 练习：根据用户输入的两个数字，计算两个数字之和，并将其输出到控制台
# num1 = input("请输入第一个数字：")
# num2 = input("请输入第二个数字：")
# sum = int(num1) + int(num2)
# print(f"两个数字之和为{sum}")