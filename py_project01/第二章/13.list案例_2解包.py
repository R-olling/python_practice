# 合并两个列表中的元素，并对合并后的结果进行去重处理（去除列表中的重复元素）
# 列表定义
num_list1 = [19,23,54,64,875,20,109,232,123,54]
num_list2 = [55,80,72,35,60,123,54,29,91]
num_list1.sort()
num_list2.sort()
print(num_list1)
print(num_list2)
"""
不要在 for 循环里删除列表元素，非常容易越界
要去重优先用 set()，简单高效不报错
你的思路是对的（双重循环找重复），只是循环和删除的写法不对

for i in range(0,len(num_list1)+1):
    for j in range(0,len(num_list2)+1):
        if num_list1[i] != num_list2[j]:
            j += 1
        else:
            num_list2.pop(j)#___________在for循环里删除元素会导致第二遍循环的长度不够____________
            j += 1
    i += 1
print(num_list1)
print(num_list2)
"""
i = 0
while i < len(num_list1):
    j = 0
    while j < len(num_list2):
        if num_list1[i] != num_list2[j]:
            j += 1
        else:
            num_list2.pop(j)
            # j += 1,这个地方不能＋1，不然会漏掉后面一个自动填补到空缺的元素
    i += 1
print(num_list1)
print(num_list2)
num = num_list1 + num_list2
num.sort()
print(num)

#———————————————————————————利用set实现上述案例—————————————————————————————
num_list1 = [19,23,54,64,875,20,109,232,123,54]
num_list2 = [55,80,72,35,60,123,54,29,91]

# 合并 + 去重 + 转回列表
result = list(set(num_list1 + num_list2))
result.sort()  # 可选排序

print("合并去重结果：", result)

#————————————————————————————解包（老师解法——————————————————————————————————
# 案例2(简化)：合并两个列表中的元素，并对合并的结果进行去重处理
num_list1 = [19, 23, 54, 64, 875, 20, 109, 232, 123, 54]
num_list2 = [55, 80, 72, 35, 60, 123, 54, 29, 91]

# 1. 合并列表（老师说的“解包操作”在这里！）
# 用 * 把两个列表“解开”，直接把所有元素放进新列表
num_list = [num_list1, num_list2]#这步是将所有的元素解包到新的列表里，好处是除了上述两个列表，还能加新的元素

print("合并后的原始列表：", num_list)

# 2. 去重重复记录
new_list = []  # 去重重复记录后的列表

for num in num_list:
    # 判断new_list中是否存在num元素，如果不存在，再添加
    if num not in new_list:
        new_list.append(num)

print("去重重复记录后的列表：", new_list)