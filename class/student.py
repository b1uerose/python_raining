"""
 * class
 * Author: xiaojl
 * Date:2023-10-10 22:33
"""


class Student:
    # name = None
    # age = None
    # gender = None

    __private_attribute = None

    def __init__(self, name, age, gender):
        self.name = name
        self.age = age
        self.gender = gender
        self.__private_method()

    def say_hi(self):
        print(f"Hello, my name is {self.name}")

    def __str__(self):
        return f"学生的姓名为：{self.name}，年龄为：{self.age}，性别为：{self.gender}"

    def __private_method(self):
        print("hello, 私有方法")


stu_1 = Student(name="xiaojl", age=19, gender="male")
# stu_1.name = 'rain'
stu_1.say_hi()

print(stu_1)
print(str(stu_1))
# stu_1.__private_attribute
