"""
 * 异常处理
 * Author: xiaojl
 * Date:2023-10-06 16:13
"""
file_obj = None
try:
    file_obj = open("/Users/xiao/Desktop/python/file_except.txt", "r")
except:
    print("没有找")
    file_obj = open("/Users/xiao/Desktop/python/file_except.txt", "w")

print(file_obj.readline())

try:
    print("hello" + 1 / 0)
except Exception as e:
    print(e)
else:
    print("没有出现异常,else字句会执行")
finally:
    print("不管怎么样都，finally都会执行！")

# try:
#     open("hello")
# except OSError:
#     raise RuntimeError("unable to handle error")


try:
    open("hello")
except OSError as e:
    e.add_note("error 1")
    e.add_note("error 2")
    raise

# def func():
#     excepts = [ValueError('error 1'), RuntimeError('error 2')]
#     raise ExceptionGroup('exception group', excepts)


# func()


