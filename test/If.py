"""
 * if 控制流
 * Author: xiaojl
 * Date:2023-09-13 12:38
"""

num = int(input("please enter a number :"))

if num < 0:
    print("you have just entered a negative number !")
elif num == 0:
    print("you have entered a zero !")
else:
    print("great job!!")

if num != 100:
    print(f"输入的金额为{num},不等于100")

if 10 < num < 20:
    print(f"输入的金额介于10和20")
