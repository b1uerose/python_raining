"""
 * json test
 * Author: xiaojl
 * Date:2023-10-07 23:56
"""

import json

data = [{"name": "张山", "age": 20}, {"name": "lisi", "age": 30}]
json_str_str = str(data)
print("字符串方法：" + json_str_str)

json_str = json.dumps(data, ensure_ascii=False)
print("json工具：" + json_str)

# print(json.loads(json_str_str))
print(json.loads(json_str))
print(type(json.loads(json_str)))


