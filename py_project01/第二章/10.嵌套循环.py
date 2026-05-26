#打印一个长度为m，宽度为n的长方形，m，n由用户输入
# # 1. 获取用户输入的长度 m 和宽度 n
# # input() 获取的是字符串，需要转成整数 int()
# m = int(input("请输入长方形的长度 m："))
# n = int(input("请输入长方形的宽度 n："))
#
# # 2. 双层 for 循环打印长方形
# # 外层循环：控制行数（宽度 n）
# for i in range(n):
#     # 内层循环：控制每行的星号数量（长度 m）
#     for j in range(m):
#         # 打印星号，不换行（end="" 表示不自动换行）
#         print("*", end="")
#     # 一行打印完，换行
# #     print()
# n = 9
# m = 9
# p = 1
# for i in range(n):
#     for j in range(m + 1):
#         if j > 0 and j <= p:
#             print(f" {j} * {p}=", p * j , end="\t")#\t是制表符，让格式更整齐
#     p += 1
#     print()

# !/usr/bin/python3
user_name1 = "admin"
user_name2 = "zhangsan"
user_name3 = "taoge"
user_code1 = "666888"
user_code2 = "123456"
user_code3 = "888666"

while True:
    name = input("请输入账号:")
    code = input("请输入密码:")

    if name == "" or code == "":
        print("输入的用户名和密码不能为空！\n请重新输入")
        continue#结束当前循环，并且重新开启新一次循环

    if (name == user_name1 and code == user_code1) or \
            (name == user_name2 and code == user_code2) or \
            (name == user_name3 and code == user_code3):
        print("登录成功，进入b站首页～")
        break#只能出现在循环中，表示符合条件后跳出循环
    else:
        print("用户名或密码错误\n请重新输入")






