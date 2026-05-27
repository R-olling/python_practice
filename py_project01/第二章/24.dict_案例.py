"""
开发一个购物车管理系统，实现商品信息的添加、修改、删除、查询功能。系统使用字典结构存储商品数据，通过控制台菜单与用户交互。具体功能如下：
添加购物车：用户根据提示录入商品名称、以及该商品的价格、数量，保存该商品信息到购物车。
修改购物车：要求用户输入要修改的购物车商品名称，然后再提示输入该商品的价格、数量，输入完成后修改该商品信息。
删除购物车：要求用户输入要删除的购物车名称，根据名称删除购物车中的商品。
查询购物车：将购物车中的商品信息展示出来，格式为："商品名称：xxx，商品价格：xxx，商品数量：xxx"。
退出购物车
"""
"""
我的错误解法
s = []
cart = {}
while True:
    name = input("请您输入商品名称")
    s.append(input("请您输入商品的价格:"))
    s.append(input("请您输入商品的数量:"))
    cart[name] = s
    a = input("时候要继续添加？（是或否）")
    if a == "否":
        break
b = input("是否要修改某个商品？（是或否）")
if b == "是":
    while True:
        name = input("输入要修改的商品名称")
        s.append(input("输入要修改的价格:"))
        s.append(input("输入要修改的数量:"))
        c = input("是否继续修改？（是或否）")
        if c == "否":
            break
d = input("是否要删除某个商品？（是或否）")
if d == "是":
    while True:
        name = input("输入要删除的商品名称")
        if name in cart:
            del cart[name]
        e = input("是否继续删除？（是或否）")
        if e == "否":
            break
print(cart)
"""
# 购物车字典：键为商品名称（字符串），值为另一部字典，包含 price 和 quantity
cart = {}

while True:
    print("\n===== 购物车管理系统 =====")
    print("1. 添加商品")
    print("2. 修改商品")
    print("3. 删除商品")
    print("4. 查询购物车")
    print("5. 退出系统")
    choice = input("请选择操作（输入数字1-5）：")

    # 1. 添加商品
    if choice == "1":
        name = input("请输入商品名称：")
        # 检查是否已存在
        if name in cart:
            print("该商品已在购物车中，如需修改请使用修改功能。")
            continue
        try:
            price = float(input("请输入商品价格："))
            quantity = int(input("请输入商品数量："))
        except ValueError:
            print("价格请输入数字，数量请输入整数！")
            continue
        cart[name] = {"price": price, "quantity": quantity}
        print(f"商品 {name} 添加成功！")
    # 🧠 先看一个没有异常处理的问题
    # 假设你写了这样一行代码：
    #
    # python
    # price = float(input("请输入商品价格："))
    # 如果用户输入的是 19.9，没问题，程序正常运行。
    # 但如果用户不小心输入了 十九点九 或者 abc，会发生什么？
    #
    # 程序会报错，崩溃，退出。错误信息类似：
    #
    # text
    # ValueError: could not convert string to float: '十九点九'
    # float() 函数只能把像 "19.9" 这样的数字字符串转成浮点数，遇到非数字字符串就会“抛出”一个 ValueError 类型的异常。
    #
    # ✅ try...except 的作用
    # try...except 就是用来捕获并处理这类异常的，让程序不会崩溃，而是给用户一个友好的提示，然后可以继续运行。
    #
    # 基本结构：
    #
    # python
    # try:
    #     # 尝试执行可能出错的代码
    #     可能会出错的代码
    # except 某种异常类型:
    #     # 如果出现了那种异常，就执行这里的代码
    #     处理错误的代码

    # 2. 修改商品
    elif choice == "2":
        name = input("请输入要修改的商品名称：")
        if name not in cart:
            print("购物车中没有该商品，请先添加。")
            continue
        try:
            new_price = float(input("请输入新的商品价格："))
            new_quantity = int(input("请输入新的商品数量："))
        except ValueError:
            print("价格请输入数字，数量请输入整数！")
            continue
        cart[name]["price"] = new_price
        cart[name]["quantity"] = new_quantity
        print(f"商品 {name} 修改成功！")

    # 3. 删除商品
    elif choice == "3":
        name = input("请输入要删除的商品名称：")
        if name in cart:
            del cart[name]
            print(f"商品 {name} 已删除。")
        else:
            print("购物车中没有该商品。")

    # 4. 查询购物车
    elif choice == "4":
        if not cart:
            print("购物车为空。")
        else:
            print("\n当前购物车商品列表：")
            for name, info in cart.items():
                print(f"商品名称：{name}，商品价格：{info['price']}，商品数量：{info['quantity']}")

    # 5. 退出系统
    elif choice == "5":
        print("感谢使用，再见！")
        break

    # 输入错误处理
    else:
        print("无效选择，请输入1-5之间的数字。")