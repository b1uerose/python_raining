"""
 * 循环break
 * Author: xiaojl
 * Date:2023-09-14 22:17
"""

for n in range(2, 10):
    for x in range(2, n):
        if n % x == 0:
            print(n, "equals", x, "*", n // x)
            break
    else:
        print("%d is a prime number" % n)

