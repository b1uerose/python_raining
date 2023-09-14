"""
 * 字符串
 * Author: xiaojl
 * Date:2023-09-12 22:22
"""

# 1、字符串的4种定义方式
name1 = 'xiaojinlong'
name2 = "xiaojinlong"
name3 = """xiao
jin
long"""
name4 = '''xiaojinlong'''

print(name1)
print(name2)
print(name3)
print(name4)

# 2、拼接字符串

print("你好" "中国")


# 3、字符串格式化
print("my name is %s" % name1)

age = 34
weight = 60
print("my age is %s, and my weight is %fKg" % (age, weight))

# 4、数值的宽度和精度

number_width = 10
print("数值的宽度设置为5,10的显示结果为%5d" % number_width)

float_digital_width = 11.345
print("%7.2f" % float_digital_width)

# 字符串格式化的第二种方式

name = "xiaojinlong"
age = 35.345

print(f"my name is {name}, and my age is {round(age, 2)}")


# 格式化表达式

day = 7
print(f"经过{day}的增长后，股票价格为{round(19.99*(1.2**day), 2) }")

