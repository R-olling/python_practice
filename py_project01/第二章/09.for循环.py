#遍历字符串“hello python”中的每一个字母
# msg = input("请输入需要遍历的字符串：")
#
# for i in msg:#i表示遍历出来的元素，msg表示需要遍历的数据
#     print(i)
# else:
#     print("循环结束")


"""
案例
1计算1-100之间所有的奇数之和
2计算100-500之间所有3的倍数的数字之和
"""
total = 0
i = 1
while i < 100:
    if i % 2 != 0:
        total += i
    i += 1
print(total)

# 计算100-500之间所有3的倍数的数字之和
total = 0
for i in range(100, 501):#不包含501，详见第三章笔记range部分
    if i % 3 == 0:
        total += i
print(total)
