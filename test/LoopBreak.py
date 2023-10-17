"""
 * 循环break
 * Author: xiaojl
 * Date:2023-09-14 22:17
"""
import random

for n in range(2, 10):
    for x in range(2, n):
        if n % x == 0:
            print(n, "equals", x, "*", n // x)
            break
    else:
        print("%d is a prime number" % n)

salary_amount = 10000

for employee_no in range(1, 21):
    if salary_amount <= 0:
        print("工资发完了，下个月再来吧！")
        break
    performance = random.randint(1, 10)
    if performance < 5:
        print(f"员工{employee_no}的绩效为{performance}，小于5，不能领取工资！")
        continue
    print(f"员工{employee_no}的绩效为{performance}，领取工资1000")
    salary_amount -= 1000
