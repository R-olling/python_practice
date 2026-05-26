# #if条件判断：如果分数超过680，我就去读清华
# score = 685
# if score >= 680:
#     print("你可以读清华了")
# print("_______________")


# # 案例：结合前面的输入输出以及if条件判断的知识，完成b站登录功能的实现（正确账号和密码为18888888888和666888）
# user_account = input("请输入账号(11位)：")
# if int(user_account) == 18888888888:
#     code = input("请输入密码：")
#     if int(code) == 666888:
#             print("恭喜您，成功登录")

# # 正确账号、密码（数字格式，适配你的int习惯）
# right_account = 18888888888
# right_pwd = 666888
#
# # 获取输入
# user_account = input("请输入账号(11位)：")
# # 转成int（你习惯的用法）
# account = int(user_account)
#
# # 第一步：判断是不是 11位数字（核心！不用len，用范围判断）
# if 10000000000 <= account <= 99999999999:
#     # 第二步：11位格式正确，再判断账号对不对
#     if account == right_account:
#         # 账号正确，输密码
#         code = int(input("请输入密码："))
#         if code == right_pwd:
#             print("恭喜您，成功登录")
#         else:
#             print("密码错误，登录失败")
#     else:
#         # 11位，但账号不是系统账号（你说的这个场景！）
#         print("账号不存在，登录失败")
# else:
#     # 不是11位（10位、12位都不行）
#     print("账号位数不正确，登录失败")



# # # 案例：结合前面的输入输出以及if条件判断的知识，完成b站登录功能的实现（正确账号和密码为18888888888和666888）
# ok_account = "123456789123"
# ok_code = "666888"
#
# user_account = input("请输入11位账号：")
# user_code = input("请输入密码：")
#
# if ok_account == user_account and ok_code == user_code:
#     print("恭喜您，成功登录bilibili")
# if ok_account != user_account or ok_code != user_code:
#     print("账号或密码不匹配，请重新输入")

# # # # 案例：结合前面的输入输出以及if条件判断的知识，完成b站登录功能的实现（正确账号和密码为18888888888和666888）
# #使用if else 语句
# right_account = "18888888888"
# right_password = "666888"
# user_account = input("请输入账号：")
# user_password = input("请输入密码：")
# if user_account == right_account and user_password == right_password :
#     print("恭喜你，成功登录")
# else:
#     print("账号或密码错误，请重新输入")


#案例2：根据用户输入的年份，判断这一年是闰年还是平年
#非整百年份且被4除的年份是闰年；整百年份能够被400整除的是闰年
#我的解法
# print("闰年平年判断器")
# num = input("请输入您要判断的年份（公元）：")
#
# if int(num) % 100 == 0:
#     num1 = int(num)
#     print(f"公元{num1}年属于整百年份")
#     if num1 % 400 == 0:
#         print(f"公元{num1}年是闰年")
#     else:
#         print(f"公元{num}年是平年")
# else:
#     if int(num) % 4 == 0:
#         print(f"公元{num}年是闰年")
#     else:
#         print(f"公元{num}年是平年")
# #老师的解法
# num = input("请输入您要判断的年份（公元）：")
# if (int(num) % 400 == 0) or (int(num) % 4 == 0 and int(num) % 100 != 0):
#     print("是闰年")
# else:
#     print("是平年")

#练习题目

#根据用户输入的数字判断该数字的奇偶
# num = input("请任意输入一个数字：")
# a = int(num)
# if a%2==0:
#     print("是偶数")
# else:
#     print("是奇数")

#根据用户输入的年龄判断是否成年
# age = int(input("请输入年龄："))
# if age >= 18:
#     print("已成年")
# else:
#     print("未成年")

#根据用户输入的数字判断正负
# num = int(input("请输入一个数字："))
# if num == 0:
#     print("是0")
# else:
#     if num > 0:
#         print("正数")
#     else:
#         print("负数")

#用if elif else
# num = int(input("请输入一个数字："))
# if num == 0:
#     print("是0")
# elif num < 0:
#     print("负数")
# else:
#     print("正数")






# 根据用户的考试分数判断是否及格
# score = int(input("请输入考试成绩："))
# if score >= 60:
#     print("恭喜你及格")
# else:
#     print(
#         "可惜了，你挂科了"
#     )

# #案例3：
# #根据输入的用户名密码进行登陆系统
# #用户名密码为：admin/666999 or root/547527 or zhangsan/123456
# # 否则就提示用户名或密码错误
# account1 = "admin"
# account2 = "root"
# account3 = "zhangsan"
# code1 = "666999"
# code2 = "547527"
# code3 = "123456"
# account = input("请输入用户名：")
# code = input("请输入密码：")
# if account == account1 and code == code1:
#     print("恭喜你登陆成功")
# elif account == account2 and code == code2:
#     print("恭喜你登陆成功")
# elif account == account3 and code == code3:
#     print("恭喜你登陆成功")
# else:
#     print("用户名或密码错误")

#作业1
# 根据输入的考试成绩判断成绩等级：大于等于85优秀；60-85及格；小于60不及格
# score = int(input("请输入成绩："))
# if score >= 85:
#     print("优秀")
# elif score >= 60 and score < 85:
#     print("及格")
# else:
#     print("不及格")

# 作业2：购物折扣计算，根据输入购物车的商品总额，以及如下规则，计算实际应付金额
# >=500 八折；300 <= 金额 < 500 九折；100 <= 金额 < 300 九五折；金额小于一百块没有折扣
sum = int(input("您的购物车总金额是（元）："))
if sum >= 500:
    print("您的折后价为：",sum * 0.8)
elif 300 <= sum < 500:
    print("您的折后价为：",sum * 0.9)
elif 100 <= sum < 300:
    print("您的折后价为：",sum * 0.95)
else:
    print(f"您未到折扣金额，应付款{sum}")

