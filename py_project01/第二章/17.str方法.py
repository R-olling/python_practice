# 定义初始字符串
s = "Hello-Python-Hello-World"

# find() 查找指定字符串第一次出现的索引位置
index = s.find("-")
print(index)  # 输出: 5
# 说明：字符串索引从0开始，第一个 "-" 在第5位（H e l l o - ...）

# count() 统计子字符串在指定字符串中出现的次数
c = s.count("o")
print(c)  # 输出: 4
# 说明：Hello(2个) + Python(0个) + Hello(2个) + World(0个) = 4个"o"

# upper() 转为大写
su = s.upper()
print(su)  # 输出: HELLO-PYTHON-HELLO-WORLD

# lower() 转为小写
sl = s.lower()
print(sl)  # 输出: hello-python-hello-world

# split() 将字符串按照指定字符串切割 - 生成列表
slist = s.split("-")
print(slist)  # 输出: ['Hello', 'Python', 'Hello', 'World']

# strip() 去除字符串两端的空格
ss = s.strip()
print(ss)  # 输出: Hello-Python-Hello-World
# 说明：原字符串两端没有空格，所以和原字符串一样
# replace() 将字符串中的指定子串替换为新的内容
sr = s.replace("-", "_")
print(sr)

# startswith() / endswith() 判断字符串是否是以指定的字符串开头 / 结尾，返回布尔值
print(s.startswith("Hello"))
print(s.endswith("Python"))