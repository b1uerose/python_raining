"""
 * 继承
 * Author: xiaojl
 * Date:2023-10-11 23:51
"""


class Phone:
    serial_no = None
    producter = None

    def call_by_4g(self):
        print("4g通话")


class IPhone(Phone):
    face_id = None

    __touch_id = "private touch id"

    def call_by_5g(self):
        print("iphone 支持5g")

    def call_by_4g(self):
        super().call_by_4g()
        print("iphone 也支持4g")

    def __check_power(self):
        print("电量充足？？？")
        return "nonono"


phone = IPhone()
phone.call_by_4g()
phone.call_by_5g()
print(phone.__class__)
print(phone._IPhone__touch_id)
print(phone._IPhone__check_power())


class Parent1:

    def __init__(self):
        self.name = "Parent1"
        self.age = 11

    def sya_hi(self):
        print("Parent1")


class Parent2:

    def __init__(self):
        self.name = "Parent2"
        self.age = 22

    def sya_hi(self):
        print("Parent2")


class Parent3:

    def sya_hi(self):
        print("Parent3")

    def __iter__(self):
        return self

    def __next__(self):
        self.index += 1
        if self.index == len(self.data):
            raise StopIteration
        return self.data[self.index]

    def __init__(self, data):
        self.name = "Parent3"
        self.age = 33
        self.index = -1
        self.data = data


class Child(Parent1, Parent2, Parent3):

    def sya_hi(self):
        super().sya_hi()
        Parent1.sya_hi(self)
        Parent2.sya_hi(self)
        Parent3.sya_hi(self)

        print("child")


child_01 = Child()
print("====override====")
child_01.sya_hi()
print("========")

print(child_01.name)
print(child_01.age)

print(isinstance(child_01, child_01.__class__))
print(isinstance(child_01, Parent1))
print(isinstance(child_01, Parent2))
print(isinstance(child_01, Parent3))

print("========")
print(issubclass(child_01.__class__, float))
print(issubclass(child_01.__class__, Parent1))

rev = Parent3("xiaojl123")
for i in rev:
    print(i)


def reverse(data):
    for index in range(len(data) - 1, -1, -1):
        yield data[index]


for i in reverse("xiaojl123"):
    print(i, end="")
