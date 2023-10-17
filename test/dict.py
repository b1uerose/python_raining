"""
 * 字典的操作
 * Author: xiaojl
 * Date:2023-10-03 23:54
"""

# 定义字典
dict1 = {"xiaojl": 100, "sunl": 99, "xiaoyt": 100}
dict2 = {}
dict3 = dict()

print(f"dict1的内容为{dict1}, 类型为{type(dict1)}")

print(dict1.keys())
print(type(dict1.keys()))

print("111" in dict1)

# print(dict1['111'])

print(dict1.get("111", "default value"))

dict1["xiaoxx"] = 88

print(dict1)

dict1["xiaojl"] = 99

print(dict1)

dict1.setdefault("xiaojl", 77)

print(dict1)

dict4 = dict.fromkeys(['a', 'b', 'c'])

print(dict4)

print(dict1.items())

for key, value in dict1.items():
    print(f"key:{key} value:{value}")

keys = dict1.keys()
for key in dict1:
    print(f"key:{key} value:{dict1[key]}")


for key in dict1:
    print(f"key:{key} value:{dict1[key]}")


print("xiaojl" in dict1)

print(dict1.values())
print(type(dict1.values()))


