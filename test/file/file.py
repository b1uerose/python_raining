"""
 * 文件操作
 * Author: xiaojl
 * Date:2023-10-05 23:48
"""

f = open("/Users/xiao/Desktop/python/file_test.txt", "r", encoding="utf-8")

print(f.read(10))
# file_data = f.read()
# 
# print(file_data)

# file_list = f.readlines()
# print(file_list)

for line in f:
    print(line, end="")

f.close()

with open("/Users/xiao/Desktop/python/file_test.txt", "r", encoding="utf-8") as file_obj:
    for line in file_obj:
        print(line, end="")


with open("/Users/xiao/Desktop/python/file_practise.txt", "r", encoding="utf-8") as file_practise_obj:
    total_count = 0
    for line in file_practise_obj:
        count = line.count("itheima")
        total_count += count
    print(f"itheima的出现次数为:{total_count}")