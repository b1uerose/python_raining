"""
 * 集合 set
 * Author: xiaojl
 * Date:2023-10-03 20:31
"""

my_set = {"hello", "world", "hello", "world"}
my_set_empty = set()

print(f"myset的内容是:{my_set},类型是{type(my_set)}")
print(f"my_set_empty的内容是:{my_set_empty},类型是{type(my_set_empty)}")

# add element
my_set.add("new world")
print(f"添加元素后，集合的内容为{my_set}")

# remove element 如果元素不在集合中会报错
my_set.remove("world")
print(f"移除元素后，集合的内容为{my_set}")

# discard(element) 丢弃元素，如果元素不在集合中不做任何处理
my_set.discard("1111")
print(f"集合丢弃元素后，如果元素不在集合中，不做任何处理 {my_set}")

# 随机移除一个元素 pop
my_set.pop()
print(f"随机移除元素后，集合的内容为{my_set}")

set1 = {1, 2, 3}
set2 = {3, 4, 5}

print(f"合并集合: {set1.union(set2)}")
print(f"交集：{set1.intersection(set2)}")
print(f"差集：{set1.difference(set2)}")
print(f"对称差集：{set1.symmetric_difference(set2)}")

set1.intersection_update()

employee_info = {}
employee_info['wang'] = {'dept': '科技部', 'salary': 1000, "level": 1}
employee_info['zhou'] = {'dept': '科技部', 'salary': 2000, "level": 2}

for employee in employee_info:
    employee_detail = employee_info[employee]
    level = employee_detail['level']
    if level == 1:
        employee_detail['salary'] = employee_detail['salary'] + 1000
        employee_detail['level'] = employee_detail['level'] + 1

print(employee_info)
