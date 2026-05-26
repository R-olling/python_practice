# # 列表操作
# # 定义
# s = [56, 90, 88, 65, 90, "A", "Hello", True]
# #     0   1   2   3   4   5      6       7
# #    -8  -7  -6  -5  -4  -3     -2      -1
# print(type(s))
#
# # 访问列表的元素
# # 获取
# print(s[0],s[1],s[2],s[3],s[4],s[5],s[6],s[7])#正向索引从0开始
# print(s[-1],s[-2],s[-3],s[-4],s[-5],s[-6],s[-7],s[-8])#反向索引从-1开始
#
# print(s[2])
# print(s[-6])
#
# # 修改
# s[5] = "ABC"
# print(s)
#
# # s[10] = "DEF"超出范围就会报错
# # print(s)
#
# # 删除指定位置的元素del
# del s[6]#删除第7个元素
# print(s)
#
# # 遍历
# for item in s:
#     print(item)

#-------------------------列表 list 切片---------------------------------
# 定义列表
# s = ["A" , "C" , "H" , "K" , "L" , "B" , "D" , "X" , "C" , "U"]
#
# # 切片操作s[开始索引：结束索引：步长]
# print(s[0:5:1])
# print(type(s[0:5:1]))
# ——————————————————————————列表 list 常用方法————————————————————————————
# 列表定义
s = [56, 90, 88, 65, 90, 100, 209, 72, 145]
print(s)

# append()在列表尾部追加元素
s.append(188)
print(s)
# insert()在指定索引之前，插入元素
s.insert(2,80)
print(s)
# remove()移除列表中第一个匹配到的元素
s.remove(90)
print(s)
# pop()删除列表中指定索引位置的元素并返回（如果未指定，默认最后一个）
e = s.pop(1)
print(e)
print(s)

e = s.pop()
print(e)
print(s)
# sort()对列表进行排序
s.sort()
print(s)
# reverse()反转列表
s.reverse()
print(s)

















