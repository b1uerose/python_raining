"""
 * while
 * Author: xiaojl
 * Date:2023-09-17 23:20
"""
import random

time = 0
while time < 100:
    print(f"次数为{time},继续循环")
    time += 1
else:
    print("到了 结束循环")

# 合计值
cycle_time = 100
number_count = 0
while cycle_time > 0:
    number_count += cycle_time
    cycle_time -= 1

print(f"1~100的合计值为{number_count}")

# 九九乘法口诀表

i = 1
while i <= 9:
    j = 1
    while j <= i:
        print(f"{j} x {i} = {i * j}\t", end="")
        j += 1
    i += 1
    print()

# 猜数字
guess_time = 0
guess_number = random.randint(1, 100)

# print("请输入要猜的数字")
# while True:
#     input_number = int(input("请输入要猜的数字:"))
#     guess_time += 1
#     if input_number == guess_number:
#         print(f"恭喜你，猜对了。你总共猜了{guess_time}次！")
#         break
#     elif input_number > guess_number:
#         print("你猜的数字大了！")
#     else:
#         print("你猜的数字小了！")
