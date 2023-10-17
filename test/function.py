"""
 * 函数的定义
 * Author: xiaojl
 * Date:2023-09-18 12:29
"""


# define a function
def fib(n):
    """定义一个函数"""
    a, b = 0, 1
    while a < n:
        print(a, end=" ")
        a, b = b, a + b
    print()


fib(1000)

# function default value
# def ask_ok(prompt, retries=4, reminder="please try later"):
#     while True:
#         ok = input(prompt)
#         if ok in ('y', 'yes', 'ye'):
#             return True
#         elif ok in ('n', 'no'):
#             return False
#         else:
#             retries -= 1
#         if retries < 0:
#             raise ValueError("invalid user respond")
#         print(reminder)
# 
# 
# ask_ok("Are you really want to quit?")
# ask_ok("Are you really want to quit?", 2)
# ask_ok("Are you really want to quit?", 1, "come on, only yes or no!")

# 默认值，基本数据类型和对象
i = 6


def default_value1(arg=i):
    print(arg)


i = 7
default_value1()


def default_value2(a, L=[]):
    L.append(a)
    print(L)


default_value2(1)
default_value2(2)
default_value2(3)


# 关键字参数
def keywork_args(first, second="second", third="third", fourth="fourth"):
    """
    关键字
    :param first: first
    :param second: second
    :param third: third
    :param fourth: fourth
    :return: None
    """
    print(first)
    print(second)
    print(third)
    print(fourth)


keywork_args(111)
print()
keywork_args("first", fourth="twenty")
keywork_args("hello", "21")
# keywork_args(first="first", "second") 关键字参数必须在位置参数后面
keywork_args(second="third", first="100000000")


# 特殊参数
def standard(arg):
    print(arg)


def position_only(arg, /):
    print(arg)


def keyword_only(*, arg):
    print(arg)


standard("hello")
standard(arg="world")

position_only("hello, world")

keyword_only(arg="hello, world")


def foo(name, /, **keywords):
    return 'name' in keywords


ret = foo("xiaojl", **{"name": "xiaojl"})
print(ret)

# unpack
unpack_args = [3, 6]

# print(range(*unpack_args))
list(range(*unpack_args))

for i in range(*unpack_args):
    print(i)

name_dictionary = {"firstname": "xiao", "lastname": "jinlong"}


def unpack_args_dictionary(firstname, lastname):
    print(firstname, lastname)


unpack_args_dictionary(**name_dictionary)

number = 200


def global_variable():
    global number
    number = 100


global_variable()
print(number)


def multi_return_values():
    return 1, 2


x, y = multi_return_values()

print(f"函数多返回值:{x} {y}")


def compute(x, y):
    return x + y


def testfunc(computexxx):
    print(type(computexxx))
    return computexxx(1, 2)


print(testfunc(compute))

anonymous = lambda w, z: x + y

print(anonymous(1, 2))


