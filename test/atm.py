"""
 * 
 * Author: xiaojl
 * Date:2023-09-28 23:39
"""

amount = 500000
name = input(print("请输入您的名称"))


def query_balance():
    print(f"{name}的余额为{amount}")


def deposit():
    mny = float(input(print("请输入要存款的金额:")))
    global amount
    amount += mny
    print(f"存入{mny},余额为{amount}")


def draw():
    mny = float(input(print("请输入要取款的金额:")))
    global amount
    amount -= mny
    print(f"取款{mny},余额为{amount}")


def main_menu():
    while True:
        operation = input(print(f"""
            {name}您好，请输入您需要的操作
            【1】查询余额
            【2】存款
            【3】取款
            【其他按键】退出
        """))

        if operation == "1":
            query_balance()
        elif operation == "2":
            deposit()
        elif operation == "3":
            draw()
        else:
            exit_atm = input(print("确定要退出吗？？？"))
            if exit_atm in ['y', 'yes']:
                break


main_menu()
