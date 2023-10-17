"""
 * 文件工具类
 * Author: xiaojl
 * Date:2023-10-07 22:34
"""


def print_file_info(file_path):
    file_obj = None
    try:
        file_obj = open(file_path, "r", encoding="UTF-8")
        for line in file_obj:
            print(line)
    except Exception as e:
        print(e)
        print("文件不存在")
    finally:
        if file_obj is not None:
            file_obj.close()


def append_to_file(file_path, string):
    file_obj = open(file_path, "a", encoding="UTF-8")
    file_obj.write(string)
