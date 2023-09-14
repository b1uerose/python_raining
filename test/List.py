"""
 * 列表。 List 有序、可变的集合 
 * Author: xiaojl
 * Date:2023-09-12 11:51
"""

# 定义 和 java的数组很像，但是是可以变的
number_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(number_list)

# 索引访问和切片

print(number_list[2])

# 倒数第1个元素
print(number_list[-1])

print(number_list[9])

# 浅拷贝
print(number_list[:])

print(type(number_list))

number_list2 = [11, 12, 13]

print(number_list + number_list2)

number_list.append()