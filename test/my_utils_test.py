"""
 * 
 * Author: xiaojl
 * Date:2023-10-07 22:40
"""

import my_utils.str_utils
from my_utils import file_utils

print(my_utils.str_utils.str_reverse("xiaojl"))
print(my_utils.str_utils.substr("xiaojl", 0, 4))

file_utils.print_file_info("/Users/xiao/Desktop/python/file_practise1111.txt")

file_utils.append_to_file("/Users/xiao/Desktop/python/file_write_test.txt", "\nHello kitty")
