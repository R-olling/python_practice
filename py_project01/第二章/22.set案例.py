# 根据提供的班级学生的选课情况，完成如下需求：
# 1. 找出同时选修了法语和艺术的学生
# 2. 找出同时选修了所有四门课程的学生
# 3. 找出选修了足球，但是没有选修篮球的学生
# 4. 统计每一个学生选修的课程数量
# 选修足球学生名单
football_set = {"王林", "曾牛", "徐立国", "道天", "天运子", "韩立", "厉飞雨", "乌丑", "紫灵"}
# 选修篮球学生名单
basketball_set = {"张铁", "墨居仁", "王林", "姜老道", "曾牛", "王蝉", "韩立", "天运子", "李化元", "厉飞雨", "云露"}
# 选修法语学生名单
french_set = {"许木", "王卓", "十三", "虎跑", "姜老道", "天运子", "红蝶", "厉飞雨", "韩立", "曾牛"}
# 选修艺术学生名单
art_set = {"道天", "天运子", "韩立", "虎跑", "姜老道", "紫灵"}
print("同时选修了法语和艺术的学生:",french_set.intersection(art_set))
all_course = football_set & basketball_set & french_set & art_set
print("找出同时选修了所有四门课程的学生",all_course)
print("选修了足球，但是没有选修篮球的学生",football_set.difference(basketball_set))
all_set = football_set | basketball_set | french_set | art_set
for x in all_set:
    count = 0
    if x in basketball_set:
        count += 1
    if x in football_set:
        count += 1
    if x in french_set:
        count += 1
    if x in art_set:
        count += 1
    print(f"{x}选了{count}次")
