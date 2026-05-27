"""
开发一个教务管理系统，在该系统中可以维护和管理学员的成绩信息，具体需求如下：
添加学生信息：根据提示录入学生姓名、语文、数学、英语成绩，录入完成保存到系统中。
修改学生信息：要求输入要修改的学生姓名，然后再提示输入语文、数学、英语成绩，输入完成后修改学员信息。
删除学生信息：要求输入要删除的学生姓名，根据姓名删除学生信息。
查询学生信息：要求输入要查询的学生姓名，根据姓名查询学生信息并输出。
列出所有学生：遍历所有学生信息并输出。
统计班级成绩：统计班级语文、数学、英语成绩的最高分、最低分、平均分，以及语文、数学、英语最高分和最低分的学员姓名。
退出系统。
"""
"""
agent = {}
while True:
    print("————————教务管理系统————————")
    print("1.添加学生信息")
    print("2.修改学生信息")
    print("3.删除学生信息")
    print("4.查询学生信息")
    print("5.列出所有学生")
    print("6.统计班级成绩")
    choice = input("请选择操作（输入1-5）：")
    if choice == "1":
        name = input("请输入学生姓名：")
        if name in agent:
            print("系统中已有该生信息，如需修改请使用功能2")
            continue
        try:
            chinese = float(input("请输入语文成绩"))
            math = float(input("请输入数学成绩"))
            english = float(input("请输入英语成绩"))
        except ValueError:
            print("请检查并输入正确的成绩！！")
            continue
        agent[name] = {"chinese":chinese, "math":math, "english":english}
        print(f"{name}的成绩添加成功！")
    if choice == "2":
        name = input("请输入要修改成绩的学生姓名：")
        if name not in agent:
            print("系统中还未有该生信息，如需添加请使用功能1")
            continue
        try:
            chinese = float(input("请输入修改后的语文成绩"))
            math = float(input("请输入修改后的数学成绩"))
            english = float(input("请输入修改后的英语成绩"))
        except ValueError:
            print("请检查并输入正确的成绩！！")
            continue
        agent[name] = {"chinese": chinese, "math": math, "english": english}
        print(f"{name}的成绩修改成功！")
    if choice == "3":
        name = input("请输入要删除的学生姓名：")
        if name not in agent:
            print("系统中还未有该生信息，如需添加请使用功能1")
            continue
        a = agent.pop(name)
        print(f"{a}的成绩已成功删除！")
    if choice == "4":
        name = input("请输入要要查询成绩信息的学生姓名：")
        if name not in agent:
            print("系统中还未有该生信息，无法查询，如需添加请使用功能1")
            continue
        scores = agent[name]
        print(f"{name}的语文成绩是{scores['chinese']}，数学成绩是{scores['math']}，英语成绩是{scores['english']}")
    if choice == "5":
        for name, scores in agent.items():
            print(f"学生姓名：{name}，语文：{scores['chinese']}，数学：{scores['math']}，英语：{scores['english']}")
        # 6. 统计班级成绩（完整实现最高分、最低分、平均分）
"""

students = {}  # 存储学生信息：key=姓名，value=三科成绩字典

while True:
    print("————————————教务管理系统————————————")
    print("1. 添加学生信息")
    print("2. 修改学生信息")
    print("3. 删除学生信息")
    print("4. 查询学生信息")
    print("5. 列出所有学生")
    print("6. 统计班级成绩")
    print("0. 退出系统")
    print("————————————————————————————————————")

    choice = input("请选择操作（输入0-6）：")

    # 1. 添加学生信息
    if choice == "1":
        name = input("请输入学生姓名：")
        if name in students:
            print("⚠️ 系统中已有该生信息，如需修改请使用功能2")
            continue
        try:
            chinese = float(input("请输入语文成绩："))
            math = float(input("请输入数学成绩："))
            english = float(input("请输入英语成绩："))
        except ValueError:
            print("⚠️ 输入错误！成绩必须是数字！")
            continue

        students[name] = {"chinese": chinese, "math": math, "english": english}
        print(f"✅ {name} 成绩添加成功！")

    # 2. 修改学生信息
    elif choice == "2":
        name = input("请输入要修改成绩的学生姓名：")
        if name not in students:
            print("⚠️ 系统中无该生信息，如需添加请使用功能1")
            continue
        try:
            chinese = float(input("请输入修改后的语文成绩："))
            math = float(input("请输入修改后的数学成绩："))
            english = float(input("请输入修改后的英语成绩："))
        except ValueError:
            print("⚠️ 输入错误！成绩必须是数字！")
            continue

        students[name] = {"chinese": chinese, "math": math, "english": english}
        print(f"✅ {name} 成绩修改成功！")

    # 3. 删除学生信息
    elif choice == "3":
        name = input("请输入要删除的学生姓名：")
        if name not in students:
            print("⚠️ 系统中无该生信息")
            continue
        students.pop(name)
        print(f"✅ {name} 已成功删除！")

    # 4. 查询学生信息
    elif choice == "4":
        name = input("请输入要查询的学生姓名：")
        if name not in students:
            print("⚠️ 系统中无该生信息")
            continue
        scores = students[name]
        print(f"\n📄 {name} 成绩信息：")
        print(f"语文：{scores['chinese']}")
        print(f"数学：{scores['math']}")
        print(f"英语：{scores['english']}\n")

    # 5. 列出所有学生
    elif choice == "5":
        if not students:
            print("⚠️ 暂无学生信息")
            continue
        print("\n📋 所有学生成绩列表：")
        for name, scores in students.items():
            print(f"姓名：{name} | 语文：{scores['chinese']} | 数学：{scores['math']} | 英语：{scores['english']}")
        print()

    # 6. 统计班级成绩（完整实现最高分、最低分、平均分）
    elif choice == "6":
        if not students:
            print("⚠️ 暂无学生信息，无法统计")
            continue

        # 取出所有成绩
        all_chinese = [s["chinese"] for s in students.values()]
        all_math = [s["math"] for s in students.values()]
        all_english = [s["english"] for s in students.values()]
        count = len(students)

        # 语文统计
        max_c = max(all_chinese)
        min_c = min(all_chinese)
        avg_c = sum(all_chinese) / count
        name_c_max = [n for n, s in students.items() if s["chinese"] == max_c]
        name_c_min = [n for n, s in students.items() if s["chinese"] == min_c]

        # 数学统计
        max_m = max(all_math)
        min_m = min(all_math)
        avg_m = sum(all_math) / count
        name_m_max = [n for n, s in students.items() if s["math"] == max_m]
        name_m_min = [n for n, s in students.items() if s["math"] == min_m]

        # 英语统计
        max_e = max(all_english)
        min_e = min(all_english)
        avg_e = sum(all_english) / count
        name_e_max = [n for n, s in students.items() if s["english"] == max_e]
        name_e_min = [n for n, s in students.items() if s["english"] == min_e]

        # 输出统计结果
        print("\n📊 班级成绩统计：")
        print(f"总人数：{count}")
        print("=" * 50)
        print(
            f"语文 | 最高分：{max_c}（{','.join(name_c_max)}）| 最低分：{min_c}（{','.join(name_c_min)}）| 平均分：{avg_c:.1f}")
        print(
            f"数学 | 最高分：{max_m}（{','.join(name_m_max)}）| 最低分：{min_m}（{','.join(name_m_min)}）| 平均分：{avg_m:.1f}")
        print(
            f"英语 | 最高分：{max_e}（{','.join(name_e_max)}）| 最低分：{min_e}（{','.join(name_e_min)}）| 平均分：{avg_e:.1f}")
        print("=" * 50 + "\n")

    # 0. 退出系统
    elif choice == "0":
        print("👋 已退出教务管理系统")
        break

    # 无效输入
    else:
        print("⚠️ 输入错误，请输入 0-6 之间的数字！")

