"""
 * 类型注解
 * Author: xiaojl
 * Date:2023-10-16 22:19
"""

var1: int = 100
var2: str = "hello world"


class Student:
    pass


stu1: Student = Student()


my_dict: dict[str, int] = {"age": 24, "value": "hello"}

print(my_dict)

my_tupe: tuple[int, str, str] = (1, "string", "111")

print(my_tupe)

# type: int
var3 = 100

