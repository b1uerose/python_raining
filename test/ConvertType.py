"""
 * 类型转换
 * Author: xiaojl
 * Date:2023-09-11 23:07
"""

number_str = "1"

number_integer = int(number_str)
print("转换成int:", int(number_integer), " 类型为:", type(number_integer))

number_digital = float(number_str)
print("转换成浮点型:", number_digital, " 类型为:", type(number_digital))

number = 1000
convert_to_string = str(number)
print("转换成字符:", convert_to_string, " 类型为:", type(convert_to_string))

print("把3.141592653转成整数:", int(3.141592653))

