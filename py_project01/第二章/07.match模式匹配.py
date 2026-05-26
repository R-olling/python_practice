# #match...case模式匹配：工作日安排
# day = int(input("请输入星期几（1-7）："))
#
# match day:
#     case 1:
#         print("周一：工作会议日")
#     case 2:
#         print("周二：学习培训日")
#     case 3:
#         print("周三：项目开发日")
#     case 4:
#         print("周四：代码审查日")
#     case 5:
#         print("周五：总结规划日")
#     case 6 | 7:
#         print("周六周日：休息日")
#     case _:
#         print("输入不合规范")


# 计算器：+-*/运算，需要用户输入运算的两个数以及运算符，就可以进行计算
# a = float(input("请输入被加数（被减数or被乘数or被除数）a："))
# b = float(input("请输入加数（减数or乘数or除数）b："))
# symbol = input("请输入运算符（+-*/）：")

# if symbol == "/" and b == 0:
#     print("错误，被除数不能为0")
# else:
#     match symbol:
#         case "+":
#             print("a + b =", a + b)
#         case "-":
#             print("a - b =", a - b)
#         case "*":
#             print("a * b =", a * b)
#         case "/":
#             print("a / b =", a / b)
#         case _:
#             print("超出运算范围，请输入+-*/")

# 老师的解法
# match symbol:
#         case "+":
#             print("a + b =", a + b)
#         case "-":
#             print("a - b =", a - b)
#         case "*":
#             print("a * b =", a * b)
#         case "/" if b != 0:
#             print("a / b =", a / b)
#         case _:
#             print("超出运算范围，请输入+-*/")

# 作业：请你编写一个游戏角色移动控制器：根据玩家输入的不同指令，控制角色执行相应的动作（输出到控制台）
# 玩家输入上/w/W 角色象上移动以此类推
operate = input("读取玩家操作输入中：")
match operate:
    case "上" | "w" | "W":
        print("向上移动")
    case "下" | "s" | "S":
        print("向下移动")
    case "左" | "a" | "A":
        print("向左移动")
    case "右" | "d" | "D":
        print("向右移动")
    case "跳" | " ":
        print("跳跃")
    case "攻击" | "j" | "J":
        print("攻击")
    case "退出" | "esc" | "ESC":
        print("退出")
    case _:
        print(None)