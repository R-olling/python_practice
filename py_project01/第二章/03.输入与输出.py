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

# 练习：根据用户输入的两个数字，计算两个数字之和，并将其输出到控制台
num1 = input("请输入第一个数字：")
num2 = input("请输入第二个数字：")
sum = int(num1) + int(num2)
print(f"两个数字之和为{sum}")