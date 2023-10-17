"""
 * 列表。 List 有序、可变的集合 
 * Author: xiaojl
 * Date:2023-09-12 11:51
"""

# 定义 和 java的数组很像，但是是可以变的
number_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

print(number_list[-1:-9:-2])

print(number_list[1:10:-2])

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

number_list.append(11)

print(number_list[:2])

# 列表操作
list_operation = []
# append 在末尾添加
list_operation.append(1)
list_operation.append(2)
list_operation.append(3)
list_operation.append(4)
list_operation.append(5)
print(list_operation)

# insert(i, x) 在索引中插入元素
list_operation.insert(0, 0)
print(list_operation)

# pop
list_operation.append("x")
print(list_operation.pop())
print(list_operation.pop(0))

# clear
# list_operation.clear()
# print(list_operation)
# index(x, [start [, end]])


# count

# sort


# reverse


# copy 浅拷贝

list_operation.index(1)

# extend
list_operation.extend([1, 2, 3, 4, 5, 6])
print(list_operation)

# 删除元素的两种方式
# 1. del list[index]
# 2. list.pop(index)

del list_operation[1]
list_operation.pop(0)
print(list_operation)

list_operation.remove(3)

print(list_operation)

print(list_operation.count(4))

# 清空列表
del list_operation[:]
print(list_operation)

# practise 学生年龄
student_ages = [21, 25, 21, 23, 22, 20]
student_ages.append(31)
student_ages.extend([29, 33, 30])

print(student_ages)

print(student_ages.pop(0))
print(student_ages.pop())
print(student_ages.index(31))

student_ages.pop()

print("for循环遍历list")
for student_age in student_ages:
    print(student_age)

print("while遍历list")
index = 0
while index < len(student_ages):
    print(student_ages[index])
    index += 1

list2 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

index = 0
newlist2 = []
while index < len(list2):
    if list2[index] % 2 == 0:
        newlist2.append(list2[index])
    index += 1
print(newlist2)

newlist2.clear()

for num in list2:
    if num % 2 == 0:
        newlist2.append(num)

print(newlist2)

new_set = set(newlist2)
print(new_set)

print("===============")
new_list = [1, 2, 3, 4, 5, 6]

if 1 not in new_list:
    print("1 不在列表中")
else:
    print("1 在列表中")

# print(new_list.reverse())
new_list.reverse()
print(new_list)

new_list = [num ** 2 for num in new_list if num > 3]
print(new_list)

# print(dir())
# print(__doc__)
# print(__file__)
# print(__loader__)
# print(__builtins__)
# print(__spec__)
# print(__name__)

a = ['1', '2', '3', '8']
b = ['5', '6', '7']

for x, y in zip(a, b):
    print(x + y, end=" ")
