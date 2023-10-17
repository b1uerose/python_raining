"""
 * 数据容器的通用函数
 * Author: xiaojl
 * Date:2023-10-05 20:44
"""

my_list = [1, 4, 3, 5, 2]
my_tuple = (1, 4, 3, 5, 2)
my_str = "bacgfed"
my_set = {1, 4, 3, 5, 2}
my_dict = {"key1": 1, "key5": 5, "key4": 4, "key2": 2, "key3": 3}

# 查看数据容器的元素个数
print(f"查看列表元素的个数{len(my_list)}")
print(f"查看元组元素的个数{len(my_tuple)}")
print(f"查看字符串元素的个数{len(my_str)}")
print(f"查看集合元素的个数{len(my_set)}")
print(f"查看字典元素的个数{len(my_dict)}")
print()

# max
print(f"查看列表元素的最大值{max(my_list)}")
print(f"查看元组元素的最大值{max(my_tuple)}")
print(f"查看字符串元素的最大值{max(my_str)}")
print(f"查看集合元素的最大值{max(my_set)}")
print(f"查看字典元素的最大值{max(my_dict)}")
print()

# min
print(f"查看列表元素的最小值{min(my_list)}")
print(f"查看元组元素的最小值{min(my_tuple)}")
print(f"查看字符串元素的最小值{min(my_str)}")
print(f"查看集合元素的最小值{min(my_set)}")
print(f"查看字典元素的最小值{min(my_dict)}")
print()

# sum
print(f"查看列表元素的合计{sum(my_list)}")
print(f"查看元组元素的合计{sum(my_tuple)}")
# print(f"查看字符串元素的合计{sum(my_str)}")
print(f"查看集合元素的合计{sum(my_set)}")
# print(f"查看字典元素的合计{sum(my_dict)}")
print()

# sorted 排序
print(f"查看列表元素排序{sorted(my_list, reverse=False)}")
print(f"查看元组元素排序{sorted(my_tuple)}")
print(f"查看字符串元素排序{sorted(my_str)}")
print(f"查看集合元素排序{sorted(my_set)}")
print(f"查看字典元素排序{sorted(my_dict)}")
print()

# any 查看是否有true的元素
print(any(my_list))

# all 是否所有的元素都是true
print(all(my_list))

# 返回迭代器 enumerate
print(enumerate(my_set))
for index, value in enumerate(my_dict):
    print(f"index:{index} value:{value}")

# 返回方向的迭代器 reversed
print(reversed(my_str))
print(list(reversed(my_str)))