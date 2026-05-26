"""
字典/key必须是不可变类型(str,int,float,tuple)
定义
dict1 = {"王林":670,"李沐婉":608,"徐立国":680,"韩立":688}
print(dict1)
print(type(dict1))

dict2 = {0:670,1.5:608,(1,2):680,3:688}#key必须是不可变类型(str,int,float,tuple)/不能是list、set、dict
print(dict2)
print(type(dict2))

# 访问
print(dict1.keys())
print(dict1.values())
print(dict2.keys())
print(dict2.values())
print(dict2.items())
print(dict1["韩立"])#访问

dict1["李沐婉"] = 6999#修改value值
print(dict1["李沐婉"])
"""
#________________字典 常见操作_____________________
dict1 = {"王林":670,"李沐婉":608,"徐立国":580,"韩立":688}
print(dict1)

# 添加
dict1["涛哥"] = 50
print(dict1)

# 修改
dict1["涛哥"] = 700
print(dict1)
# 查询
print(dict1["涛哥"])
print(dict1.get("涛哥"))
print(dict1.keys())
print(dict1.values())
print(dict1.items())

# 删除
score = dict1.pop("徐立国")
print(score)
print(dict1)
del dict1["韩立"]
print(dict1)

# 遍历
for k in dict1.keys():
    print(f"{k}: {dict1[k]}")

for item in dict1.items():
    print(f"{item[0]}: {item[1]}")

for k, v in dict1.items():
    print(f"{k}: {v}")