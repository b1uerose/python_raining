"""
 * for 循环
 * Author: xiaojl
 * Date:2023-09-13 12:50
"""

animals = ["cat", "dog", "snake", "dolphin"]

for animal in animals:
    print("动物:%s单词的长度为:%d" % (animal, len(animal)))

status_collection = {'amy': 'active', 'sam': 'inactive', 'lisa': 'active'}

# TODO what is this??? dict_items([('amy', 'active'), ('sam', 'inactive'), ('lisa', 'active')])
print(status_collection.items())

for user, status in status_collection.items():
    print("%s is %s" % (user, status))

# for循环打印99乘法表

for i in range(1, 10):
    for j in range(1, i + 1):
        print(f"{j} x {i} = {i * j}\t", end="")
    print()
