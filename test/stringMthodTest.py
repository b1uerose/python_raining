"""
 * 字符串方法测试
 * Author: xiaojl
 * Date:2023-10-03 13:00
"""

# 大小写

print("hello".capitalize())

print("hello".upper())

print("HELLO".lower())

print("hello world!".title())

# 去掉空格
print(" hello ".strip())

print(" hello ".lstrip())
print(" hello ".rstrip())

print("hello".index("l"))
print("hello".find("x"))


# 字符串替换
print("hello world".replace("world", "python"))


# startwith
print("hello world".startswith(("he", "hi")))

print("hello world".endswith(("d", "h", "a")))

# 切割成列表

print(type("hello,world,china".split(",")))

print("31225".isdecimal())

print("111".isdigit())

print(len("hello world"))

print("111hello 111 world222".strip("12"))

for element in "hello":
    print(element)

print("hello".count("x"))
