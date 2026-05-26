# 题目1：合并、去重、排序
list1 = ['M', 'A', 'C', 'E', 'F', 'G', 'H', 'L', 'N', 'I', 'J', 'K', 'O']
list2 = ['X', 'Z', 'T', 'Y', 'D', 'E', 'F', 'G']
list3 = ['W', 'A', 'S', 'D']

# 方式1：传统写法（解包合并 + 循环去重）
combined = [*list1, *list2, *list3]  # 解包合并三个列表
new_list = []
for char in combined:
    if char not in new_list:
        new_list.append(char)
new_list.sort()  # 升序排序
print("题目1（传统写法）：", new_list)

# 方式2：列表推导式 + 集合去重（更简洁）
combined_set = set(list1 + list2 + list3)  # 合并后用set自动去重
new_list2 = sorted(combined_set)  # 直接升序排序
print("题目1（简化写法）：", new_list2)
# ______________________________________________________________________________________________________
# 题目2：筛选能被3或5整除的数，计算平方
list1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30]

# 方式1：传统循环写法
square_list = []
for num in list1:
    if num % 3 == 0 or num % 5 == 0:
        square_list.append(num ** 2)
print("题目2（传统写法）：", square_list)

# 方式2：列表推导式写法
square_list2 = [num**2 for num in list1 if num % 3 == 0 or num % 5 == 0]
print("题目2（列表推导式）：", square_list2)
# _____________________________________________________________________________________________________
# 题目3：提取列表中的正数
list1 = [11, 2, 31, 4, -5, 15, 17, 28, 49, 10, -11, 16, 54, -14, 36, -16, 87, -39]

# 方式1：传统循环写法
positive_list = []
for num in list1:
    if num > 0:
        positive_list.append(num)
print("题目3（传统写法）：", positive_list)

# 方式2：列表推导式写法
positive_list2 = [num for num in list1 if num > 0]
print("题目3（列表推导式）：", positive_list2)