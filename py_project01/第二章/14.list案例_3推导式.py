"""
完成如下需求
1.生成1-20的平方列表
2.从如下数字列表中提取所有的偶数，并计算其平方，组成新的列表
    num_list = [19,23,54,64,87,20,109,232,123,43,26,55,72]
"""
"""
1.
square = []
for i in range(1,21):
    square.append(i**2)
    i += 2
print(square)
"""
# 一行搞定：[要插入的值 for i in 序列]
num_list2 = [i**2 for i in range(1, 21)]
print(num_list2)
# ————————————————————————————————————
num_list = [19,23,54,64,87,20,109,232,123,43,26,55,72]
square = []
for num in num_list:
    if num % 2 == 0:
        square.append(num**2)
print(square)
# ——————————————————————————————
# 案例4：提取所有偶数并计算平方，组成新列表
num_list = [12, 32, 45, 77, 80, 92, 33, 57, 97, 98, 110, 111, 122]
new_list = [i**2 for i in num_list if i % 2 == 0]
print(new_list)