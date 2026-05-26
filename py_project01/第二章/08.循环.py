# # 打印十遍人生苦短，我用python
# a = 0
# while a  < 10:
#     print("人生苦短，我用python")
#     a += 1
# else:
#     print("循环结束")

# # 计算1-100之间的所有偶数累加之和
# even = 0
# s = 0
# while even < 100 :
#     even =  even + 2
#     s +=  even
# print("1-100之间所有偶数的和为：",s)

# # # 计算1-100之间的所有偶数累加之和
# total = 0
# i = 1
# s = 0
# while total <= 100:
#     if i % 2 == 0:#i是偶数
#         s += i#s是累加的值
#         i += 1#此时i增大1个值
#         total += 1#计数也变大
#     else:#i不是偶数，i和计数同样应该增大1个值
#         total += 1
#         i += 1
# else:
#     print(s)

# 计算1-100之间的所有偶数累加之和，上面两种是我自己想出来的，下面是老师的标准答案
total = 0
i = 1
while i <= 100:
    if i % 2 == 0:
        total += i
    i += 1
print(total)