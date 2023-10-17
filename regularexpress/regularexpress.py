"""
 * 正则表达式测试
 * Author: xiaojl
 * Date:2023-10-13 09:58
"""
import re

str_test = "Cats are smarter than dogs"
pattern = r"(.*) ARE (.*?) .*"

print("=====================MATCH=====================")
match_obj = re.match(pattern, str_test, re.I)
print(match_obj)
print(match_obj.groups())
if match_obj is not None:
    print(match_obj.group())
    print(match_obj.group(0))
    print(match_obj.group(1))
    print(match_obj.group(2))
else:
    print(match_obj)

print(re.match(pattern, str_test, re.I).span())

print("hello\n\rwld\n\rguapi")

print("=====================SEARCH=====================")
str_test = "big dogs and small dogs"
pattern = r"dog"
print(re.search(pattern, str_test).span())

print("=====================SUB=====================")

phone = "2004-959-559 # 这是一个电话号码"

print("电话号码:" + re.sub(r"\D", "", phone))
print("电话号码:" + re.sub(r'#.*$', "", phone))

s = 'A23G4HFD567'

def double_value(matched):
    int_value = int(matched.group("value"))
    return str(int_value * 2)


print(re.sub('(?P<value>(\d+))', double_value, s, count=2))

print(re.split('(\W+)', ' runoob, runoob, runoob.'))
