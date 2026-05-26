# 案例1
# 将用户输入的10个数字，存储到一个列表中，并将列表中的数字进行排序，输出其中的最小值、最大值 和 平均值。
# 我的解法
"""
s = [0,0,0,0,0,0,0,0,0,0]
s[0] = int(input("请输入第1个数字："))
s[1] = int(input("请输入第2个数字："))
s[2] = int(input("请输入第3个数字："))
s[3] = int(input("请输入第4个数字："))
s[4] = int(input("请输入第5个数字："))
s[5] = int(input("请输入第6个数字："))
s[6] = int(input("请输入第7个数字："))
s[7] = int(input("请输入第8个数字："))
s[8] = int(input("请输入第9个数字："))
s[9] = int(input("请输入第10个数字："))
print(s)
s.sort()
print("最小值为:",s[0])
print("最大值为:",s[9])
print("平均值为：",(s[0]+s[1]+s[2]+s[3]+s[4]+s[5]+s[6]+s[7]+s[8]+s[9])/10)
"""
#老师的解法for循环

# 1：定义列表
num_list = []
# 2：将用户输入的10个数字存入列表
for i in range(10):
   num = int(input("请输入数字："))
   num_list.append(num)
   i += 1
# 3：排序
num_list.sort()
# 4：输出其中的最小值、最大值 和 平均值
print(num_list)
print("最大值:",num_list[9])
print("最小值:",num_list[0])
print("平均值：",(num_list[0]+num_list[1]+num_list[2]+num_list[3]+num_list[4]+num_list[5]+num_list[6]+num_list[7]+num_list[8]+num_list[9])/10)
print("平均值：",sum(num_list)/len(num_list))#sum列表所有元素的加和，len列表的长度