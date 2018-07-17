# author:  yijie
# data:  2018/6/6
# 商品清单
product_list = [

    ("book", 109),
    ("iphone", 5388),
    ("BMW 730", 760000),
    ("adidas", 799),
    ("iMac", 28999),
]
# 输入你手中的钱
savings = input("input your money:")
shopping_car = []
if savings.isdigit():
    savings = int(savings)
    while True:

        for i,v in enumerate(product_list, 1):  # 将商品清单写出来
            print(i,">>>",v)

        choice = input("select you goods:")  # 你选择的物品

        if choice.isdigit():    # 如果输入合法
            choice = int(choice)    # 将输入转换成数字整型
            if (choice > 0) and (choice <= len(product_list)):  # 如果输入在正确范围内
                p_item = product_list[choice - 1]   # 将product_list的所选择的元素赋值给p_item
                if p_item[1] < savings:  # 如果能买的下
                    savings -= p_item[1]    # 计算剩余的钱
                    shopping_car.append(p_item)     # 将买到的商品加入购物车
                else:
                    print("余额不足！还剩%s" % savings)
                print(p_item)       # 余额不足，并打印购物车
            else:
                print("编码不存在！")     # 或者编码不存在
        elif choice == "Q":     # 退出程序，退出前将购物车打印
            print('-------------您购买的商品如下--------------')

            for i in shopping_car:
                print(i)
            print("您还剩余%s元钱" % savings)
            break
        else:
            print("invalid input")