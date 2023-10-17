"""
 * 文件写操作
 * Author: xiaojl
 * Date:2023-10-06 15:23
"""

import module.module1

f = open("/Users/xiao/Desktop/python/file_write_test.txt", "w", encoding="UTF-8")

f.write("guapi")

f.close()

f = open("/Users/xiao/Desktop/python/file_write_test.txt", "a", encoding="UTF-8")

f.write("\n是狗狗")

f.close()
